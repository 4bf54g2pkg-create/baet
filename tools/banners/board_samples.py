# Artboard "Samples": drie voorstellen voor de samplepagina / sampleknoppen, met echte stalen uit de productfoto's.
import json
C = '/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/canvas/project/'
D = [('Hout', [('602', 'Wood Classic'), ('607', 'Wood White Oak'), ('615', 'Wood Radiata'), ('810', 'Noir Oak'), ('811', 'Walnut Classic'), ('812', 'Walnut Deep')]),
     ('Beton en travertin', [('691', 'Concrete Smoke'), ('851', 'Travertine Ivory')]),
     ('Japandi', [('619', 'Jade'), ('620', 'Light Brown'), ('821', 'Light'), ('823', 'Taupe Dark'), ('824', 'Taupe')]),
     ('Leer', [('646', 'Khaki'), ('830', 'Taupe'), ('831', 'Sand')]),
     ('Art', [('840', 'Grain Creme'), ('841', 'Grain Blue'), ('842', 'Stucco Light'), ('843', 'Stucco Shadow')]),
     ('Marmer', [('632', 'White Rock'), ('670', 'Pandora Slate'), ('678', 'Italian Gold Slate'), ('689', 'Beverly Gold Slate')])]
SEL = ['811', '824', '851']
INK, STONE, LINE, PAPER, SAND, BRONZE = '#151413', '#6E675E', '#DDD6CA', '#F5F2EC', '#EFEAE1', '#8C6A4A'


def sw(code, size=None):
    return f'<img src="./beeld/staal-{code}.jpg" style="display:block;width:100%;aspect-ratio:1/1;object-fit:cover">'


def tile(code, name, group, state='', num=0):
    on = code in SEL if state == '' else state == 'on'
    n = num or (SEL.index(code) + 1 if code in SEL else 0)
    hover = state == 'hover'
    media = (f'<img src="./beeld/room-{code}.jpg" style="display:block;width:100%;aspect-ratio:1/1;object-fit:cover">' if hover else sw(code))
    ring = f'outline:2px solid {INK};outline-offset:3px;' if on else ''
    badge = (f'<span style="position:absolute;right:8px;top:8px;width:24px;height:24px;border-radius:50%;background:{INK};color:{PAPER};font-size:12px;display:flex;align-items:center;justify-content:center">{n}</span>' if on else
             f'<span style="position:absolute;right:8px;top:8px;width:24px;height:24px;border-radius:50%;background:rgba(245,242,236,.92);color:{INK};font-size:16px;display:flex;align-items:center;justify-content:center">+</span>')
    hv = ('<span style="position:absolute;left:8px;bottom:8px;background:rgba(245,242,236,.92);font-size:10px;color:#6E675E;padding:3px 6px">In een interieur · visualisatie</span>' if hover else '')
    return (f'<div><div style="position:relative;{ring}">{media}{badge}{hv}</div>'
            f'<div style="margin-top:10px;font-size:13px;color:{INK}"><b style="font-weight:600">{code}</b> {name}</div>'
            f'<div style="font-size:11px;color:{STONE};margin-top:2px">{group}</div></div>')


