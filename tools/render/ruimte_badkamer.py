"""Visualisatie badkamer: 851 Travertine Ivory (Signature, 8 mm) achter een zwevend badmeubel."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 3 * P.PANEL_W, 3.2, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.84, 0.82, 0.78)), P.microcement((0.46, 0.44, 0.41)),
             win=(1.25, 2.65, 0.95, 2.3), sun_dir=(1.0, 0.85, -0.42), sun_energy=7.0, day=140, fill=35)
P.panel_wall('851', 0, RD, 0, 3, h=RH, thick=0.008, joint=0.00025)

oak = P.img_mat('meubel-eik', f'{P.TEX}/p607.jpg', rough=0.45, bump=0.2, tint=(0.92, 0.86, 0.78))
black = P.mat('zwart-mat', (0.025, 0.025, 0.025), rough=0.38, metal=0.7)
cx = RW / 2
P.box('meubel', (1.2, 0.46, 0.42), (cx, RD - 0.008 - 0.23, 0.62), oak, bevel=0.003)
P.box('meubel-naad', (0.002, 0.462, 0.40), (cx, RD - 0.008 - 0.23, 0.62), P.mat('naad', (0.02, 0.02, 0.02), rough=0.8))
P.box('greep', (1.1, 0.02, 0.012), (cx, RD - 0.008 - 0.465, 0.825), P.mat('schaduwgroef', (0.03, 0.025, 0.02), rough=0.7))
P.box('blad', (1.22, 0.48, 0.02), (cx, RD - 0.008 - 0.24, 0.84), P.mat('blad', (0.80, 0.78, 0.74), rough=0.35), bevel=0.002)
ceram = P.mat('keramiek', (0.93, 0.92, 0.9), rough=0.08, coat=0.5)
bowl = P.cyl('kom', 0.23, 0.13, (cx, RD - 0.27, 0.915), ceram, verts=96, bevel=0.01); bowl.scale = (1.0, 0.72, 1.0)
inner = P.cyl('kom-in', 0.205, 0.12, (cx, RD - 0.27, 0.93), ceram, verts=96); inner.scale = (1.0, 0.70, 1.0)
mb = bowl.modifiers.new('hol', 'BOOLEAN'); mb.object = inner; mb.operation = 'DIFFERENCE'; inner.hide_render = True
P.cyl('kraan', 0.011, 0.20, (cx, RD - 0.1, 1.07), black, rot=(math.radians(90), 0, 0))
P.cyl('kraan-rozet', 0.03, 0.012, (cx, RD - 0.012, 1.07), black, rot=(math.radians(90), 0, 0))
P.cyl('kraan-hendel', 0.022, 0.03, (cx + 0.12, RD - 0.025, 1.07), black, rot=(math.radians(90), 0, 0))
P.cyl('spiegel-rand', 0.356, 0.014, (cx, RD - 0.03, 1.6), black, rot=(math.radians(90), 0, 0), verts=128)
P.cyl('spiegel', 0.35, 0.012, (cx, RD - 0.04, 1.6), P.mat('spiegel', (0.92, 0.92, 0.92), rough=0.02, metal=1.0), rot=(math.radians(90), 0, 0), verts=128)
P.cyl('led', 0.34, 0.01, (cx, RD - 0.02, 1.6), P.mat('led', (1, 1, 1), emit=(1.0, 0.82, 0.62), emit_strength=6), rot=(math.radians(90), 0, 0), verts=128)
P.cyl('rek', 0.008, 0.6, (RW - 0.35, RD - 0.07, 1.25), black, rot=(0, math.radians(90), 0))
P.towel('handdoek', (0.42, 0.03, 0.62), (RW - 0.35, RD - 0.075, 0.96))
P.rounded('vaas', (0.09, 0.09, 0.2), (cx - 0.45, RD - 0.2, 0.95), P.mat('vaas', (0.55, 0.47, 0.40), rough=0.7), radius=0.04)
stem = P.mat('tak', (0.25, 0.2, 0.15), rough=0.8)
for i, tilt in enumerate([4, -9, 13]):
    P.cyl(f'tak{i}', 0.003, 0.55, (cx - 0.45 + math.sin(math.radians(tilt)) * 0.27, RD - 0.2, 1.32), stem, rot=(0, math.radians(tilt), 0), verts=8)
P.level_camera((RW - 0.55, 0.15, 1.2), 17, lens=24, shift=(0.0, 0.05), dof=3.2, fstop=8)
P.render(out)
