# Artboard "Hero-opties": drie richtingen voor de homepagebanner met 811 / 812.
import json, shutil, subprocess
C = '/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/canvas/project/'
B = '/home/user/baet/media/banners/'
for f in ['hero-a-licht', 'hero-a-licht-mobiel', 'hero-b-materiaal', 'hero-b-materiaal-mobiel', 'hero-c-sfeer', 'hero-c-sfeer-mobiel']:
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', B + f + '.jpg', '-vf', "scale='min(1600,iw)':-2", '-q:v', '3', C + 'beeld/' + f + '.jpg'], check=True)

HDR = ('<div style="height:34px;background:#151413;color:#D8D0C4;font-size:11px;display:flex;justify-content:center;gap:28px;align-items:center">'
       '<span>Gratis bezorgd in Nederland vanaf € 600</span><span>3 jaar garantie</span><span>Studio Herwen · op afspraak</span></div>'
       '<div style="height:72px;background:#F5F2EC;border-bottom:1px solid #DDD6CA;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:0 48px;font-size:14px">'
       '<div style="display:flex;gap:28px"><span>Collecties</span><span>Inspiratie</span><span>Projecten</span><span>Studio</span></div>'
       '<div style="font-size:22px"><b>Pure</b>Deco</div>'
       '<div style="display:flex;gap:20px;justify-content:flex-end;align-items:center"><span>Professionals</span><span style="border:1px solid #151413;padding:8px 14px">Samples</span><span>🛒</span></div></div>')
EYEBROW = 'Wandpanelen met bamboekern · voor wonen en projecten'
BTN_L = '<span style="white-space:nowrap;background:#F5F2EC;color:#151413;padding:14px 22px;font-size:14px">Ontdek de collecties</span><span style="border:1px solid #F5F2EC;color:#F5F2EC;padding:14px 22px;font-size:14px;white-space:nowrap">Voor projecten</span>'
BTN_D = '<span style="white-space:nowrap;background:#151413;color:#F5F2EC;padding:14px 22px;font-size:14px">Ontdek de collecties</span><span style="border:1px solid #151413;color:#151413;padding:14px 22px;font-size:14px;white-space:nowrap">Voor projecten</span>'


def k(t, c='#6E675E'):
    return f'<div style="font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:{c}">{t}</div>'


def h1(c, size=92):
    return f'<div class="s" style="font-size:{size}px;line-height:.95;color:{c};margin-top:18px">Eén wand.<br>Eén geheel.</div>'


def mob(img, inner):
    return (f'<div style="width:300px;height:620px;position:relative;overflow:hidden;border:1px solid #DDD6CA;background:#F5F2EC">'
            '<div style="height:48px;border-bottom:1px solid #DDD6CA;display:flex;align-items:center;justify-content:space-between;padding:0 14px;font-size:13px;background:#F5F2EC"><span>☰</span><span style="font-size:16px"><b>Pure</b>Deco</span><span>🛒</span></div>'
            + inner + '</div>')


# Optie A · Licht: papier links, 812-slaapkamer rechts
A_desk = ('<div style="position:relative;aspect-ratio:16/9;display:grid;grid-template-columns:47% 53%;background:#F5F2EC">'
          '<div style="display:flex;flex-direction:column;justify-content:center;padding:0 40px 0 48px">' + k(EYEBROW, '#8C6A4A') + h1('#151413', 60) +
          '<div style="font-size:15px;line-height:1.65;color:#3A3733;margin-top:22px;max-width:420px">Panelen van 280 cm met een kern van bamboe. Vloer tot plafond, rustig van ver, materiaal van dichtbij.</div>'
          '<div style="display:flex;gap:12px;margin-top:28px">' + BTN_D + '</div></div>'
          '<div style="position:relative"><img src="./beeld/hero-a-licht.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
          '<span style="position:absolute;left:16px;bottom:14px;background:rgba(245,242,236,.92);font-size:11px;padding:6px 10px">812 Walnut Deep · visualisatie</span></div></div>')