def box(compact=False):
    slots = ''
    for i in range(5):
        if i < len(SEL):
            c = SEL[i]
            nm = [n for g, l in D for cc, n in l if cc == c][0]
            slots += (f'<div style="display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid {LINE}"><div style="width:52px">{sw(c)}</div>'
                      f'<div style="flex:1;font-size:13px"><b style="font-weight:600">{c}</b> {nm}</div><span style="color:{STONE};font-size:16px">×</span></div>')
        else:
            slots += (f'<div style="display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid {LINE}"><div style="width:52px;aspect-ratio:1/1;border:1px dashed #C9C1B4"></div>'
                      f'<div style="font-size:13px;color:#A39B90">Vak {i+1} · nog vrij</div></div>')
    return (f'<div style="background:{PAPER};border:1px solid {LINE};padding:24px">'
            f'<div class="k">Je samplebox</div><div class="s" style="font-size:30px;margin-top:6px">3 van 5 gekozen</div>'
            f'<div style="margin-top:14px">{slots}</div>'
            f'<div style="display:flex;justify-content:space-between;font-size:13px;margin-top:16px"><span>Stalen</span><span>gratis</span></div>'
            f'<div style="display:flex;justify-content:space-between;font-size:13px;margin-top:6px"><span>Verzending</span><span>€ 6,95</span></div>'
            f'<div style="font-size:12px;color:{STONE};margin-top:6px">Binnen 3–5 werkdagen in huis</div>'
            f'<div style="margin-top:18px;background:{INK};color:{PAPER};text-align:center;padding:14px;font-size:14px">Samples aanvragen</div></div>')


# ---------- Optie A: stalenkaart ----------
tabs = ''.join(f'<span style="padding:8px 14px;border:1px solid {INK if i==0 else LINE};{"background:"+INK+";color:"+PAPER+";" if i==0 else ""}font-size:13px">{t}</span>'
               for i, t in enumerate(['Alle 24'] + [f'{g} {len(l)}' for g, l in D]))
grid = ''
for g, l in D[:2]:
    grid += f'<div style="grid-column:1/-1;display:flex;align-items:baseline;gap:12px;margin-top:8px"><span class="s" style="font-size:26px">{g}</span><span style="font-size:12px;color:{STONE}">{len(l)} decors</span></div>'
    for c, n in l:
        grid += tile(c, n, g, 'hover' if c == '812' else '')
A_desk = (f'<div style="background:{PAPER};padding:40px 48px 48px">'
          f'<div style="display:grid;grid-template-columns:1.1fr 1fr;gap:48px;align-items:center">'
          f'<div><div class="k">The Puredeco Edit</div><div class="s" style="font-size:64px;line-height:1;margin-top:12px">Voel het verschil.<br>Tot vijf stalen, gratis.</div>'
          f'<div style="font-size:15px;line-height:1.7;color:#3A3733;margin-top:16px;max-width:520px">Kies je decors op kleur en structuur. Je krijgt echte stalen van het paneel thuis: leg ze naast je vloer, bekijk ze bij daglicht en ’s avonds.</div>'
          f'<div style="display:flex;gap:28px;margin-top:22px;font-size:13px;color:{STONE}"><span><b style="color:{INK}">1</b> Kies tot 5 stalen</span><span><b style="color:{INK}">2</b> € 6,95 verzending</span><span><b style="color:{INK}">3</b> In 3–5 werkdagen thuis</span></div></div>'
          f'<img src="./beeld/samplebox.jpg" style="display:block;width:100%;aspect-ratio:16/10;object-fit:cover"></div>'
          f'<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:40px;padding-top:24px;border-top:1px solid {LINE}">{tabs}</div>'
          f'<div style="display:grid;grid-template-columns:1fr 320px;gap:40px;margin-top:28px;align-items:start">'
          f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px 20px">{grid}</div>'
          f'<div style="position:sticky;top:0">{box()}</div></div></div>')

