"""Visualisatie kantoor/werkplek: 619 Jade (Japandi) met een vlak akupanelen, bureau en stoel."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 3 * P.PANEL_W + 0.6, 3.4, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.86, 0.85, 0.82)), P.mat('x', (0.3, 0.3, 0.3)),
             win=(0.9, 2.9, 0.85, 2.35), sun_dir=(1.0, 0.8, -0.42), sun_energy=6.0, day=170, fill=28)
P.oak_floor(-0.2, RW + 0.2, -1.6, RD, tint=(0.97, 0.93, 0.88))
P.panel_wall('619', 0, RD, 0, 3, h=RH, thick=0.008, joint=0.00025)
# akupanelen rechts: lamellen op zwart vilt, 60 cm breed
felt = P.mat('vilt', (0.025, 0.025, 0.025), rough=1.0)
walnut = P.img_mat('lamel-noot', f'{P.TEX}/p811.jpg', rough=0.5, bump=0.2, scale=(0.3, 1))
ax0 = 3 * P.PANEL_W
P.box('vilt', (0.6, 0.012, RH), (ax0 + 0.3, RD - 0.006, RH / 2), felt)
for i in range(16):
    x = ax0 + 0.0165 + i * 0.0375
    P.box(f'lamel{i}', (0.027, 0.021, RH), (x + 0.0135 - 0.0135, RD - 0.012 - 0.0105, RH / 2), walnut, bevel=0.0008, seg=2)
oak = P.img_mat('meubel-eik', f'{P.TEX}/p607.jpg', rough=0.45, bump=0.2, tint=(0.92, 0.86, 0.78))
black = P.mat('zwart-mat', (0.02, 0.02, 0.02), rough=0.4, metal=0.5)
cx = 1.83
P.box('bureaublad', (1.6, 0.75, 0.03), (cx, RD - 0.55, 0.735), oak, bevel=0.002)
for dx in (-0.75, 0.75):
    P.box(f'poot{dx}', (0.04, 0.65, 0.72), (cx + dx, RD - 0.55, 0.36), black, bevel=0.002)
P.box('scherm', (0.62, 0.02, 0.37), (cx, RD - 0.25, 1.06), P.mat('scherm', (0.01, 0.01, 0.012), rough=0.08), bevel=0.003)
P.box('scherm-voet', (0.02, 0.02, 0.2), (cx, RD - 0.23, 0.85), black)
P.box('voetplaat', (0.22, 0.16, 0.008), (cx, RD - 0.25, 0.754), black, bevel=0.002)
P.box('toetsenbord', (0.38, 0.12, 0.012), (cx, RD - 0.7, 0.756), P.mat('toetsen', (0.85, 0.84, 0.82), rough=0.5), bevel=0.003)
P.cyl('lamp-voet', 0.07, 0.015, (cx - 0.6, RD - 0.35, 0.758), black)
P.cyl('lamp-arm', 0.006, 0.45, (cx - 0.6, RD - 0.35, 0.98), black, verts=12)
P.cyl('lamp-kap', 0.08, 0.12, (cx - 0.52, RD - 0.38, 1.2), black, rot=(0, math.radians(35), 0))
P.cyl('plant-pot', 0.06, 0.18, (cx + 0.35, RD - 0.2, 0.84), P.mat('aardewerk', (0.85, 0.82, 0.76), rough=0.5))
for k, (c, hgt) in enumerate([((0.72, 0.68, 0.62), 0.03), ((0.25, 0.27, 0.25), 0.025)]):
    P.box(f'boek{k}', (0.24, 0.17, hgt), (cx + 0.6, RD - 0.3, 0.75 + [0.015, 0.0425][k]), P.mat(f'boek{k}', c, rough=0.8), bevel=0.002)
# stoel
seat = P.mat('stoel', (0.18, 0.16, 0.14), rough=0.7)
P.rounded('zitting', (0.5, 0.48, 0.07), (cx - 0.05, RD - 1.25, 0.47), seat, radius=0.03)
P.rounded('rug', (0.48, 0.06, 0.42), (cx - 0.05, RD - 1.5, 0.82), seat, radius=0.03)
P.cyl('stoelpoot', 0.025, 0.4, (cx - 0.05, RD - 1.25, 0.24), black)
for k in range(5):
    a = k * 2 * math.pi / 5
    P.box(f'ster{k}', (0.3, 0.035, 0.03), (cx - 0.05 + math.cos(a) * 0.15, RD - 1.25 + math.sin(a) * 0.15, 0.06), black, rot=(0, 0, a), bevel=0.005)
P.level_camera((RW - 0.55, 0.0, 1.35), 20, lens=24, shift=(0, -0.03), dof=3.2, fstop=8)
P.render(out)