A_mob = mob('', '<img src="./beeld/hero-a-licht-mobiel.jpg" style="width:100%;height:300px;object-fit:cover;display:block">'
        '<div style="padding:22px 18px">' + k('Wandpanelen met bamboekern', '#8C6A4A') +
        '<div class="s" style="font-size:44px;line-height:.95;margin-top:10px">Eén wand.<br>Eén geheel.</div>'
        '<div style="margin-top:18px;background:#151413;color:#F5F2EC;text-align:center;padding:12px;font-size:13px">Ontdek de collecties</div>'
        '<div style="margin-top:8px;border:1px solid #151413;text-align:center;padding:12px;font-size:13px">Voor projecten</div></div>')

# Optie B · Materiaal: 811-oppervlak met kop, 811-interieur ernaast
B_desk = ('<div style="position:relative;aspect-ratio:2/1"><img src="./beeld/hero-b-materiaal.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
          '<div style="position:absolute;left:48px;top:90px;width:440px;color:#F5F2EC">' + k(EYEBROW, 'rgba(245,242,236,.85)') + h1('#F5F2EC', 70) +
          '<div style="display:flex;gap:12px;margin-top:30px">' + BTN_L + '</div></div>'
          '<span style="position:absolute;left:72px;bottom:22px;color:rgba(245,242,236,.85);font-size:11px">811 Walnut Classic · Signature · echte productfoto</span>'
          '<span style="position:absolute;right:16px;bottom:14px;background:rgba(245,242,236,.92);font-size:11px;padding:6px 10px">811 Walnut Classic · visualisatie</span></div>')
B_mob = mob('', '<div style="position:relative;height:572px"><img src="./beeld/hero-b-materiaal-mobiel.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
        '<div style="position:absolute;left:18px;right:18px;bottom:22px;color:#F5F2EC">' + k('811 Walnut Classic · Signature', 'rgba(245,242,236,.85)') +
        '<div class="s" style="font-size:46px;line-height:.95;margin-top:10px">Eén wand.<br>Eén geheel.</div>'
        '<div style="margin-top:18px;background:#F5F2EC;color:#151413;text-align:center;padding:12px;font-size:13px">Ontdek de collecties</div>'
        '<div style="margin-top:8px;border:1px solid #F5F2EC;text-align:center;padding:12px;font-size:13px">Voor projecten</div></div></div>')

# Optie C · Sfeer: 812-slaapkamer schermbreed
C_desk = ('<div style="position:relative;aspect-ratio:2/1"><img src="./beeld/hero-c-sfeer.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
          '<div style="position:absolute;left:44px;top:110px;width:360px;color:#F5F2EC">' + k('Wandpanelen met bamboekern', 'rgba(245,242,236,.85)') + h1('#F5F2EC', 64) +
          '<div style="display:flex;gap:12px;margin-top:30px">' + BTN_L + '</div></div>'
          '<span style="position:absolute;right:16px;bottom:14px;color:rgba(245,242,236,.85);font-size:11px">812 Walnut Deep · visualisatie</span></div>')
C_mob = mob('', '<div style="position:relative;height:572px"><img src="./beeld/hero-c-sfeer-mobiel.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
        '<div style="position:absolute;left:18px;right:18px;bottom:22px;color:#F5F2EC">' + k('Wandpanelen met bamboekern', 'rgba(245,242,236,.85)') +
        '<div class="s" style="font-size:46px;line-height:.95;margin-top:10px">Eén wand.<br>Eén geheel.</div>'
        '<div style="margin-top:18px;background:#F5F2EC;color:#151413;text-align:center;padding:12px;font-size:13px">Ontdek de collecties</div>'
        '<div style="margin-top:8px;border:1px solid #F5F2EC;text-align:center;padding:12px;font-size:13px">Voor projecten</div></div></div>')