mob_tiles = ''.join(tile(c, n, 'Hout') for c, n in D[0][1][3:6])
A_mob = (f'<div style="width:300px;border:1px solid {LINE};background:{PAPER};position:relative;overflow:hidden">'
         f'<div style="height:44px;border-bottom:1px solid {LINE};display:flex;align-items:center;justify-content:center;font-size:15px"><b>Pure</b>Deco</div>'
         f'<div style="padding:18px 16px"><div class="k">The Puredeco Edit</div><div class="s" style="font-size:34px;line-height:1;margin-top:8px">Tot vijf stalen, gratis.</div>'
         f'<div style="display:flex;gap:6px;overflow:hidden;margin-top:14px;white-space:nowrap">' +
         ''.join(f'<span style="padding:6px 10px;border:1px solid {INK if i==0 else LINE};{"background:"+INK+";color:"+PAPER+";" if i==0 else ""}font-size:11px">{t}</span>' for i, t in enumerate(['Alle', 'Hout', 'Beton', 'Japandi'])) +
         f'</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 12px;margin-top:16px">{mob_tiles}{tile("824","Taupe","Japandi")}</div></div>'
         f'<div style="position:sticky;bottom:0;background:{INK};color:{PAPER};padding:12px 16px;display:flex;align-items:center;gap:10px">'
         + ''.join(f'<div style="width:30px">{sw(c)}</div>' for c in SEL) +
         f'<div style="width:30px;aspect-ratio:1/1;border:1px dashed #6E675E"></div><div style="width:30px;aspect-ratio:1/1;border:1px dashed #6E675E"></div>'
         f'<span style="margin-left:auto;font-size:12px">Aanvragen →</span></div></div>')

# ---------- Optie B: sample overal ----------
pdp = (f'<div style="background:{PAPER};border:1px solid {LINE};padding:28px;display:grid;grid-template-columns:1fr 1fr;gap:28px">'
       f'<img src="./beeld/room-811.jpg" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover">'
       f'<div><div class="k">Hout · Signature</div><div class="s" style="font-size:40px;line-height:1;margin-top:8px">811 Walnut Classic</div>'
       f'<div style="font-size:14px;margin-top:10px">vanaf <b>€ 139,95</b> per paneel</div>'
       f'<div style="margin-top:18px;background:{INK};color:{PAPER};text-align:center;padding:13px;font-size:14px">In winkelmand</div>'
       f'<div style="margin-top:10px;border:1px solid {INK};display:flex;align-items:center;gap:12px;padding:8px 12px"><div style="width:40px">{sw("811")}</div>'
       f'<div style="font-size:13px;line-height:1.35"><b style="font-weight:600">Eerst voelen? Gratis staal</b><br><span style="color:{STONE}">€ 6,95 verzending · 3–5 werkdagen</span></div><span style="margin-left:auto;font-size:18px">+</span></div>'
       f'<div style="font-size:12px;color:{STONE};margin-top:10px">Combineer met tot 4 andere decors in één samplebox.</div></div></div>')
drawer = (f'<div style="background:{PAPER};border:1px solid {LINE};padding:24px;box-shadow:-20px 0 40px rgba(0,0,0,.08)">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><div class="s" style="font-size:30px">Toegevoegd aan je samplebox</div><span style="font-size:18px">×</span></div>'
          f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:16px">'
          + ''.join(f'<div>{sw(c)}</div>' for c in SEL) + ''.join(f'<div style="aspect-ratio:1/1;border:1px dashed #C9C1B4"></div>' for _ in range(2)) +
          f'</div><div style="font-size:13px;color:{STONE};margin-top:10px">3 van 5 · nog 2 vakken vrij</div>'
          f'<div class="k" style="margin-top:22px">Past hierbij</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:10px">'
          + ''.join(f'<div>{sw(c)}<div style="font-size:12px;margin-top:6px"><b style="font-weight:600">{c}</b> {n}</div><div style="font-size:11px;color:{BRONZE};margin-top:2px">+ Sample</div></div>' for c, n in [('812', 'Walnut Deep'), ('823', 'Taupe Dark'), ('691', 'Concrete Smoke')]) +
          f'</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:22px"><div style="border:1px solid {INK};text-align:center;padding:12px;font-size:13px">Verder kijken</div>'
          f'<div style="background:{INK};color:{PAPER};text-align:center;padding:12px;font-size:13px">Samples aanvragen</div></div></div>')
