#!/bin/bash
# Beelden (8 fps) → vloeiende 24 fps-video (bewegingsinterpolatie), H.264 + poster. Gebruik: maak-video.sh beeldenmap uit-zonder-extensie
IN=$1; OUT=$2
ffmpeg -y -loglevel error -framerate 8 -i "$IN/f%03d.png" \
  -vf "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,format=yuv420p" \
  -c:v libx264 -preset slow -crf 22 -profile:v high -movflags +faststart -an "$OUT.mp4"
cp "$IN/f000.png" "$OUT-poster.png"
ls -la "$OUT.mp4"
