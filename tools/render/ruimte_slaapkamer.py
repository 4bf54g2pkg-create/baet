"""Visualisatie slaapkamer: 646 Khaki leer (Linea, 5 mm) achter het bed, nachtkastjes en hanglampen."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 4 * P.PANEL_W, 4.2, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.85, 0.83, 0.79)), P.mat('x', (0.3, 0.3, 0.3)),
             win=(1.2, 3.2, 0.6, 2.35), sun_dir=(1.0, 0.7, -0.33), sun_energy=5.0, day=170, fill=25)
P.oak_floor(-0.2, RW + 0.2, -1.6, RD, tint=(0.98, 0.94, 0.88))
P.panel_wall('646', 0, RD, 0, 4, h=RH, thick=0.005, joint=0.0012)
lin = P.mat('linnen', (0.86, 0.84, 0.8), rough=1.0)
nt = lin.node_tree; b = nt.nodes['Principled BSDF']; b.inputs['Sheen Weight'].default_value = 0.5
n = nt.nodes.new('ShaderNodeTexNoise'); n.inputs['Scale'].default_value = 400; n.inputs['Detail'].default_value = 6
bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.25
nt.links.new(n.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
plaid = P.mat('plaid', (0.42, 0.33, 0.26), rough=1.0)
base = P.mat('bedstof', (0.58, 0.54, 0.48), rough=1.0)
cx = RW / 2
by = RD - 0.005 - 1.05
P.rounded('bodem', (1.9, 2.12, 0.34), (cx, by, 0.17), base, radius=0.04)
dv = P.rounded('bed', (1.84, 2.06, 0.3), (cx, by, 0.47), lin, radius=0.11, levels=3)
tex = P.bpy.data.textures.new('plooien', 'CLOUDS'); tex.noise_scale = 0.3
dm = dv.modifiers.new('plooi', 'DISPLACE'); dm.texture = tex; dm.strength = 0.025
P.rounded('plaid', (1.9, 0.5, 0.035), (cx, by - 0.62, 0.63), plaid, radius=0.017)
for k, dx in enumerate([-0.45, 0.45]):
    P.rounded(f'kussen{k}', (0.68, 0.22, 0.45), (cx + dx, RD - 0.17, 0.8), lin, radius=0.105)
P.rounded('kussen-voor', (0.5, 0.14, 0.32), (cx + 0.15, RD - 0.34, 0.76), plaid, radius=0.06)
oak = P.img_mat('meubel-eik', f'{P.TEX}/p607.jpg', rough=0.45, bump=0.2, tint=(0.92, 0.86, 0.78))
black = P.mat('zwart-mat', (0.02, 0.02, 0.02), rough=0.4, metal=0.5)
for k, sx in enumerate([cx - 1.25, cx + 1.25]):
    P.box(f'nachtkast{k}', (0.45, 0.38, 0.38), (sx, RD - 0.005 - 0.19, 0.42), oak, bevel=0.004)
    P.cyl(f'snoer{k}', 0.002, 1.2, (sx, RD - 0.25, RH - 0.6), black, verts=8)
    P.sphere(f'lamp{k}', 0.1, (sx, RD - 0.25, RH - 1.3), P.mat('opaal', (1, 1, 1), rough=0.3, emit=(1, 0.82, 0.6), emit_strength=7))
P.rounded('boek', (0.22, 0.16, 0.03), (cx - 1.25, RD - 0.2, 0.627), P.mat('boek', (0.3, 0.32, 0.3), rough=0.8), radius=0.003, levels=1)
P.cyl('kaars', 0.035, 0.08, (cx + 1.25, RD - 0.2, 0.651), P.mat('kaars', (0.9, 0.88, 0.84), rough=0.6))
P.level_camera((RW - 0.7, 0.2, 1.3), 18, lens=24, shift=(0, -0.03), dof=3.8, fstop=8)
P.render(out)
