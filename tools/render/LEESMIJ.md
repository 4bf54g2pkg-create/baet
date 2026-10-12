# Visualisaties (renders) voor Puredeco

Fotorealistische visualisaties per ruimte, gemaakt met Blender 4.2 (bpy, Cycles op CPU) in de cloudomgeving.

**Waarom het klopt**
- Het decor is de echte packshot-scan van het product (`textuur-uit-packshot.py` knipt het paneel uit de productfoto), 1:1 over het hele paneel.
- Panelen zijn op maat: 122 cm breed, 260 of 280 cm hoog. Linea (5 mm) met zichtbare naad, Signature (8 mm) met vrijwel onzichtbare naad, zoals per decor in de winkel.
- Op de site staat bij elke visualisatie het label **Visualisatie**. Het zijn geen foto's van projecten.

**Bestanden**
- `pd_scene.py`: bouwstenen (kamer met raam en zon, panelenwand, eikenvloer, materialen, camera).
- `ruimte_<ruimte>.py`: één scène per ruimte (badkamer 851, toilet 666, keuken 670, woonkamer 811, slaapkamer 646, kantoor 619 + akupanelen).
- `render-alle.sh`: alles renderen (1800 × 1200, 128 samples, ± 15 min per beeld op 4 kernen) + `nabewerking.py` (vignet, korrel, verscherping).
- `video_woonkamer.py` + `maak-video.sh`: korte camerabeweging (40 beelden, 8 fps → 24 fps met bewegingsinterpolatie).

**Nieuw decor of nieuwe ruimte**
1. Packshot downloaden en `python3 textuur-uit-packshot.py raw.jpg /tmp/claude-0/r/tex/p<code>.jpg`.
2. Code toevoegen aan `DECOR` in `pd_scene.py` (ruwheid, glans, structuur).
3. In een `ruimte_*.py` de code in `panel_wall(...)` aanpassen en renderen.

Installatie: `pip download bpy==4.2.0 --no-deps` en `pip install` het wiel (Python 3.11).
