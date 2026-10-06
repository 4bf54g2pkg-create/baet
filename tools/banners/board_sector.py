# Artboard "Sectorbeelden": aangeleverde sectorfoto's met een Puredeco-decor op de wand (visualisaties).
import json, subprocess
C = '/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/canvas/project/'
M = '/home/user/baet/media/sector/'
for f in ['hotel-bron', 'hotel-678', 'hotel-811', 'hotel-810led']:
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', M + f + '.jpg', '-vf', 'scale=1400:-2', '-q:v', '3', C + 'beeld/sector-' + f + '.jpg'], check=True)


def card(f, title, sub, tag):
    return ('<div><div style="position:relative"><img src="./beeld/sector-' + f + '.jpg">' +
            ('<span style="position:absolute;right:12px;top:12px;background:rgba(245,242,236,.92);font-size:11px;padding:5px 9px;color:#6E675E">' + tag + '</span>' if tag else '') +
            '</div><div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:12px"><span class="s" style="font-size:30px">' + title +
            '</span><span style="font-size:12px;color:#6E675E">' + sub + '</span></div></div>')


body = ('<div class="tag" style="left:24px;top:20px">Sectorbeelden · test hotel · aangeleverde foto + Puredeco-decor</div>'
        '<div style="padding:90px 96px 80px">'
        '<div class="s" style="font-size:64px;line-height:1">Hotels: jullie wand in een echte hotelkamer</div>'
        '<div style="font-size:16px;line-height:1.7;color:#3A3733;margin-top:14px;max-width:1080px">De wand achter het bed is vervangen door het echte oppervlak van het decor, '
        'in perspectief en op ware grootte (panelen van 122 cm breed, gemeten aan het bed). Licht, kleur van het daglicht, hanglampen en hoofdbord komen uit de foto zelf. '
        'Het kunstwerk aan de wand is weggelaten. Twee panelen (244 cm) staan symmetrisch achter het hoofdbord; aan beide uiteinden zit een LED-lijn die over het hout en de wand ernaast strijkt. Op de site staat bij dit beeld altijd “Visualisatie”, want het is een bewerkte foto en geen geplaatst project.</div>'
        '<div style="margin-top:48px">' + card('hotel-810led', '810 Noir Oak met LED', '2 panelen achter het hoofdbord · LED aan beide uiteinden', 'Visualisatie') + '</div>'
        '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px;margin-top:48px">' +
        card('hotel-678', '678 marmer', 'eerdere variant', 'Visualisatie') +
        card('hotel-811', '811 hout', 'eerdere variant', 'Visualisatie') +
        card('hotel-bron', 'Origineel', 'aangeleverde foto', '') +
        '</div>'
        '<div style="margin-top:56px;max-width:1000px;font-size:15px;line-height:1.7;color:#3A3733">'
        '<div class="k">Voor dit live gaat</div>'
        '<div style="margin-top:10px">1. <b>Bron en licentie:</b> stuur de link naar de foto (Unsplash/Pexels of de fotograaf). Zonder bron zetten we hem niet live.</div>'
        '<div style="margin-top:6px">2. <b>LED:</b> nieuw in het assortiment. Zodra de LED-productpagina er is, linken we vanaf dit beeld naar de LED en noemen we hem in het bijschrift.</div>'
        '<div style="margin-top:6px">3. De tweede aangeleverde foto heeft een signatuur “k/r” op het hoofdbord. Die gebruiken we niet zonder toestemming van de maker.</div>'
        '<div style="margin-top:6px">4. Daarna volgen horeca, kantoren en retail op dezelfde manier.</div></div>'
        '</div>')

page = ('<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n<title>Sectorbeelden</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;1,500&amp;family=Instrument+Sans:wght@400;500;600&amp;display=swap">\n'
        '<style>\nbody{margin:0}\n.s{font-family:\'Cormorant\',Georgia,serif;font-weight:500}\n'
        '.k{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A}\nimg{display:block;width:100%}\n'
        '.tag{position:absolute;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:#E9E3D8;color:#6E675E;padding:4px 8px;z-index:3}\n</style>\n</helmet>\n'
        '<div style="width:1440px;height:1860px;position:relative;overflow:hidden;background:#F5F2EC;color:#151413;font-family:\'Instrument Sans\',\'Helvetica Neue\',Arial,sans-serif">\n'
        + body +
        '\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1440,"height":1860}}\'>\n'
        'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')
open(C + 'Sectorbeelden.dc.html', 'w').write(page)
d = json.load(open(C + 'canvas.json'))
d['boards']['Sectorbeelden.dc.html'] = {'h': 1860, 'title': 'Sectorbeelden · hotel (test)', 'w': 1440, 'x': 3040, 'y': 13820}
if 'Sectorbeelden.dc.html' not in d['order']:
    d['order'].append('Sectorbeelden.dc.html')
json.dump(d, open(C + 'canvas.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
