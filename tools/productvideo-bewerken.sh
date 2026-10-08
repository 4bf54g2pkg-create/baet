#!/usr/bin/env bash
# Puredeco · productvideo per decor bewerken (zelfde look voor elk decor).
# Gebruik: [STICKER=1] tools/productvideo-bewerken.sh <bron.MOV> <naam, bijv. 692-urban-smoke> [hoogte boven de 4:5-uitsnede als deel van het beeld, standaard 0.172]
#   STICKER=1 haalt de witte naamsticker van het showroomdisplay weg (tools/productvideo-sticker-weg.py).
# Uit: docs/productvideo/<naam>/<naam>-4x5.mp4 (1080×1350), -9x16.mp4 (1080×1920), -poster.jpg
# Stappen: HDR (iPhone HLG/PQ) → gewone kleuren · stabiliseren · vertraagd naar 24 fps (60 fps-opname → 0,4×) ·
#          neutrale kleurcorrectie (geen 'mooier maken': kleur moet het echte paneel benaderen) ·
#          naadloze lus met 1 s overvloeier · geen geluid · geen metadata (geen locatie/telefoon).
set -euo pipefail
SRC="$1"; NAME="$2"; CYF="${3:-0.172}"
OUT="$(cd "$(dirname "$0")/.." && pwd)/docs/productvideo/$NAME"; mkdir -p "$OUT"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

probe() { ffprobe -v error -select_streams v:0 -show_entries "stream=$1" -of csv=p=0 "$2" | head -1 | cut -d, -f1; }
TRC=$(probe color_transfer "$SRC")
if [[ "$TRC" == "arib-std-b67" || "$TRC" == "smpte2084" ]]; then
  TONE="zscale=tin=$TRC:min=bt2020nc:pin=bt2020:rin=tv:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:param=0.3:desat=0,zscale=t=bt709:m=bt709:r=tv,"
else
  TONE=""
fi
if [[ -n "$TONE" ]]; then echo "Bron: $TRC (HDR) → omgezet naar gewone kleur"; else echo "Bron: ${TRC:-onbekend} (geen HDR)"; fi
ffmpeg -v error -y -i "$SRC" -an -map_metadata -1 -vf "${TONE}format=yuv420p" -c:v libx264 -crf 8 -preset slow "$TMP/sdr.mp4"
ffmpeg -v error -y -i "$TMP/sdr.mp4" -vf "vidstabdetect=shakiness=6:accuracy=15:result=$TMP/tr.trf" -f null -
ffmpeg -v error -y -i "$TMP/sdr.mp4" -vf "vidstabtransform=input=$TMP/tr.trf:smoothing=40:optzoom=1:interpol=bicubic,unsharp=5:5:0.4" -c:v libx264 -crf 8 -preset slow "$TMP/stab.mp4"
if [[ "${STICKER:-0}" == "1" ]]; then
  python3 "$(dirname "$0")/productvideo-sticker-weg.py" "$TMP/stab.mp4" "$TMP/clean.mp4" && mv "$TMP/clean.mp4" "$TMP/stab.mp4"
fi

# Lengte na vertragen; lus = alles vanaf 1 s, laatste seconde vloeit over in het begin.
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$TMP/stab.mp4")
# Vertraging volgt de opname: 60 fps → 0,4× (2,5), 30 fps → 0,8× (1,25); altijd 24 fps uit.
FPS=$(probe r_frame_rate "$TMP/stab.mp4")
SLOW=$(python3 -c "f=$FPS; print(round(min(2.5,max(1.0,f/23.976)),3))")
OFF=$(python3 -c "print(round($DUR*$SLOW-2,3))")
G="curves=master='0/0 0.3/0.21 0.6/0.48 0.85/0.76 1/0.95',colorbalance=rs=-0.02:bs=0.015:rm=-0.04:bm=0.03:rh=-0.01:bh=0.01,eq=contrast=1.05:saturation=0.92"
mk() {
  ffmpeg -v error -y -i "$TMP/stab.mp4" -filter_complex \
    "[0:v]setpts=$SLOW*PTS,fps=24000/1001,$1,$G,split[a][b];[a]trim=start=1,setpts=PTS-STARTPTS[A];[b]trim=0:1,setpts=PTS-STARTPTS[B];[A][B]xfade=transition=fade:duration=1:offset=$OFF,format=yuv420p[v]" \
    -map "[v]" -an -map_metadata -1 -c:v libx264 -crf 21 -preset slow -profile:v high \
    -color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart "$2"
}
W=$(probe width "$TMP/stab.mp4")
H=$(probe height "$TMP/stab.mp4")
CY=$(python3 -c "print(int($H*$CYF)//2*2)")
mk "crop=$W:$((W*5/4/2*2)):0:$CY,scale=1080:1350" "$OUT/$NAME-4x5.mp4"
mk "scale=1080:1920" "$OUT/$NAME-9x16.mp4"
ffmpeg -v error -y -i "$OUT/$NAME-4x5.mp4" -frames:v 1 -q:v 3 "$OUT/$NAME-poster.jpg"
ls -la "$OUT"
