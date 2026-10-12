"""Nabewerking zoals een camera: lichte vignettering, fijne korrel, subtiele verscherping. Gebruik: nabewerking.py in.png uit.jpg"""
import sys
import numpy as np
from PIL import Image, ImageFilter

im = Image.open(sys.argv[1]).convert('RGB')
im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=35, threshold=2))
a = np.asarray(im).astype(np.float32) / 255
h, w = a.shape[:2]
y, x = np.mgrid[0:h, 0:w]
r = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2) / np.sqrt(2)
a *= (1 - 0.16 * r ** 2.2)[..., None]
rng = np.random.default_rng(5)
g = rng.normal(0, 0.011, (h, w, 1)).astype(np.float32)
a = np.clip(a + g * (0.6 + 0.4 * (1 - a.mean(axis=2, keepdims=True))), 0, 1)
Image.fromarray((a * 255 + 0.5).astype(np.uint8)).save(sys.argv[2], quality=90, optimize=True, progressive=True)
print('ok', sys.argv[2])
