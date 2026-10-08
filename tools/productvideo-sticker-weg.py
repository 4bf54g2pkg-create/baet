#!/usr/bin/env python3
"""Puredeco · naamsticker van het showroomdisplay uit een productvideo halen.

Gebruik: productvideo-sticker-weg.py <in.mp4> <uit.mp4> [controle.jpg]
Zoekt per beeld het witte, liggende rechthoekje (rechterhelft van het paneel), maakt het spoor
glad en vult de plek met het paneel zelf, direct eronder (seamless clone). Omdat die bron met
het paneel meebeweegt, blijft het rustig tussen de beelden. Niets anders in het beeld verandert.
"""
import json, subprocess, sys
import cv2, numpy as np

src, dst = sys.argv[1], sys.argv[2]
check = sys.argv[3] if len(sys.argv) > 3 else None

# Lezen en schrijven via ffmpeg met vaste BT.709 / tv-range, zodat kleur en helderheid exact gelijk blijven.
info = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                                'stream=width,height,r_frame_rate', '-of', 'csv=p=0', src]).decode().strip().split(',')
W, H, fps = int(info[0]), int(info[1]), info[2]
raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', src, '-vf',
                               'scale=in_color_matrix=bt709:in_range=tv:flags=accurate_rnd+full_chroma_int+bitexact,format=bgr24',
                               '-f', 'rawvideo', '-'])
frames = list(np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).copy())

# 1 · zoeken
boxes = []
for f in frames:
    m = (f.min(2) > 185).astype(np.uint8)
    m[:, :int(W * 0.5)] = 0; m[:int(H * 0.1)] = 0; m[int(H * 0.7):] = 0
    n, _, st, _ = cv2.connectedComponentsWithStats(m)
    best = None
    for k in range(1, n):
        x, y, w, h, a = st[k]
        if 15 <= w <= 0.12 * W and 3 <= h <= 0.025 * H and w / h > 2.5 and a > 0.6 * w * h:
            if best is None or a > best[4]:
                best = (x, y, w, h, a)
    boxes.append(best)
found = [i for i, b in enumerate(boxes) if b is not None]
if len(found) < len(frames) * 0.6:
    sys.exit(f'Sticker niet betrouwbaar gevonden ({len(found)}/{len(frames)} beelden); niets aangepast.')

# 2 · spoor: echte positie per beeld, ontbrekende beelden ingevuld, licht gemiddeld (5 beelden)
t = np.array(found, float)
cols = np.array([boxes[i][:4] for i in found], float)
idx = np.arange(len(frames))
fit = []
for c in range(4):
    v = np.interp(idx, t, cols[:, c])
    k = np.ones(5) / 5
    fit.append(np.convolve(np.pad(v, 2, mode='edge'), k, mode='valid'))

# 3 · vullen
pad = max(8, int(W * 0.009))
proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                         '-r', fps, '-i', '-', '-vf', 'scale=out_color_matrix=bt709:in_range=pc:out_range=tv:flags=accurate_rnd+full_chroma_int+bitexact,format=yuv420p',
                         '-c:v', 'libx264', '-crf', '8', '-preset', 'slow', '-color_primaries', 'bt709',
                         '-color_trc', 'bt709', '-colorspace', 'bt709', '-color_range', 'tv', dst], stdin=subprocess.PIPE)
log = []
for i, f in enumerate(frames):
    x, y, w, h = [int(round(v)) for v in (fit[0][i], fit[1][i], fit[2][i], fit[3][i])]
    x0, y0, x1, y1 = x - pad, y - pad, x + w + pad, y + h + pad
    bw, bh = x1 - x0, y1 - y0
    dy = bh + 4                                     # bron: paneel direct onder de sticker
    patch = f[y0 + dy:y1 + dy, x0:x1].copy()
    mask = np.full((bh, bw), 255, np.uint8)
    centre = (x0 + bw // 2, y0 + bh // 2)
    cl = cv2.seamlessClone(patch, f, mask, centre, cv2.NORMAL_CLONE)
    # zachte overgang: kern volledig vervangen, rand loopt in 4 px uit
    a = np.zeros((H, W), np.float32)
    a[y0 + 2:y1 - 2, x0 + 2:x1 - 2] = 1
    a = cv2.GaussianBlur(a, (0, 0), 2)[..., None]
    a[y - 2:y + h + 2, x - 2:x + w + 2] = 1
    out = (cl * a + f * (1 - a)).astype(np.uint8)
    proc.stdin.write(out.tobytes())
    log.append((x0, y0, bw, bh))
    if check and i == len(frames) // 2:
        a = f[y0 - 60:y1 + 60, x0 - 80:x1 + 80]; b = out[y0 - 60:y1 + 60, x0 - 80:x1 + 80]
        cv2.imwrite(check, cv2.resize(np.hstack([a, np.full((a.shape[0], 8, 3), 255, np.uint8), b]), None, fx=3, fy=3,
                                      interpolation=cv2.INTER_NEAREST))
proc.stdin.close(); proc.wait()
print(json.dumps({'beelden': len(frames), 'gevonden': len(found), 'eerste': log[0], 'laatste': log[-1]}))
