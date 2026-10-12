"""Visualisatie keuken: 670 Pandora Slate glans (Linea, 5 mm) als volledige keukenwand, onderkasten met spoelbak.
Geen kookplaat tegen de wand (geen claim over hitte)."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 3 * P.PANEL_W, 3.6, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.85, 0.84, 0.81)), P.mat('vloer-tegel', (0.3, 0.29, 0.27), rough=0.6),
             win=(1.4, 3.0, 0.9, 2.3), sun_dir=(1.0, 0.9, -0.5), sun_energy=6.5, day=150, fill=30)
P.oak_floor(-0.2, RW + 0.2, -1.6, RD, tint=(0.95, 0.9, 0.84))
P.panel_wall('670', 0, RD, 0, 3, h=RH, thick=0.005, joint=0.0012)
front = P.mat('front-groen', (0.10, 0.13, 0.11), rough=0.55)
oak = P.img_mat('meubel-eik', f'{P.TEX}/p607.jpg', rough=0.45, bump=0.2, tint=(0.92, 0.86, 0.78))
black = P.mat('zwart-mat', (0.025, 0.025, 0.025), rough=0.38, metal=0.7)
x0, x1 = 0.25, RW - 0.25
L = x1 - x0
d = 0.62
P.box('plint', (L, d - 0.06, 0.1), ((x0 + x1) / 2, RD - 0.005 - (d - 0.06) / 2 - 0.02, 0.05), P.mat('plint', (0.03, 0.03, 0.03), rough=0.7))
n = 5
for i in range(n):
    w = L / n
    P.box(f'front{i}', (w - 0.003, 0.02, 0.78), (x0 + w * i + w / 2, RD - 0.005 - d + 0.01, 0.1 + 0.39), front, bevel=0.0015)
P.box('kast', (L, d - 0.02, 0.78), ((x0 + x1) / 2, RD - 0.005 - (d - 0.02) / 2, 0.49), front)
P.box('greeplijst', (L, 0.025, 0.03), ((x0 + x1) / 2, RD - 0.005 - d + 0.02, 0.86), P.mat('groef', (0.02, 0.02, 0.02), rough=0.8))
top = P.box('blad', (L + 0.02, d + 0.02, 0.03), ((x0 + x1) / 2, RD - 0.005 - (d + 0.02) / 2, 0.905), oak, bevel=0.002)
# spoelbak (onderbouw) + kraan
sx = x0 + L * 0.68
P.box('spoelbak', (0.5, 0.4, 0.004), (sx, RD - 0.33, 0.921), P.mat('rvs-donker', (0.08, 0.08, 0.08), rough=0.3, metal=1.0))
P.cyl('kraan-voet', 0.022, 0.06, (sx, RD - 0.07, 0.95), black)
P.cyl('kraan', 0.012, 0.36, (sx, RD - 0.07, 1.13), black)
P.cyl('kraan-uitloop', 0.011, 0.22, (sx, RD - 0.17, 1.30), black, rot=(math.radians(90), 0, 0))
# zwevende plank met objecten
P.box('plank', (1.3, 0.24, 0.035), (x0 + 0.85, RD - 0.005 - 0.12, 1.55), oak, bevel=0.002)
cer = P.mat('aardewerk', (0.85, 0.82, 0.76), rough=0.5)
P.cyl('pot1', 0.06, 0.16, (x0 + 0.4, RD - 0.12, 1.648), cer)
P.cyl('pot2', 0.045, 0.11, (x0 + 0.55, RD - 0.12, 1.623), P.mat('aardewerk2', (0.35, 0.3, 0.26), rough=0.55))
for k in range(4):
    P.cyl(f'bord{k}', 0.13, 0.014, (x0 + 1.2, RD - 0.13, 1.575 + k * 0.016), cer, bevel=0.004)
# snijplank en schaal op het blad
P.box('snijplank', (0.42, 0.012, 0.3), (x0 + 0.5, RD - 0.03, 1.07), oak, bevel=0.004, rot=(math.radians(-6), 0, 0))
bowl = P.sphere('schaal', 0.14, (x0 + 1.15, RD - 0.3, 0.97), cer, scale=(1, 1, 0.38))
for k, (dx, dy) in enumerate([(-0.04, 0.0), (0.04, 0.02), (0.0, -0.04)]):
    P.sphere(f'citroen{k}', 0.036, (x0 + 1.15 + dx, RD - 0.3 + dy, 1.0), P.mat('citroen', (0.85, 0.65, 0.12), rough=0.45))
# twee hanglampen
for k, lx in enumerate([RW / 2 - 0.6, RW / 2 + 0.6]):
    P.cyl(f'snoer{k}', 0.002, 0.9, (lx, RD - 0.9, RH - 0.45), black, verts=8)
    shade = P.cyl(f'kap{k}', 0.12, 0.22, (lx, RD - 0.9, RH - 0.98), P.mat('kap', (0.04, 0.04, 0.04), rough=0.5, metal=0.5), verts=64)
    P.sphere(f'bol{k}', 0.05, (lx, RD - 0.9, RH - 1.08), P.mat('gloei', (1, 1, 1), emit=(1, 0.8, 0.55), emit_strength=25))
P.level_camera((RW - 0.6, 0.2, 1.35), 14, lens=24, shift=(0, -0.02), dof=3.4, fstop=8)
P.render(out)
