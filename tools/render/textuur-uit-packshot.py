"""Snijdt het paneel uit een packshot (wit/lichte achtergrond) en schaalt het naar 122 x 280 verhouding.
Gebruik: python3 textuur-uit-packshot.py in.jpg uit.jpg"""
import sys
import numpy as np
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(int)
# achtergrond = bijna wit of zeer licht grijs zonder kleur
bg = (a.min(axis=2) > 236) & ((a.max(axis=2) - a.min(axis=2)) < 10)
rows = np.where((~bg).mean(axis=1) > 0.25)[0]
cols = np.where((~bg).mean(axis=0) > 0.25)[0]
if len(rows) < 50 or len(cols) < 50:
    box = (0, 0, im.width, im.height)
else:
    y0, y1, x0, x1 = rows[0], rows[-1], cols[0], cols[-1]
    ix, iy = int((x1 - x0) * 0.02) + 3, int((y1 - y0) * 0.015) + 3  # rand en schaduw eraf
    box = (x0 + ix, y0 + iy, x1 - ix, y1 - iy)
c = im.crop(box)
H = max(1600, c.height)
W = round(H * 122 / 280)
c.resize((W, H), Image.LANCZOS).save(dst, quality=94)
print(src, '->', box, c.size, '->', (W, H))
