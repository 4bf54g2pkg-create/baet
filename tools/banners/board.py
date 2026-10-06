# Maakt het canvas-artboard "Beeldset" met de nieuwe banners en foto's.
import json
C = '/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/canvas/project/'


def sec(k, title, sub):
    return ('<div style="margin-top:96px"><div class="k">' + k + '</div>'
            '<div class="s" style="font-size:44px;margin-top:10px">' + title + '</div>'
            '<div style="font-size:15px;line-height:1.6;color:#3A3733;margin-top:8px;max-width:860px">' + sub + '</div></div>')


def cap(t):
    return '<div style="font-size:12px;color:#6E675E;margin-top:8px">' + t + '</div>'


def img(f):
    return '<img src="./beeld/' + f + '">'


coll = [('hout', 'Hout', 'sfeer: Hout (catalogusbeeld) · materiaal: 812 Walnut Deep'),
        ('japandi', 'Japandi', '823 Taupe Dark · sfeer en materiaal'),
        ('leer', 'Leer', '830 Taupe · sfeer en detail'),
        ('art', 'Art', '843 Stucco Shadow · sfeer en detail'),
        ('marmer', 'Marmer', '678 Italian Gold Slate · doorlopend marmer'),
        ('steen', 'Steen', '851 Travertine Ivory · badkamer en detail')]

coll_html = ''.join(
    '<div>' + img('collectie-' + n + '.jpg') +
    '<div style="display:flex;justify-content:space-between;margin-top:10px"><span class="s" style="font-size:26px">' + t +
    '</span><span style="font-size:12px;color:#6E675E">' + c + '</span></div></div>' for n, t, c in coll)

hero = (
    '<div style="display:grid;grid-template-columns:1fr 300px;gap:24px;margin-top:28px;align-items:end">'
    '<div style="position:relative">' + img('home-hero-desktop.jpg') +
    '<div style="position:absolute;left:6%;top:30%;color:#F5F2EC">'
    '<div style="font-size:11px;letter-spacing:.22em;text-transform:uppercase;opacity:.85">Wandpanelen met bamboekern · voor wonen en projecten</div>'
    '<div class="s" style="font-size:84px;line-height:.95;margin-top:14px">Eén wand.<br>Eén geheel.</div>'
    '<div style="display:flex;gap:10px;margin-top:22px"><span style="background:#F5F2EC;color:#151413;padding:12px 18px;font-size:13px">Ontdek de collecties</span>'
    '<span style="border:1px solid #F5F2EC;padding:12px 18px;font-size:13px">Voor projecten</span></div></div>'
    '<div style="position:absolute;right:16px;bottom:12px;font-size:11px;color:#F5F2EC;opacity:.85">851 Travertine Ivory · visualisatie</div></div>'
    '<div style="position:relative">' + img('home-hero-mobile.jpg') +
    '<div style="position:absolute;left:16px;bottom:20px;color:#F5F2EC;text-shadow:0 1px 12px rgba(0,0,0,.3)">'
    '<div class="s" style="font-size:40px;line-height:.95">Eén wand.<br>Eén geheel.</div></div></div></div>')

pro = ('<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr 1fr;gap:16px;margin-top:28px;align-items:end">'
       '<div>' + img('projects-hero.jpg') + cap('Hero · 1600 × 2000') + '</div>' +
       ''.join('<div>' + img('sector-' + n + '.jpg') + cap(t) + '</div>' for n, t in
               [('hotels', 'Hotels'), ('horeca', 'Horeca'), ('kantoren', 'Kantoren'), ('retail', 'Retail en showrooms')]) +
       '</div>')

social = ('<div style="display:grid;grid-template-columns:1fr 1fr 1fr 0.75fr;gap:20px;margin-top:28px;align-items:end">' +
          ''.join('<div>' + img('social-' + n + '.jpg') + cap('Post 1080 × 1350') + '</div>' for n in ['851', '823', '678']) +
          '<div>' + img('social-story-851.jpg') + cap('Story 1080 × 1920') + '</div></div>')

