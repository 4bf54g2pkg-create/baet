"""Puredeco · bouwstenen voor fotorealistische visualisaties (Blender 4.2 / bpy, Cycles).

Alles in meters. Panelen zijn 1,22 m breed en 2,60 of 2,80 m hoog; het decor is de echte packshot-scan van het product
(tools/render/textuur-uit-packshot.py), 1:1 over het hele paneel, zoals het product is.
Linea = 5 mm stomp (zichtbare naad), Signature = 8 mm klik (naad vrijwel onzichtbaar).
"""
import math
import os
import bpy
import bmesh
from mathutils import Vector

TEX = os.environ.get('PD_TEX', '/tmp/claude-0/r/tex')
PANEL_W = 1.22

# Per decor: ruwheid, glans (coat), structuur (bump)
DECOR = {
    '607': dict(rough=0.48, bump=0.25, kind='hout'),
    '810': dict(rough=0.42, bump=0.25, kind='hout'),
    '811': dict(rough=0.42, bump=0.25, kind='hout'),
    '619': dict(rough=0.78, bump=0.55, kind='stof'),
    '821': dict(rough=0.80, bump=0.55, kind='stof'),
    '824': dict(rough=0.80, bump=0.55, kind='stof'),
    '646': dict(rough=0.55, bump=0.45, kind='leer'),
    '666': dict(rough=0.12, coat=0.6, bump=0.02, kind='glans'),
    '670': dict(rough=0.12, coat=0.6, bump=0.02, kind='glans'),
    '692': dict(rough=0.38, bump=0.08, kind='mat'),
    '691': dict(rough=0.55, bump=0.25, kind='beton'),
    '842': dict(rough=0.70, bump=0.9, kind='stucco'),
    '851': dict(rough=0.40, bump=0.25, kind='travertin'),
}


# ---------- basis ----------
def reset(samples=160, res=(1800, 1200)):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.render.engine = 'CYCLES'
    s.cycles.device = 'CPU'
    s.cycles.samples = samples
    s.cycles.use_adaptive_sampling = True
    s.cycles.adaptive_threshold = 0.02
    s.cycles.use_denoising = True
    s.cycles.denoiser = 'OPENIMAGEDENOISE'
    s.cycles.max_bounces = 8
    s.cycles.diffuse_bounces = 4
    s.cycles.glossy_bounces = 4
    s.cycles.transmission_bounces = 8
    s.cycles.caustics_reflective = False
    s.cycles.caustics_refractive = False
    s.cycles.blur_glossy = 1.0
    s.render.resolution_x, s.render.resolution_y = res
    s.render.resolution_percentage = 100
    s.render.film_transparent = False
    s.view_settings.view_transform = 'AgX'
    s.view_settings.look = 'AgX - Base Contrast'
    s.view_settings.exposure = 0.0
    s.render.image_settings.file_format = 'PNG'
    s.render.image_settings.color_depth = '16'
    s.render.threads_mode = 'AUTO'
    return s


def mat(name, color=(0.8, 0.8, 0.8), rough=0.5, metal=0.0, coat=0.0, trans=0.0, emit=None, emit_strength=0.0, ior=1.45):
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*color, 1)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    b.inputs['Coat Weight'].default_value = coat
    b.inputs['Transmission Weight'].default_value = trans
    b.inputs['IOR'].default_value = ior
    if emit:
        b.inputs['Emission Color'].default_value = (*emit, 1)
        b.inputs['Emission Strength'].default_value = emit_strength
    return m