card = (f'<div style="background:{PAPER};border:1px solid {LINE};padding:20px"><img src="./beeld/room-824.jpg" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover">'
        f'<div style="font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:{BRONZE};margin-top:12px">Japandi</div><div class="s" style="font-size:24px;margin-top:4px">824 Taupe</div>'
        f'<div style="font-size:13px;margin-top:4px">vanaf <b>€ 139,95</b> per paneel</div>'
        f'<div style="display:flex;gap:14px;align-items:center;margin-top:12px"><span style="border-bottom:1px solid {INK};font-size:13px">Bekijk en bereken</span>'
        f'<span style="background:{INK};color:{PAPER};padding:6px 10px;font-size:12px">✓ Sample</span></div></div>')

# ---------- Optie C: stijlwijzer ----------
moods = [('811', 'Warm hout', 'Walnoot en eiken'), ('824', 'Rustig Japandi', 'Stof en linnen'), ('830', 'Zacht leer', 'Taupe en zand'),
         ('843', 'Art en structuur', 'Stucco en grain'), ('678', 'Marmer', 'Doorlopend en mat'), ('851', 'Beton en travertin', 'Steen zonder gewicht')]
mood_html = ''.join(f'<div style="position:relative{";outline:2px solid "+INK+";outline-offset:3px" if c=="811" else ""}"><img src="./beeld/room-{c}.jpg" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover">'
                    f'<div style="position:absolute;left:0;right:0;bottom:0;padding:14px;background:linear-gradient(0deg,rgba(21,20,19,.6),rgba(21,20,19,0));color:{PAPER}">'
                    f'<div class="s" style="font-size:24px">{t}</div><div style="font-size:11px;opacity:.85">{s}</div></div></div>' for c, t, s in moods)
C_html = (f'<div style="background:{PAPER};padding:36px 40px;border:1px solid {LINE}">'
          f'<div style="display:flex;gap:16px;font-size:12px;color:{STONE}"><b style="color:{INK}">1 Stijl</b><span>2 Decors</span><span>3 Box</span></div>'
          f'<div class="s" style="font-size:44px;margin-top:10px">Welke sfeer zoek je?</div>'
          f'<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:20px">{mood_html}</div>'
          f'<div style="margin-top:30px;padding-top:24px;border-top:1px solid {LINE};display:grid;grid-template-columns:320px 1fr;gap:32px;align-items:center">'
          f'<div><div class="k">Stap 2 · warm hout</div><div class="s" style="font-size:32px;margin-top:6px">Onze keuze voor jou</div>'
          f'<div style="font-size:14px;color:#3A3733;margin-top:8px;line-height:1.6">Drie tinten naast elkaar, zodat je ziet wat bij je vloer past. Ruil gerust één decor.</div>'
          f'<div style="margin-top:14px;background:{INK};color:{PAPER};display:inline-block;padding:12px 18px;font-size:13px">Deze 3 in mijn box</div></div>'
          f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px">'
          + ''.join(tile(c, n, 'Hout', 'on' if c in ('810', '811', '812') else 'off', {'811':1,'812':2,'810':3}.get(c,0)) for c, n in [('607', 'Wood White Oak'), ('602', 'Wood Classic'), ('811', 'Walnut Classic'), ('812', 'Walnut Deep'), ('810', 'Noir Oak')]) +
          '</div></div></div>')


def section(letter, name, sub, why):
    return (f'<div style="margin-top:96px;display:flex;align-items:baseline;gap:18px"><span class="s" style="font-size:60px;color:{BRONZE}">{letter}</span>'
            f'<span class="s" style="font-size:46px">{name}</span><span style="font-size:13px;color:{STONE}">{sub}</span></div>'
            f'<div style="font-size:15px;line-height:1.65;color:#3A3733;margin-top:6px;max-width:1080px">{why}</div>')


