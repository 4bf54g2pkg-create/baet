"""Korte video woonkamer: langzame zijwaartse camerabeweging (slider), 5 s.
Rendert N beelden (standaard 40 = 8 per seconde); daarna vloeiend gemaakt tot 24 fps met ffmpeg (zie maak-video.sh).
python3 video_woonkamer.py uitmap [breed hoog samples beelden]"""
import sys, os, runpy, math
here = __file__.rsplit('/', 1)[0]
sys.path.insert(0, here)
import pd_scene as P
import bpy

out = sys.argv[1]
W, H, S, N = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1280, 720, 32, 40)
os.makedirs(out, exist_ok=True)
# scène opbouwen zonder te renderen
P_render = P.render
P.render = lambda path: None
sys.argv = [sys.argv[0], '/dev/null', str(W), str(H), str(S)]
runpy.run_path(os.path.join(here, 'ruimte_woonkamer.py'), run_name='__main__')
P.render = P_render
s = bpy.context.scene
s.render.image_settings.file_format = 'PNG'
s.render.image_settings.color_depth = '8'
cam = s.camera
x0, y0, z0 = cam.location
for i in range(N):
    t = i / (N - 1)
    e = 0.5 - 0.5 * math.cos(math.pi * t)          # zacht beginnen en eindigen
    cam.location = (x0 - 0.45 * e, y0 + 0.18 * e, z0)
    cam.rotation_euler[2] = math.radians(10 - 4 * e)
    s.render.filepath = os.path.join(out, f'f{i:03d}.png')
    bpy.ops.render.render(write_still=True)
    print('beeld', i, flush=True)
