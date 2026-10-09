#!/usr/bin/env python3
"""Puredeco · lijntekeningen per ruimte (wandaanzicht met paneelnaden om de 122 cm).

Eén vaste stijl: inkt-lijn 1.2, naden in brons (gestippeld), wand licht getint met de kleur van een echt decor.
Gebruik: python3 tools/inspiratie-tekeningen.py <uitmap>  →  badkamer.svg, toilet.svg, keuken.svg, woonkamer.svg, slaapkamer.svg, werkplek.svg
Schaal: 1 eenheid = 1 cm. Wand 488 breed (4 panelen) × 280 hoog; vloer op y=300.
"""
import os, sys

INK = '#151413'
SEAM = '#8C6A4A'
W, H, X0, Y0 = 488, 280, 36, 20          # wand
FLOOR = Y0 + H


TEX = {}   # naam → url van de decorscan (optioneel); wordt de wand, licht gedempt


def wall(tint, panels=4, seam=True, name=None):
    s = [f'<rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="{tint}" stroke="none"/>']
    if name and TEX.get(name):
        s.append(f'<defs><pattern id="tx-{name}" patternUnits="userSpaceOnUse" x="{X0}" y="{Y0}" width="{W}" height="{H}">'
                 f'<image href="{TEX[name]}" width="{W}" height="{W}" y="{(H - W) / 2}" preserveAspectRatio="xMidYMid slice"/></pattern></defs>'
                 f'<rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="url(#tx-{name})" stroke="none" opacity=".72"/>')
    if seam:
        for i in range(1, panels):
            x = X0 + i * 122
            s.append(f'<line x1="{x}" y1="{Y0}" x2="{x}" y2="{FLOOR}" stroke="{SEAM}" stroke-width="1" stroke-dasharray="3 4" fill="none"/>')
    s.append(f'<rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="none" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<line x1="{X0 - 30}" y1="{FLOOR}" x2="{X0 + W + 30}" y2="{FLOOR}" stroke="{INK}" stroke-width="1.6"/>')
    # maatlijnen: hoogte 280 links, paneelbreedte 122 onder
    s.append(f'<g stroke="{INK}" stroke-width=".8" fill="{INK}" font-family="Instrument Sans,Arial" font-size="10">'
             f'<line x1="{X0 - 16}" y1="{Y0}" x2="{X0 - 16}" y2="{FLOOR}"/><line x1="{X0 - 20}" y1="{Y0}" x2="{X0 - 12}" y2="{Y0}"/>'
             f'<line x1="{X0 - 20}" y1="{FLOOR}" x2="{X0 - 12}" y2="{FLOOR}"/>'
             f'<text x="{X0 - 22}" y="{Y0 + H / 2}" transform="rotate(-90 {X0 - 22} {Y0 + H / 2})" text-anchor="middle" stroke="none">280 cm</text>'
             f'<line x1="{X0}" y1="{FLOOR + 14}" x2="{X0 + 122}" y2="{FLOOR + 14}"/><line x1="{X0}" y1="{FLOOR + 10}" x2="{X0}" y2="{FLOOR + 18}"/>'
             f'<line x1="{X0 + 122}" y1="{FLOOR + 10}" x2="{X0 + 122}" y2="{FLOOR + 18}"/>'
             f'<text x="{X0 + 61}" y="{FLOOR + 28}" text-anchor="middle" stroke="none">122 cm</text></g>')
    return s


def svg(body, label):
    # meubels gevuld met papierkleur, zodat ze leesbaar boven het materiaal liggen
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 560 340" role="img" aria-label="{label}">'
            f'<g fill="#F5F2EC" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">'
            + ''.join(body) + '</g></svg>')


def badkamer():
    b = wall('#EDEAE6', name='badkamer')
    b += ['<rect x="380" y="20" width="144" height="280" fill="#F5F2EC" fill-opacity=".28"/>', '<line x1="380" y1="40" x2="524" y2="40"/>',   # douchewand + rail
          '<path d="M452 40v26"/>', '<rect x="436" y="66" width="32" height="5" rx="2"/>',               # regendouche
          '<path d="M78 196h190v36H78z"/>', '<path d="M90 206h166"/>', '<path d="M146 186h56l-6 10h-44z"/>',  # meubel + kom
          '<path d="M172 186v-14h10"/>', '<circle cx="174" cy="120" r="38"/>']                           # kraan + spiegel
    return svg(b, 'Badkamerwand met wandpanelen, wastafel en douche')