body = (f'<div class="tag" style="left:24px;top:20px">Samples · drie voorstellen · echte stalen uit de productfoto’s</div>'
        f'<div style="padding:90px 72px 80px">'
        f'<div class="s" style="font-size:64px;line-height:1">Samples: van namenlijst naar materiaalbibliotheek</div>'
        f'<div style="font-size:16px;line-height:1.7;color:#3A3733;margin-top:14px;max-width:1120px">Mensen kiezen een wand op kleur en structuur, niet op naam. '
        f'Daarom tonen alle voorstellen het echte oppervlak als vierkant staal (uitgesneden uit jullie eigen productfoto’s), met de naam eronder en het interieur bij hover. '
        f'De samplebox met vijf vakjes maakt meteen duidelijk wat je kiest, wat het kost en wanneer het komt. '
        f'<b>Advies: A als samplepagina + B op elke productpagina en collectiekaart.</b> C kan later als ingang bovenaan A.</div>' +
        section('A', 'Stalenkaart', 'de samplepagina als materiaalbibliotheek',
                'Grote stalen per collectie, filter met aantallen, gekozen stalen genummerd 1–5. Rechts een vaste samplebox met lege vakken, kosten en levertijd. Op mobiel een balk onderin met je vijf vakjes. Hover: het decor in een interieur (gemarkeerd als visualisatie).') +
        f'<div style="display:grid;grid-template-columns:1fr 300px;gap:32px;margin-top:28px;align-items:start"><div style="border:1px solid {LINE}">{A_desk}</div>{A_mob}</div>' +
        section('B', 'Sample overal', 'knop op productpagina en collectiekaart',
                'Waar iemand twijfelt, staat de knop: op de productpagina direct onder “In winkelmand” met het staal ernaast, en op elke collectiekaart. Na klikken schuift de samplebox in met “Past hierbij”: drie decors die wij bij dit decor aanraden (door jullie te kiezen per product). Iedereen hoeft niet meer naar een aparte pagina.') +
        f'<div style="display:grid;grid-template-columns:1.25fr 1fr 0.6fr;gap:24px;margin-top:28px;align-items:start">{pdp}{drawer}{card}</div>' +
        section('C', 'Stijlwijzer', 'eerst de sfeer, dan de decors',
                'Voor wie nog niet weet wat hij zoekt: kies een sfeer, krijg drie decors die samen werken, ruil er één. Kort, persoonlijk en het verhoogt de kans dat de stalen bij de wand passen. Kan als blok bovenaan de stalenkaart.') +
        f'<div style="margin-top:28px">{C_html}</div>'
        f'<div style="font-size:12px;color:{STONE};margin-top:40px">Stalen zijn uitsneden uit jullie productfoto’s; voor de site gebruiken we dezelfde uitsnede uit de Shopify-productfoto, zodat elk staal automatisch klopt met het decor.</div>'
        f'</div>')

H = 3560
page = ('<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n<title>Samples</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;1,500&amp;family=Instrument+Sans:wght@400;500;600&amp;display=swap">\n'
        '<style>\nbody{margin:0}\n.s{font-family:\'Cormorant\',Georgia,serif;font-weight:500}\n'
        '.k{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A}\nimg{display:block}\n'
        '.tag{position:absolute;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:#E9E3D8;color:#6E675E;padding:4px 8px;z-index:3}\n</style>\n</helmet>\n'
        f'<div style="width:1440px;height:{H}px;position:relative;overflow:hidden;background:#EFEAE1;color:#151413;font-family:\'Instrument Sans\',\'Helvetica Neue\',Arial,sans-serif">\n'
        + body +
        f'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{{"$preview":{{"width":1440,"height":{H}}}}}\'>\n'
        'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')
open(C + 'Samples.dc.html', 'w').write(page)
d = json.load(open(C + 'canvas.json'))
d['boards']['Samples.dc.html'] = {'h': H, 'title': 'Samples · 3 voorstellen', 'w': 1440, 'x': 4560, 'y': 13820}
if 'Samples.dc.html' not in d['order']:
    d['order'].append('Samples.dc.html')
json.dump(d, open(C + 'canvas.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
