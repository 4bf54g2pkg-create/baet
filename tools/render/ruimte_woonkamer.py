"""Visualisatie woonkamer: tv-wand in 811 Walnut Classic (Signature, 8 mm), laag dressoir, bank."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import pd_scene as P

out = sys.argv[1]
W, H, S = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1800, 1200, 160)
P.reset(S, (W, H))
RW, RD, RH = 4 * P.PANEL_W, 4.6, 2.6
P.room_shell(RW, RD, RH, P.stuc((0.86, 0.84, 0.80)), P.mat('x', (0.3, 0.3, 0.3)),
             win=(1.4, 3.9, 0.05, 2.45), sun_dir=(1.0, 0.75, -0.38), sun_energy=6.5, day=150, fill=30)
P.oak_floor(-0.2, RW + 0.2, -1.6, RD, tint=(1.0, 0.96, 0.92))
P.panel_wall('811', 0, RD, 0, 4, h=RH, thick=0.008, joint=0.00025)
greige = P.mat('dressoir', (0.62, 0.58, 0.52), rough=0.6)
black = P.mat('zwart-mat', (0.02, 0.02, 0.02), rough=0.4, metal=0.5)
cx = RW / 2
P.box('dressoir', (2.4, 0.42, 0.42), (cx, RD - 0.008 - 0.21, 0.42), greige, bevel=0.004)
for i in range(1, 4):
    P.box(f'dr-naad{i}', (0.002, 0.425, 0.40), (cx - 1.2 + i * 0.6, RD - 0.008 - 0.21, 0.42), P.mat('naad', (0.05, 0.05, 0.05), rough=0.8))
tv = P.box('tv', (1.45, 0.03, 0.83), (cx, RD - 0.008 - 0.03, 1.4), P.mat('tv', (0.01, 0.01, 0.012), rough=0.06, coat=0.0), bevel=0.003)
P.box('tv-rand', (1.452, 0.026, 0.832), (cx, RD - 0.008 - 0.025, 1.4), black, bevel=0.002)
cer = P.mat('aardewerk', (0.85, 0.82, 0.76), rough=0.5)
P.rounded('vaas1', (0.16, 0.16, 0.34), (cx + 0.85, RD - 0.2, 0.8), P.mat('aardewerk2', (0.35, 0.3, 0.26), rough=0.55), radius=0.07)
for k, (c, hgt) in enumerate([((0.7, 0.66, 0.6), 0.03), ((0.25, 0.27, 0.25), 0.025), ((0.8, 0.78, 0.74), 0.035)]):
    P.box(f'boek{k}', (0.28, 0.2, hgt), (cx - 0.8, RD - 0.2, 0.63 + sum([0.03, 0.025, 0.035][:k]) + hgt / 2), P.mat(f'boek{k}', c, rough=0.8), bevel=0.002)
P.sphere('bal', 0.06, (cx - 0.8, RD - 0.2, 0.78), cer)
# bank in de voorgrond (bouclé)
bou = P.mat('boucle', (0.80, 0.77, 0.71), rough=1.0)
nt = bou.node_tree; b = nt.nodes['Principled BSDF']; b.inputs['Sheen Weight'].default_value = 0.8
v = nt.nodes.new('ShaderNodeTexVoronoi'); v.inputs['Scale'].default_value = 700
bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.6
nt.links.new(v.outputs['Distance'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], b.inputs['Normal'])
# fauteuil links, schuin naar de wand
P.rounded('fauteuil-zit', (0.8, 0.8, 0.4), (1.25, 2.3, 0.2), bou, radius=0.12)
P.rounded('fauteuil-rug', (0.8, 0.2, 0.42), (1.25, 1.95, 0.55), bou, radius=0.09)
P.rounded('fauteuil-kussen', (0.66, 0.6, 0.12), (1.25, 2.38, 0.44), bou, radius=0.05)
# salontafel rond, travertin-achtig (geen productclaim)
tab = P.img_mat('tafel-noot', f'{P.TEX}/p810.jpg', rough=0.35, bump=0.15, scale=(0.5, 0.5), tint=(1.25, 1.2, 1.15))
P.cyl('tafel', 0.42, 0.34, (cx + 0.2, 2.45, 0.17), tab, verts=96, bevel=0.01)
P.rounded('tafel-boek', (0.26, 0.2, 0.035), (cx + 0.12, 2.42, 0.358), P.mat('boek-t', (0.74, 0.70, 0.64), rough=0.8), radius=0.004, levels=1)
P.sphere('tafel-schaal', 0.09, (cx + 0.38, 2.55, 0.37), cer, scale=(1, 1, 0.35))
# vloerkleed
rug = P.mat('kleed', (0.55, 0.50, 0.44), rough=1.0)
rn = rug.node_tree; rb = rn.nodes['Principled BSDF']; rb.inputs['Sheen Weight'].default_value = 1.0
rv = rn.nodes.new('ShaderNodeTexNoise'); rv.inputs['Scale'].default_value = 1500; rv.inputs['Detail'].default_value = 2
rbp = rn.nodes.new('ShaderNodeBump'); rbp.inputs['Strength'].default_value = 0.8
rn.links.new(rv.outputs['Fac'], rbp.inputs['Height']); rn.links.new(rbp.outputs['Normal'], rb.inputs['Normal'])
P.box('kleed', (2.8, 2.0, 0.012), (cx, 2.4, 0.018), rug, bevel=0.004)
P.level_camera((RW - 1.1, -0.2, 1.3), 10, lens=24, shift=(0.0, -0.02), dof=5.4, fstop=8)
P.render(out)