def option(letter, name, decor, why, desk, mobile):
    return (f'<div style="margin-top:80px;display:flex;align-items:baseline;gap:18px"><span class="s" style="font-size:56px;color:#8C6A4A">{letter}</span>'
            f'<span class="s" style="font-size:44px">{name}</span><span style="font-size:13px;color:#6E675E">{decor}</span></div>'
            f'<div style="font-size:15px;line-height:1.6;color:#3A3733;margin-top:6px;max-width:1000px">{why}</div>'
            '<div style="display:grid;grid-template-columns:1fr 300px;gap:32px;margin-top:24px;align-items:start">'
            '<div style="border:1px solid #DDD6CA;overflow:hidden">' + HDR + desk + '</div>' + mobile + '</div>')


body = ('<div class="tag" style="left:24px;top:20px">Homepage-hero · drie richtingen · 811 Walnut Classic en 812 Walnut Deep</div>'
        '<div style="padding:90px 96px 80px">'
        '<div class="s" style="font-size:64px;line-height:1">Drie richtingen voor de hoofdbanner</div>'
        '<div style="font-size:16px;line-height:1.7;color:#3A3733;margin-top:14px;max-width:1040px">Alle drie met jullie eigen 811- of 812-beelden: '
        'echte productfoto’s waar het om het materiaal gaat, catalogusrenders (gemarkeerd als visualisatie) waar het om de ruimte gaat. '
        'De tekst is op de site echte tekst. Kies A, B of C; daarna zet ik hem in H1-test.</div>' +
        option('A', 'Licht', '812 Walnut Deep · slaapkamer',
               'Rustig en licht, zoals een interieurmagazine: de kop staat donker op papier, het beeld krijgt de ruimte. '
               'Past bij de papierkleur van de hele site en laat het donkere hout extra spreken. Scherpst, omdat het beeld niet schermbreed hoeft.', A_desk, A_mob) +
        option('B', 'Materiaal', '811 Walnut Classic · Signature',
               'Ons paradepaardje in twee delen: links het echte 811-oppervlak in strijklicht met de kop erop, rechts dezelfde wand in een interieur. '
               'Vertelt in één beeld “van ver één vlak, van dichtbij materiaal”. Op mobiel: het materiaal schermvullend.', B_desk, B_mob) +
        option('C', 'Sfeer', '812 Walnut Deep · slaapkamer, schermbreed',
               'Klassiek en filmisch: de slaapkamer over de volle breedte met warm verloop achter de kop. '
               'Meeste sfeer; het beeld wordt wel groter vergroot, dus iets zachter dan A en B.', C_desk, C_mob) +
        '</div>')

page = ('<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n<title>Hero-opties</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;1,500&amp;family=Instrument+Sans:wght@400;500;600&amp;display=swap">\n'
        '<style>\nbody{margin:0}\n.s{font-family:\'Cormorant\',Georgia,serif;font-weight:500}\nimg{display:block}\n'
        '.tag{position:absolute;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:#E9E3D8;color:#6E675E;padding:4px 8px;z-index:3}\n</style>\n</helmet>\n'
        '<div style="width:1440px;height:2700px;position:relative;overflow:hidden;background:#F5F2EC;color:#151413;font-family:\'Instrument Sans\',\'Helvetica Neue\',Arial,sans-serif">\n'
        + body +
        '\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1440,"height":2700}}\'>\n'
        'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')
open(C + 'HeroOpties.dc.html', 'w').write(page)

d = json.load(open(C + 'canvas.json'))
d['boards']['HeroOpties.dc.html'] = {'h': 2700, 'title': 'Homepage-hero · 3 opties (811 / 812)', 'w': 1440, 'x': 1520, 'y': 13820}
if 'HeroOpties.dc.html' not in d['order']:
    d['order'].append('HeroOpties.dc.html')
json.dump(d, open(C + 'canvas.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