body = (
    '<div class="tag" style="left:24px;top:20px">Beeldset · voorstel · gemaakt uit jullie eigen catalogus- en projectbeelden</div>'
    '<div style="padding:90px 96px 0">'
    '<div class="s" style="font-size:64px;line-height:1">Eén beeldtaal voor de hele site</div>'
    '<div style="font-size:16px;line-height:1.7;color:#3A3733;margin-top:16px;max-width:980px">Elk beeld komt uit jullie eigen catalogus: '
    'het decor in beeld is altijd het decor dat erbij staat. Renders blijven gemarkeerd als visualisatie, de 670-beelden zijn echt. '
    'Op de site staat tekst nooit ín het beeld maar erop als echte tekst; zo blijft alles scherp, vindbaar en aanpasbaar. '
    'Eén warme kleurcorrectie (“avondlicht”) houdt de set samen.</div>' +
    sec('1 · Homepage', 'Hero: 851 Travertine Ivory',
        'De huidige heldenfoto heeft de tekst “PureDeco wandpanelen” ín het beeld en botst daardoor met de nieuwe kop. '
        'Nieuw: een rustig vlak voor de tekst en het interieur in zijlicht. Hetzelfde beeld staand voor mobiel.') +
    hero + cap('Desktop 2400 × 1200 · mobiel 1080 × 1600') +
    sec('2 · Collectiepagina’s', 'Sfeer naast het materiaal van dichtbij',
        'Per collectie een kopbanner: links het interieur, rechts het oppervlak van hetzelfde decor. '
        'Hetzelfde sfeerbeeld ook als collectiekaart op de homepage (16:10).') +
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px 24px;margin-top:28px">' + coll_html + '</div>' +
    cap('Banner 2400 × 900 · kaart 1600 × 1000 · sfeerbeelden zijn visualisaties en worden zo gemarkeerd') +
    sec('3 · Puredeco Projects', 'Sectoren met het juiste decor',
        'Hotels: 678 Italian Gold Slate · Horeca: 689 Beverly Gold Slate · Kantoren: 810 Noir Oak · Retail en showrooms: 823 Taupe Dark · '
        'hero: 678 in een lounge. Alle visualisaties, tot het eerste grote project gefotografeerd is.') +
    pro +
    '<div style="display:grid;grid-template-columns:1fr 1.5fr;gap:48px;align-items:start">'
    '<div>' + sec('4 · The Puredeco Edit', 'Drie echte stalen',
                  '811 Walnut Classic, 824 Taupe en 851 Travertine Ivory, gesneden uit de echte productfoto’s. '
                  'Voor het samplesblok op de homepage en het samplesvenster.') +
    '<div style="margin-top:24px">' + img('edit-samplebox.jpg') + '</div>' + cap('1600 × 1200') + '</div>'
    '<div>' + sec('5 · In de praktijk', '670 Pandora Slate, echt geplaatst',
                  'Echte beelden uit jullie video: op maat zagen, plaatsen, het resultaat. '
                  'Voor de productpagina van 670, een projectpagina of social.') +
    '<div style="margin-top:24px">' + img('praktijk-670.jpg') + '</div>' + cap('2400 × 1000 · echte foto’s, geen visualisatie') + '</div></div>' +
    sec('6 · Social', 'Posts en story in dezelfde stijl',
        'Hier mag tekst wél in het beeld: decorcode, naam en de belofte. Klaar voor Instagram en Facebook.') +
    social + '</div>')

page = ('<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n<title>Beeldset</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;1,500&amp;family=Instrument+Sans:wght@400;500;600&amp;display=swap">\n'
        '<style>\nbody{margin:0}\n.s{font-family:\'Cormorant\',Georgia,serif;font-weight:500}\n'
        '.k{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A}\nimg{display:block;width:100%}\n'
        '.tag{position:absolute;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:#E9E3D8;color:#6E675E;padding:4px 8px;z-index:3}\n</style>\n</helmet>\n'
        '<div style="width:1440px;height:4300px;position:relative;overflow:hidden;background:#F5F2EC;color:#151413;font-family:\'Instrument Sans\',\'Helvetica Neue\',Arial,sans-serif">\n'
        + body +
        '\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1440,"height":4300}}\'>\n'
        'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')
open(C + 'Beeldset.dc.html', 'w').write(page)

d = json.load(open(C + 'canvas.json'))
d['boards']['Beeldset.dc.html'] = {'h': 4300, 'title': 'Beeldset · banners en foto’s (voorstel)', 'w': 1440, 'x': 0, 'y': 13820}
d['notes']['beeld'] = {'kind': 'title1', 'maxW': 3900, 'text': 'Ronde 8 · beeldset uit de eigen catalogus · voorstel, nog niet geplaatst',
                       'w': 240, 'x': 0, 'y': 13600}
if 'Beeldset.dc.html' not in d['order']:
    d['order'].append('Beeldset.dc.html')
json.dump(d, open(C + 'canvas.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