def img_mat(name, path, rough=0.5, coat=0.0, bump=0.2, bump_dist=0.0015, scale=(1, 1), rot=0.0, tint=None, proj='UV'):
    """Materiaal met afbeelding als kleur en luminantie als lichte structuur."""
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    tc = nt.nodes.new('ShaderNodeTexCoord')
    mp = nt.nodes.new('ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (scale[0], scale[1], 1)
    mp.inputs['Rotation'].default_value = (0, 0, rot)
    nt.links.new(tc.outputs['UV' if proj == 'UV' else 'Object'], mp.inputs['Vector'])
    im = nt.nodes.new('ShaderNodeTexImage')
    im.image = bpy.data.images.load(path, check_existing=True)
    im.interpolation = 'Cubic'
    im.extension = 'REPEAT'
    nt.links.new(mp.outputs['Vector'], im.inputs['Vector'])
    col = im.outputs['Color']
    if tint:
        mix = nt.nodes.new('ShaderNodeMix')
        mix.data_type = 'RGBA'
        mix.blend_type = 'MULTIPLY'
        mix.inputs['Factor'].default_value = 1.0
        mix.inputs[7].default_value = (*tint, 1)
        nt.links.new(col, mix.inputs[6])
        col = mix.outputs[2]
    nt.links.new(col, b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = rough
    b.inputs['Coat Weight'].default_value = coat
    b.inputs['Coat Roughness'].default_value = 0.04
    if bump > 0:
        bw = nt.nodes.new('ShaderNodeRGBToBW')
        nt.links.new(im.outputs['Color'], bw.inputs['Color'])
        bp = nt.nodes.new('ShaderNodeBump')
        bp.inputs['Strength'].default_value = bump
        bp.inputs['Distance'].default_value = bump_dist
        nt.links.new(bw.outputs['Val'], bp.inputs['Height'])
        nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
        # ruwheid licht laten variëren met het decor (minder 'CG')
        rr = nt.nodes.new('ShaderNodeMapRange')
        rr.inputs['To Min'].default_value = rough * 0.85
        rr.inputs['To Max'].default_value = min(1.0, rough * 1.15)
        nt.links.new(bw.outputs['Val'], rr.inputs['Value'])
        nt.links.new(rr.outputs['Result'], b.inputs['Roughness'])
    return m


def decor_mat(code):
    d = DECOR[code]
    return img_mat('decor-' + code, f'{TEX}/p{code}.jpg', rough=d['rough'], coat=d.get('coat', 0.0),
                   bump=d['bump'], bump_dist=0.0008 if d['kind'] in ('glans', 'mat') else 0.0018)


def _link(ob):
    bpy.context.scene.collection.objects.link(ob)
    return ob


def box(name, size, loc, m=None, bevel=0.0, seg=3, rot=(0, 0, 0), uv_scale=None):
    """Kubus met afmetingen size (x, y, z) en middelpunt loc. UV per vlak in meters (uv_scale = meter per tegel)."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= size[0]; v.co.y *= size[1]; v.co.z *= size[2]
    uv = bm.loops.layers.uv.new()
    for f in bm.faces:
        n = f.normal
        for l in f.loops:
            c = l.vert.co
            if abs(n.z) > 0.5:
                u, v = c.x, c.y
            elif abs(n.x) > 0.5:
                u, v = c.y, c.z
            else:
                u, v = c.x, c.z
            if uv_scale:
                l[uv].uv = (u / uv_scale, v / uv_scale)
            else:
                l[uv].uv = (u, v)
    bm.to_mesh(me); bm.free()
    ob = _link(bpy.data.objects.new(name, me))
    ob.location = loc
    ob.rotation_euler = rot
    if m:
        ob.data.materials.append(m)
    if bevel > 0:
        md = ob.modifiers.new('bevel', 'BEVEL')
        md.width = bevel
        md.segments = seg
        md.limit_method = 'ANGLE'
        md.harden_normals = False
    # vlakke shading: met afschuining vangen de randen het licht, zonder schaduwfouten op grote vlakken
    for p in ob.data.polygons:
        p.use_smooth = False
    return ob


def cyl(name, r, h, loc, m=None, rot=(0, 0, 0), verts=48, bevel=0.0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc, rotation=rot)
    ob = bpy.context.active_object
    ob.name = name
    if m:
        ob.data.materials.append(m)
    if bevel:
        md = ob.modifiers.new('bevel', 'BEVEL'); md.width = bevel; md.segments = 3; md.limit_method = 'ANGLE'
    bpy.ops.object.shade_smooth_by_angle(angle=math.radians(35))
    return ob


def sphere(name, r, loc, m=None, scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=r, location=loc)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = scale
    if m:
        ob.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return ob


def rounded(name, size, loc, m, radius=0.04, levels=2, rot=(0, 0, 0)):
    """Zachte vorm (kussen, toiletpot): kubus + afronding + subdivision."""
    ob = box(name, size, loc, m, bevel=radius, seg=4, rot=rot)
    sd = ob.modifiers.new('sub', 'SUBSURF'); sd.levels = levels; sd.render_levels = levels
    for p in ob.data.polygons:
        p.use_smooth = True
    return ob


# ---------- panelen ----------
def panel_wall(code, x0, y, z0, n, h=2.6, axis='x', thick=0.005, joint=0.0012, offset_tex=True, facing=1, name='paneel'):
    """n panelen naast elkaar op een wand.
    axis 'x': wand loopt langs x, voorkant kijkt naar -y*facing (facing=1: naar de camera in -y).
    axis 'y': wand loopt langs y, voorkant naar +x*facing.
    joint: naadbreedte (Linea ~1,2 mm zichtbaar, Signature ~0,2 mm)."""
    m = decor_mat(code)
    obs = []
    total = n * PANEL_W
    if joint > 0.0005:
        # donkere lijmlaag achter de panelen: maakt de Linea-naad leesbaar zoals in het echt
        dk = mat('naad-achter', (0.02, 0.02, 0.02), rough=0.9)
        if axis == 'x':
            box(name + '-achter', (total, 0.0008, h), (x0 + total / 2, y - 0.0004 * facing, z0 + h / 2), dk)
        else:
            box(name + '-achter', (0.0008, total, h), (y + 0.0004 * facing, x0 + total / 2, z0 + h / 2), dk)
    for i in range(n):
        c = x0 + i * PANEL_W + PANEL_W / 2
        w = PANEL_W - joint
        if axis == 'x':
            ob = box(f'{name}-{i}', (w, thick, h), (c, y - facing * thick / 2, z0 + h / 2), m, bevel=0.0006, seg=2)
            # UV: voorkant 0..1 over het hele paneel
            _panel_uv(ob, 'x', w, h)
        else:
            ob = box(f'{name}-{i}', (thick, w, h), (y + facing * thick / 2, c, z0 + h / 2), m, bevel=0.0006, seg=2)
            _panel_uv(ob, 'y', w, h)
        obs.append(ob)
    return obs


def _panel_uv(ob, axis, w, h):
    me = ob.data
    uv = me.uv_layers.active.data
    for poly in me.polygons:
        for li in poly.loop_indices:
            vi = me.loops[li].vertex_index
            co = me.vertices[vi].co
            u = (co.x if axis == 'x' else co.y) / w + 0.5
            v = co.z / h + 0.5
            uv[li].uv = (u, v)


def profile(name, loc, length, axis='z', w=0.012, d=0.010, m=None):
    """Aluminium hoek-/eindprofiel."""
    m = m or mat('alu-antraciet', (0.06, 0.06, 0.065), rough=0.35, metal=1.0)
    size = {'z': (w, d, length), 'x': (length, d, w), 'y': (d, length, w)}[axis]
    return box(name, size, loc, m, bevel=0.0008, seg=2)


# ---------- licht en camera ----------
def sky(strength=1.0, elev=28, rot=200, sun=True, sun_strength=3.5, sun_size=1.5):
    w = bpy.data.worlds.new('wereld')
    bpy.context.scene.world = w
    w.use_nodes = True
    nt = w.node_tree
    bg = nt.nodes['Background']
    sk = nt.nodes.new('ShaderNodeTexSky')
    sk.sky_type = 'NISHITA'
    sk.sun_disc = False
    sk.sun_elevation = math.radians(elev)
    sk.sun_rotation = math.radians(rot)
    sk.air_density = 1.0
    sk.dust_density = 1.5
    nt.links.new(sk.outputs['Color'], bg.inputs['Color'])
    bg.inputs['Strength'].default_value = strength * 0.12
    if sun:
        ld = bpy.data.lights.new('zon', 'SUN')
        ld.energy = sun_strength
        ld.angle = math.radians(sun_size)
        ld.color = (1.0, 0.93, 0.84)
        ob = _link(bpy.data.objects.new('zon', ld))
        ob.rotation_euler = (math.radians(90 - elev), 0, math.radians(rot + 180 - 90))
        return ob


def area(name, loc, rot, size=(1, 1), energy=200, color=(1, 0.97, 0.92), portal=False, spread=180):
    ld = bpy.data.lights.new(name, 'AREA')
    ld.shape = 'RECTANGLE'
    ld.size, ld.size_y = size
    ld.energy = energy
    ld.color = color
    ld.spread = math.radians(spread)
    ld.cycles.is_portal = portal
    ob = _link(bpy.data.objects.new(name, ld))
    ob.location = loc
    ob.rotation_euler = rot
    return ob


def point(name, loc, energy=30, radius=0.03, color=(1, 0.85, 0.65)):
    ld = bpy.data.lights.new(name, 'POINT')
    ld.energy = energy
    ld.shadow_soft_size = radius
    ld.color = color
    ob = _link(bpy.data.objects.new(name, ld))
    ob.location = loc
    return ob


def camera(loc, look_at, lens=32, shift=(0, 0), dof=None, fstop=4.0, sensor=36):
    cd = bpy.data.cameras.new('cam')
    cd.lens = lens
    cd.sensor_width = sensor
    cd.shift_x, cd.shift_y = shift
    ob = _link(bpy.data.objects.new('cam', cd))
    ob.location = loc
    d = Vector(look_at) - Vector(loc)
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    if dof:
        cd.dof.use_dof = True
        cd.dof.focus_distance = dof
        cd.dof.aperture_fstop = fstop
    bpy.context.scene.camera = ob
    return ob


def level_camera(loc, yaw_deg, lens=28, shift=(0, 0), dof=None, fstop=5.6):
    """Architectuurfoto: camera waterpas (verticale lijnen recht), richting met yaw, kadrering met shift."""
    cd = bpy.data.cameras.new('cam')
    cd.lens = lens
    cd.sensor_width = 36
    cd.shift_x, cd.shift_y = shift
    ob = _link(bpy.data.objects.new('cam', cd))
    ob.location = loc
    ob.rotation_euler = (math.radians(90), 0, math.radians(yaw_deg))
    if dof:
        cd.dof.use_dof = True
        cd.dof.focus_distance = dof
        cd.dof.aperture_fstop = fstop
    bpy.context.scene.camera = ob
    return ob


def render(path):
    s = bpy.context.scene
    s.render.filepath = path
    bpy.ops.render.render(write_still=True)
    return path


# ---------- veelgebruikte materialen ----------
def stuc(color=(0.86, 0.84, 0.80)):
    m = bpy.data.materials.get('stuc')
    if m:
        return m
    m = mat('stuc', color, rough=0.9)
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    n = nt.nodes.new('ShaderNodeTexNoise'); n.inputs['Scale'].default_value = 80; n.inputs['Detail'].default_value = 8
    bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.08; bp.inputs['Distance'].default_value = 0.002
    nt.links.new(n.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
    return m


def microcement(color=(0.62, 0.60, 0.57), name='microcement'):
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = mat(name, color, rough=0.55)
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']
    tc = nt.nodes.new('ShaderNodeTexCoord')
    n1 = nt.nodes.new('ShaderNodeTexNoise'); n1.inputs['Scale'].default_value = 1.6; n1.inputs['Detail'].default_value = 12; n1.inputs['Roughness'].default_value = 0.62
    nt.links.new(tc.outputs['Object'], n1.inputs['Vector'])
    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].position = 0.35; ramp.color_ramp.elements[0].color = (color[0] * 0.86, color[1] * 0.86, color[2] * 0.86, 1)
    ramp.color_ramp.elements[1].position = 0.7; ramp.color_ramp.elements[1].color = (min(1, color[0] * 1.1), min(1, color[1] * 1.1), min(1, color[2] * 1.1), 1)
    nt.links.new(n1.outputs['Fac'], ramp.inputs['Fac']); nt.links.new(ramp.outputs['Color'], b.inputs['Base Color'])
    rr = nt.nodes.new('ShaderNodeMapRange'); rr.inputs['To Min'].default_value = 0.35; rr.inputs['To Max'].default_value = 0.7
    nt.links.new(n1.outputs['Fac'], rr.inputs['Value']); nt.links.new(rr.outputs['Result'], b.inputs['Roughness'])
    n2 = nt.nodes.new('ShaderNodeTexNoise'); n2.inputs['Scale'].default_value = 300; n2.inputs['Detail'].default_value = 4
    nt.links.new(tc.outputs['Object'], n2.inputs['Vector'])
    bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.05; bp.inputs['Distance'].default_value = 0.001
    nt.links.new(n2.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
    return m


def oak_floor(x0, x1, y0, y1, plank=0.20, length=2.2, code='607', name='vloer', tint=(1.0, 0.97, 0.93)):
    """Eiken plankenvloer uit de 607-scan: elke plank een eigen stuk van de textuur, verspringende kopse naden."""
    import random
    random.seed(7)
    m = img_mat('vloer-eik', f'{TEX}/p{code}.jpg', rough=0.5, bump=0.3, bump_dist=0.001, tint=tint)
    xs = x0
    i = 0
    obs = []
    while xs < x1:
        ys = y0 - random.random() * length
        while ys < y1:
            L = length * (0.75 + random.random() * 0.5)
            ob = box(f'{name}-{i}', (plank - 0.0015, L - 0.0015, 0.014), (xs + plank / 2, ys + L / 2, 0.003), m, bevel=0.0012, seg=2)
            # plank toont een willekeurige strook van de textuur, nerf in de lengte
            me = ob.data
            uvd = me.uv_layers.active.data
            ou, ov = random.random(), random.random()
            for poly in me.polygons:
                for li in poly.loop_indices:
                    co = me.vertices[me.loops[li].vertex_index].co
                    uvd[li].uv = (ou + co.x / 1.22 * 0.9, ov + co.y / 2.8)
            obs.append(ob)
            ys += L
            i += 1
        xs += plank
    # samenvoegen voor snelheid
    bpy.ops.object.select_all(action='DESELECT')
    for o in obs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = obs[0]
    bpy.ops.object.join()
    return bpy.context.active_object


def room_shell(RW, RD, RH, wall, floor, win=None, sun_dir=(1.0, 0.8, -0.45), sun_energy=6.0, day=150, fill=30,
               ceiling=(0.9, 0.9, 0.88), sky_rot=150):
    """Kamer x 0..RW, y 0..RD (achterwand op y=RD), z 0..RH, camera staat binnen (voorwand op y=-1,2).
    win = (y0, y1, z0, z1): raam in de linkerwand (x=0) met zon en daglicht."""
    P = globals()
    box('vloer', (RW + 1, RD + 1.6, 0.02), (RW / 2, RD / 2 - 0.8, -0.01), floor)
    box('plafond', (RW + 1, RD + 1.6, 0.02), (RW / 2, RD / 2 - 0.8, RH + 0.01), mat('plafond', ceiling, rough=0.95))
    box('achter-ruw', (RW + 1, 0.1, RH), (RW / 2, RD + 0.05, RH / 2), wall)
    box('rechts', (0.1, RD + 1.6, RH), (RW + 0.05, RD / 2 - 0.8, RH / 2), wall)
    box('voor', (RW + 1, 0.1, RH), (RW / 2, -1.6, RH / 2), wall)
    if not win:
        box('links', (0.12, RD + 1.6, RH), (-0.06, RD / 2 - 0.8, RH / 2), wall)
    else:
        wy0, wy1, wz0, wz1 = win
        box('l-a', (0.12, wy0 + 1.6, RH), (-0.06, (wy0 - 1.6) / 2, RH / 2), wall)
        box('l-b', (0.12, RD - wy1, RH), (-0.06, (wy1 + RD) / 2, RH / 2), wall)
        box('l-c', (0.12, wy1 - wy0, wz0), (-0.06, (wy0 + wy1) / 2, wz0 / 2), wall)
        box('l-d', (0.12, wy1 - wy0, RH - wz1), (-0.06, (wy0 + wy1) / 2, (RH + wz1) / 2), wall)
        frame = mat('kozijn', (0.05, 0.05, 0.05), rough=0.4, metal=0.6)
        for (sy, sz, ly, lz) in [((wy1 - wy0), 0.05, (wy0 + wy1) / 2, wz0 + 0.025), ((wy1 - wy0), 0.05, (wy0 + wy1) / 2, wz1 - 0.025),
                                 (0.05, wz1 - wz0, wy0 + 0.025, (wz0 + wz1) / 2), (0.05, wz1 - wz0, wy1 - 0.025, (wz0 + wz1) / 2)]:
            box('kozijn', (0.06, sy, sz), (-0.09, ly, lz), frame)
        box('vensterbank', (0.16, wy1 - wy0 + 0.04, 0.025), (-0.02, (wy0 + wy1) / 2, wz0 - 0.0125), mat('vensterbank', (0.8, 0.79, 0.76), rough=0.4), bevel=0.002)
        g = box('glas', (0.006, wy1 - wy0, wz1 - wz0), (-0.09, (wy0 + wy1) / 2, (wz0 + wz1) / 2), mat('glas', (1, 1, 1), rough=0.0, trans=1.0, ior=1.5))
        g.visible_shadow = False
        area('raam-portal', (-0.16, (wy0 + wy1) / 2, (wz0 + wz1) / 2), (0, math.radians(90), 0), size=(wz1 - wz0, wy1 - wy0), energy=0, portal=True)
        area('daglicht', (-0.03, (wy0 + wy1) / 2, (wz0 + wz1) / 2), (0, math.radians(90), 0), size=(wz1 - wz0, wy1 - wy0), energy=day, color=(0.9, 0.95, 1.0))
        d = Vector(sun_dir).normalized()
        ld = bpy.data.lights.new('zon', 'SUN'); ld.energy = sun_energy; ld.angle = math.radians(0.7); ld.color = (1.0, 0.92, 0.82)
        so = _link(bpy.data.objects.new('zon', ld)); so.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    sky(strength=1.0, elev=30, rot=sky_rot, sun=False)
    if fill:
        area('vul', (RW / 2, -1.3, RH - 0.3), (math.radians(60), 0, 0), size=(RW * 0.7, 1.0), energy=fill, color=(1, 0.96, 0.9))


def towel(name, size, loc, color=(0.78, 0.74, 0.68)):
    m = bpy.data.materials.get('stof-' + name) or mat('stof-' + name, color, rough=1.0)
    nt = m.node_tree
    b = nt.nodes['Principled BSDF']; b.inputs['Sheen Weight'].default_value = 0.6
    if len(nt.nodes) < 4:
        n = nt.nodes.new('ShaderNodeTexNoise'); n.inputs['Scale'].default_value = 900
        bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.4
        nt.links.new(n.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
    ob = rounded(name, size, loc, m, radius=min(size) * 0.45)
    # lichte plooien
    tex = bpy.data.textures.new(name + '-plooi', 'CLOUDS'); tex.noise_scale = 0.08
    dm = ob.modifiers.new('plooi', 'DISPLACE'); dm.texture = tex; dm.strength = 0.006
    return ob