def toilet():
    b = wall('#E9E6E1', name='toilet')
    b += ['<path d="M206 214h68c0 22-14 34-34 34h-6c-16 0-28-12-28-34z"/>', '<path d="M216 214v-10h48v10"/>',  # hangtoilet
          '<rect x="228" y="148" width="24" height="16" rx="2"/>',                                          # bedieningsplaat
          '<path d="M372 176h70v10c0 12-10 20-22 20h-26c-12 0-22-8-22-20z"/>', '<path d="M407 176v-14h8"/>',   # fonteintje
          '<rect x="396" y="96" width="34" height="46" rx="3"/>']
    return svg(b, 'Toiletwand met wandpanelen, hangtoilet en fonteintje')


def keuken():
    b = wall('#EFEBE4', name='keuken')
    b += ['<rect x="36" y="214" width="488" height="86"/>', '<path d="M36 220h488" fill="none"/>',          # werkblad + kasten
          '<path d="M158 220v80M280 220v80M402 220v80" fill="none"/>',
          '<path d="M96 252h4M218 252h4M340 252h4M462 252h4"/>',
          '<path d="M300 20v54"/>', '<path d="M240 74h120l16 26H224z"/>',                                             # afzuigkap
          '<path d="M96 214v-22h40v22"/>', '<path d="M108 192v-10h16v10"/>']                              # pot
    return svg(b, 'Keukenwand met wandpanelen boven het werkblad')


def woonkamer():
    b = wall('#E8E2DA', name='woonkamer')
    b += ['<rect x="178" y="92" width="204" height="116" rx="2" fill="#2B2927"/>',                       # tv
          '<path d="M150 252h260v34H150z"/>', '<path d="M150 286v14M410 286v14"/>',                       # tv-meubel
          '<path d="M60 236h70v64H60z"/>', '<path d="M60 236c0-26 70-26 70 0"/>',                         # fauteuil
          '<path d="M462 300v-74"/>', '<path d="M448 226h28l-6-22h-16z"/>']                               # staande lamp
    return svg(b, 'Woonkamerwand met wandpanelen achter tv en meubel')


def slaapkamer():
    b = wall('#E6E2DD', name='slaapkamer')
    b += ['<path d="M140 196h280v44H140z"/>', '<path d="M126 240h308v32H126z"/>', '<path d="M126 272v28M434 272v28"/>',  # bed
          '<path d="M166 196c0-18 40-18 40 0M354 196c0-18 40-18 40 0"/>',                                  # kussens
          '<rect x="70" y="240" width="44" height="40"/>', '<rect x="446" y="240" width="44" height="40"/>',
          '<path d="M92 20v124M468 20v124" fill="none"/>', '<path d="M82 144h20l-4 14h-12zM458 144h20l-4 14h-12z"/>']   # hanglampen
    return svg(b, 'Slaapkamerwand met wandpanelen achter het bed')


def werkplek():
    b = wall('#E7E4DE', name='werkplek')
    for i in range(12):                                                                                  # akupaneel-lamellen
        x = 54 + i * 7
        b.append(f'<line x1="{x}" y1="20" x2="{x}" y2="300" stroke-width="2.2"/>')
    b += ['<rect x="216" y="202" width="228" height="6"/>', '<path d="M226 208v92M434 208v92" fill="none"/>',  # bureau
          '<rect x="296" y="148" width="72" height="48" rx="2"/>', '<path d="M332 196v10"/>',             # scherm
          '<path d="M256 300l8-48h40l8 48M262 252v-40h44v40"/>']                                          # stoel
    return svg(b, 'Werkplek met wandpanelen en akupanelen')


ROOMS = dict(badkamer=badkamer, toilet=toilet, keuken=keuken, woonkamer=woonkamer, slaapkamer=slaapkamer, werkplek=werkplek)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    # optioneel: naam=url paren, bv. badkamer=../stalen/travertin-851.jpg
    for a in sys.argv[2:]:
        k, v = a.split('=', 1); TEX[k] = v
    os.makedirs(out, exist_ok=True)
    for name, fn in ROOMS.items():
        with open(os.path.join(out, name + '.svg'), 'w') as f:
            f.write(fn())
    print('ok', list(ROOMS))
