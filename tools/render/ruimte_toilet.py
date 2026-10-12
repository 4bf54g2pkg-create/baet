"""Visualisatie toilet: 666 White Slate glans (Linea, 5 mm) op achter- en zijwand, hangtoilet."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 1.22, 1.75, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.86, 0.85, 0.82)), P.microcement((0.36, 0.35, 0.33), 'mc-donker'),
             win=(1.0, 1.5, 1.75, 2.35), sun_dir=(1.0, 0.25, -0.55), sun_energy=6.0, day=60, fill=18)
P.panel_wall('666', 0, RD, 0, 1, h=RH, thick=0.005, joint=0.0012)
# rechterwand: panelen langs y, voorkant naar -x
P.panel_wall('666', 0.0, RW, 0, 2, h=RH, axis='y', thick=0.005, joint=0.0012, facing=-1, name='zij')
white = P.mat('keramiek', (0.93, 0.92, 0.9), rough=0.07, coat=0.5)
black = P.mat('zwart-mat', (0.025, 0.025, 0.025), rough=0.38, metal=0.7)
cx = RW / 2
# hangtoilet: pot + zitting + deksel
P.rounded('pot-achter', (0.30, 0.20, 0.26), (cx, RD - 0.005 - 0.10, 0.30), white, radius=0.09, levels=3)
P.bpy.ops.mesh.primitive_cone_add(vertices=96, radius1=0.12, radius2=0.18, depth=0.30, location=(cx, RD - 0.33, 0.28))
pot = P.bpy.context.active_object; pot.name = 'pot'; pot.scale = (0.95, 1.25, 1); pot.data.materials.append(white)
bv = pot.modifiers.new('bevel', 'BEVEL'); bv.width = 0.03; bv.segments = 5; bv.limit_method = 'ANGLE'
sd = pot.modifiers.new('sub', 'SUBSURF'); sd.levels = 2; sd.render_levels = 2
P.bpy.ops.object.shade_smooth()
seat = P.cyl('zitting', 0.18, 0.022, (cx, RD - 0.33, 0.441), white, verts=96, bevel=0.009); seat.scale = (0.96, 1.26, 1)
lid = P.cyl('deksel', 0.175, 0.016, (cx, RD - 0.335, 0.46), white, verts=96, bevel=0.007); lid.scale = (0.95, 1.24, 1)
P.box('scharnier', (0.12, 0.02, 0.015), (cx, RD - 0.035, 0.45), P.mat('chroom', (0.8, 0.8, 0.8), rough=0.15, metal=1.0), bevel=0.004)
# bedieningsplaat, mat zwart
P.box('drukplaat', (0.25, 0.012, 0.16), (cx, RD - 0.011, 1.05), black, bevel=0.003)
P.box('knop1', (0.1, 0.004, 0.13), (cx - 0.055, RD - 0.019, 1.05), black, bevel=0.002)
P.box('knop2', (0.1, 0.004, 0.13), (cx + 0.055, RD - 0.019, 1.05), black, bevel=0.002)
# toiletrolhouder rechts
P.cyl('rolhouder', 0.006, 0.12, (RW - 0.06, RD - 0.55, 0.75), black, rot=(0, math.radians(90), 0))
P.cyl('rol', 0.055, 0.1, (RW - 0.07, RD - 0.55, 0.75), P.mat('papier', (0.95, 0.94, 0.92), rough=0.9), rot=(0, math.radians(90), 0))
# plankje met kaars en takje
shelf = P.img_mat('meubel-eik', f'{P.TEX}/p607.jpg', rough=0.45, bump=0.2, tint=(0.92, 0.86, 0.78))
P.box('plank', (0.9, 0.16, 0.025), (cx, RD - 0.085, 1.42), shelf, bevel=0.002)
P.cyl('kaars', 0.035, 0.09, (cx + 0.25, RD - 0.09, 1.478), P.mat('kaars', (0.9, 0.88, 0.84), rough=0.6))
P.rounded('vaasje', (0.07, 0.07, 0.16), (cx - 0.22, RD - 0.09, 1.513), P.mat('vaas', (0.55, 0.47, 0.40), rough=0.7), radius=0.03)
# hanglamp
P.cyl('snoer', 0.002, 0.7, (cx, RD - 0.7, RH - 0.35), black, verts=8)
P.sphere('lamp', 0.09, (cx, RD - 0.7, RH - 0.75), P.mat('opaal', (1, 1, 1), rough=0.3, emit=(1, 0.86, 0.68), emit_strength=8))
# deurwand met opening (blik vanuit de gang)
hall = P.stuc((0.80, 0.78, 0.74)) if False else P.mat('gangwand', (0.78, 0.76, 0.72), rough=0.9)
P.box('deur-l', (0.21, 0.1, RH), (0.105, -0.05, RH / 2), hall)
P.box('deur-r', (0.21, 0.1, RH), (RW - 0.105, -0.05, RH / 2), hall)
P.box('deur-boven', (RW, 0.1, RH - 2.1), (RW / 2, -0.05, (RH + 2.1) / 2), hall)
trim = P.mat('kozijn-wit', (0.88, 0.87, 0.85), rough=0.35)
P.box('kozijn-l', (0.05, 0.12, 2.12), (0.235, -0.05, 1.06), trim, bevel=0.003)
P.box('kozijn-r', (0.05, 0.12, 2.12), (RW - 0.235, -0.05, 1.06), trim, bevel=0.003)
P.box('kozijn-b', (RW - 0.42, 0.12, 0.05), (RW / 2, -0.05, 2.125), trim, bevel=0.003)
P.area('gang', (RW / 2, -1.4, 2.4), (math.radians(40), 0, 0), size=(1.0, 0.6), energy=25, color=(1, 0.9, 0.78))
P.level_camera((RW / 2, -1.25, 1.3), 0, lens=33, shift=(0.0, -0.04), dof=2.8, fstop=7)
P.render(out)
