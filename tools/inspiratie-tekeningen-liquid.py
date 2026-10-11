#!/usr/bin/env python3
"""Zet de lijntekeningen (tools/inspiratie-tekeningen.py) om naar snippets/pd-tekening.liquid voor het thema.
Gebruik in Liquid: {% render 'pd-tekening', room: 'badkamer', tex: url_van_decorscan, uid: section.id %}
"""
import importlib.util, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'tools', 'inspiratie-tekeningen.py'))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
out = ['{%- comment -%}',
       '  Puredeco · lijntekening van een wand per ruimte (op schaal: paneel 122 × 280 cm).',
       '  Gegenereerd door tools/inspiratie-tekeningen-liquid.py; niet met de hand aanpassen.',
       "  room: badkamer | toilet | keuken | woonkamer | slaapkamer | werkplek · tex: url van een decorscan (optioneel) · uid: uniek per pagina",
       '{%- endcomment -%}',
       '{%- case room -%}']
for name, fn in t.ROOMS.items():
    t.TEX.clear(); t.TEX[name] = '__TEX__'
    with_tex = fn().replace(f'tx-{name}', f'tx-{name}-__UID__')
    t.TEX.clear()
    without = fn()
    lq = lambda s: s.replace('__TEX__', '{{ tex }}').replace('__UID__', '{{ uid }}')
    out.append(f"{{%- when '{name}' -%}}{{%- if tex != blank -%}}{lq(with_tex)}{{%- else -%}}{without}{{%- endif -%}}")
out.append('{%- endcase -%}')
open(os.path.join(ROOT, 'theme-h1', 'snippets', 'pd-tekening.liquid'), 'w').write('\n'.join(out) + '\n')
print('ok')
