#!/usr/bin/env python3
"""Genereert docs/ontwerp-puredeco-finish/InspiratieV2.dc.html (artboard Inspiratie v2)."""
import importlib.util, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'tools', 'inspiratie-tekeningen.py'))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
S = 'inspiratie/stalen/'
t.TEX.update(badkamer=S + 'travertin-851.jpg', toilet=S + 'marmer-666.jpg', keuken=S + 'beton-691.jpg',
             woonkamer=S + 'hout-811.jpg', slaapkamer=S + 'leer-646.jpg', werkplek=S + 'japandi-619.jpg')
D = {k: f() for k, f in t.ROOMS.items()}

ROOMS = [('badkamer', 'Wandpanelen in de badkamer', 'Decors voor natte ruimtes, plaatsen en kosten'),
         ('toilet', 'Wandpanelen in het toilet', 'Kleine ruimte, groot verschil'),
         ('keuken', 'Wandpanelen in de keuken', 'Achterwand en kookhoek'),
         ('woonkamer', 'Wandpanelen in de woonkamer', 'Tv-wand en accentwand'),
         ('slaapkamer', 'Wandpanelen in de slaapkamer', 'Achter het bed'),
         ('werkplek', 'Wandpanelen op kantoor', 'Rust en akoestiek')]
MAT = [('hout-811', 'Hout', 'hout-1'), ('marmer-692', 'Marmerlook', 'wandpanelen'), ('beton-691', 'Betonlook', 'wandpanelen'),
       ('travertin-851', 'Travertinlook', 'wandpanelen'), ('japandi-619', 'Japandi', 'japandi'), ('leer-646', 'Leer', 'leer'),
       ('art-842', 'Art', 'kunst'), ('marmer-666', 'Marmer glans', 'wandpanelen')]


def room_cards(n=6, h=210):
    out = []
    for key, title, sub in ROOMS[:n]:
        out.append(f'<div><div style="background:#F5F2EC;border:1px solid #E2DBCF;padding:14px 10px 4px">{D[key]}</div>'
                   f'<div class="ttl" style="font-size:24px;margin-top:14px">{title}</div><div class="note">{sub}</div></div>')
    return ''.join(out)


def swatches(size=128):
    return ''.join(f'<div><img src="{S}{f}.jpg" style="width:{size}px;height:{size}px;object-fit:cover"><div style="font-size:13px;margin-top:8px">{n}</div></div>'
                   for f, n, _ in MAT)


PIN = lambda n, top, left: f'<div class="pin" style="top:{top}px;left:{left}px">{n}</div>'
LEG = lambda items: '<div class="leg">' + ''.join(f'<div><span class="pn">{i}</span>{t}</div>' for i, t in enumerate(items, 1)) + '</div>'

html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Inspiratie v2</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;1,500&amp;family=Instrument+Sans:wght@400;500;600&amp;display=swap">
<style>
@font-face{{font-family:'Cormorant';src:url('../../tools/banners/cormorant.woff2') format('woff2');font-weight:300 700}}
@font-face{{font-family:'Instrument Sans';src:url('../../tools/banners/instrument.woff2') format('woff2');font-weight:400 700}}
body{{margin:0}}
.s{{font-family:'Cormorant',Georgia,serif;font-weight:500}}
.k{{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A}}
.eyeb{{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#6E675E}}
.tag{{position:absolute;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:#E9E3D8;color:#6E675E;padding:4px 8px;z-index:3}}
.h2{{font-family:'Cormorant',Georgia,serif;font-weight:500;font-size:46px;line-height:1.05;margin:0}}
.lead{{font-size:16px;line-height:1.7;color:#3A3733;max-width:1080px;margin-top:12px}}
.note{{font-size:13px;line-height:1.6;color:#6E675E}}
.sec{{margin-top:96px;display:flex;align-items:baseline;gap:18px}}
.num{{font-family:'Cormorant',Georgia,serif;font-size:60px;color:#8C6A4A;line-height:1}}
ul.l,ol.l{{margin:10px 0 0;padding-left:20px;font-size:14.5px;line-height:1.75;color:#3A3733}}
img,svg{{display:block}}
svg{{width:100%;height:auto}}
.frame{{background:#F5F2EC;border:1px solid #DDD6CA;overflow:hidden;position:relative}}
.nav{{height:64px;padding:0 48px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;border-bottom:1px solid #DDD6CA;font-size:13px}}
.nav b{{font-family:'Cormorant',Georgia,serif;font-size:26px;font-weight:500}}
.ttl{{font-family:'Cormorant',Georgia,serif;font-size:26px;line-height:1.1}}
.lnk{{font-size:13.5px;border-bottom:1px solid #151413;padding-bottom:2px;display:inline-block}}
.box{{background:#F5F2EC;border:1px solid #DDD6CA}}
.real{{position:absolute;left:8px;bottom:8px;background:rgba(21,20,19,.72);color:#F5F2EC;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;padding:3px 7px}}
.pin{{position:absolute;z-index:5;width:26px;height:26px;border-radius:50%;background:#8C6A4A;color:#F5F2EC;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 4px rgba(140,106,74,.22)}}
.leg{{display:grid;grid-template-columns:1fr 1fr;gap:10px 40px;margin-top:18px;font-size:13.5px;line-height:1.5;color:#3A3733}}
.leg div{{display:grid;grid-template-columns:34px 1fr;align-items:start}}
.pn{{width:22px;height:22px;border-radius:50%;background:#8C6A4A;color:#F5F2EC;font-size:11.5px;font-weight:600;display:flex;align-items:center;justify-content:center}}
table.t{{border-collapse:collapse;width:100%;font-size:13.5px}}
table.t th{{text-align:left;font-weight:500;color:#6E675E;font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:8px 10px;border-bottom:1px solid #151413}}
table.t td{{padding:9px 10px;border-bottom:1px solid #DDD6CA;vertical-align:top}}
.faq{{display:grid;grid-template-columns:1fr auto;padding:16px 0;border-top:1px solid #DDD6CA;font-size:15px}}
.toc a{{display:block;font-size:13.5px;padding:7px 0;border-top:1px solid #DDD6CA;color:#151413;text-decoration:none}}
.pc .im{{position:relative}}
</style>
</helmet>
<div style="width:1440px;height:9560px;position:relative;overflow:hidden;background:#EFEAE1;color:#151413;font-family:'Instrument Sans','Helvetica Neue',Arial,sans-serif">
<div class="tag" style="left:24px;top:20px">Inspiratie v2 · gebouwd op zoekdata · zonder fotoshoot · nog niets aangepast</div>
<div style="padding:90px 72px 80px">

<div class="s" style="font-size:64px;line-height:1">Inspiratie die gevonden wordt</div>
<div class="lead">Versie 2. Uitgangspunt: wat mensen echt zoeken (Google Search Console, 90 dagen) en een beeldtaal die zonder fotoshoot premium is. Elke ruimte krijgt een eigen gids die één zoekvraag goed beantwoordt; samen vormen ze de inspiratiepagina. Echte projecten komen erbij zodra er goede foto's zijn.</div>

<!-- 1 Data -->
<div class="sec"><span class="num">1</span><span class="h2">Wat Google nu laat zien</span></div>
<div style="display:grid;grid-template-columns:360px 1fr;gap:48px;margin-top:28px;align-items:start">
  <div class="box" style="padding:26px 28px">
    <div class="k">Inspiratie + 6 artikelen · 90 dagen</div>
    <div style="display:flex;gap:36px;margin-top:14px"><div><div class="s" style="font-size:56px;line-height:1">115</div><div class="note">vertoningen in Google</div></div><div><div class="s" style="font-size:56px;line-height:1">2</div><div class="note">klikken</div></div></div>
    <div class="note" style="margin-top:14px">De pagina's bestaan, maar beantwoorden geen zoekvraag. Ter vergelijking: de homepage en collecties halen samen duizenden vertoningen.</div>
  </div>
  <div>
    <div class="k">Zoekvragen waar nu geen goede pagina voor is</div>
    <table class="t" style="margin-top:10px">
      <tr><th>Zoekvraag (voorbeelden)</th><th>Vertoningen</th><th>Positie nu</th><th>Nieuwe pagina</th></tr>
      <tr><td>bamboe panelen · bamboe paneel · bamboe wand · bamboe wandbekleding · wanddecoratie bamboe</td><td>±915</td><td>18 – 56</td><td><b>Bamboe wandpanelen: wat zijn het?</b></td></tr>
      <tr><td>bamboe panelen badkamer · bamboe wandpaneel badkamer · badkamer wandpanelen · wandpanelen douche · japandi wandpaneel badkamer</td><td>±57</td><td>5 – 74</td><td><b>Wandpanelen in de badkamer</b></td></tr>
      <tr><td>wandpanelen over tegels badkamer · wandpaneel plaatsen · montage wandpanelen</td><td>±5</td><td>9 – 58</td><td><b>Wandpanelen over tegels plaatsen</b></td></tr>
      <tr><td>wandpanelen hoek afwerken · hoekprofiel voor wandpanelen · wandpanelen hoekprofiel</td><td>±8</td><td>10 – 12</td><td><b>Hoeken en randen afwerken</b></td></tr>
      <tr><td>wandpaneel keuken · keuken wandpanelen · keuken wandpaneel</td><td>±6</td><td>42 – 77</td><td><b>Wandpanelen in de keuken</b></td></tr>
      <tr><td>wandpanelen slaapkamer · wandpaneel slaapkamer · wandpanelen woonkamer · muurpanelen woonkamer</td><td>±7</td><td>3 – 12</td><td><b>Slaapkamer</b> · <b>Woonkamer</b></td></tr>
      <tr><td>wandpanelen toilet</td><td>1</td><td>69</td><td><b>Wandpanelen in het toilet</b></td></tr>
      <tr><td>akupanelen · akoestische wandpanelen · akoestiek wandpanelen</td><td>±410</td><td>13 – 74</td><td>Collectie Akupanelen verbeteren + gids <b>Werkplek</b></td></tr>
    </table>
    <div class="note" style="margin-top:10px">Vertoningen zijn die van puredeco.nl zelf; het echte zoekvolume is hoger. Bij positie 10+ zien weinig mensen je, vandaar weinig vertoningen: een goede pagina kan dat veranderen. Merknamen van anderen ('pure panelen', 1.130×) en spam-zoekwoorden uit de oude hack zijn weggelaten.</div>
  </div>
</div>

<!-- 2 Beeldtaal -->
<div class="sec"><span class="num">2</span><span class="h2">Beeldtaal zonder fotoshoot</span></div>
<div class="lead" style="margin-top:8px">Drie lagen, alle drie eerlijk. Wat er niet is, wordt niet nagemaakt.</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px;margin-top:28px">
  <div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px"><img src="{S}hout-811.jpg" style="width:100%;aspect-ratio:1"><img src="{S}marmer-692.jpg" style="width:100%;aspect-ratio:1"><img src="{S}leer-646.jpg" style="width:100%;aspect-ratio:1"><img src="{S}travertin-851.jpg" style="width:100%;aspect-ratio:1"><img src="{S}japandi-619.jpg" style="width:100%;aspect-ratio:1"><img src="{S}beton-691.jpg" style="width:100%;aspect-ratio:1"></div>
    <div class="ttl" style="margin-top:16px">1 · Materiaalscans</div><div class="note">Uitsneden uit de scherpe productscans (2048 px) die er al zijn. Echt materiaal, echte kleur.</div></div>
  <div><div style="background:#F5F2EC;border:1px solid #E2DBCF;padding:14px 10px 4px">{D["woonkamer"]}</div>
    <div class="ttl" style="margin-top:16px">2 · Lijntekeningen met materiaal</div><div class="note">Een wandaanzicht per ruimte, op schaal (paneel 122 × 280 cm), de wand gevuld met een echt decor. Als code in het thema: geen extra laadtijd.</div></div>
  <div><div style="position:relative;height:282px;overflow:hidden;background:#E9E3D8"><img src="inspiratie/kantoor.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real">Echte foto</span></div>
    <div class="ttl" style="margin-top:16px">3 · Echte projecten (klein)</div><div class="note">Klantfoto's klein en eerlijk als bewijs, niet als blikvanger. Zo vallen onscherpte en rommel minder op. Betere foto's schuiven later vanzelf in.</div></div>
</div>

<!-- 3 Hub desktop -->
<div class="sec"><span class="num">3</span><span class="h2">De inspiratiepagina</span><span class="note">/blogs/nieuws · URL blijft</span></div>
<div class="frame" style="margin-top:24px;width:1296px">
  <div class="nav"><div style="display:flex;gap:28px"><span>Collecties</span><span style="border-bottom:1px solid #151413">Inspiratie</span><span>Projecten</span><span>Studio</span></div><b>PureDeco</b><div style="display:flex;gap:22px;justify-content:flex-end"><span>Professionals</span><span style="border:1px solid #151413;padding:6px 12px">Samples</span></div></div>
  <div style="padding:18px 72px 0" class="note">Home · Inspiratie</div>
  <div style="padding:40px 72px 0;display:grid;grid-template-columns:7fr 5fr;gap:72px;align-items:end">
    <div><div class="k">Inspiratie &amp; advies</div><div class="s" style="font-size:66px;line-height:1;margin-top:14px">Wandpanelen voor elke ruimte</div></div>
    <div style="font-size:15.5px;line-height:1.7;color:#3A3733">Per ruimte uitgelegd: welke decors passen, hoe je plaatst en wat een wand kost. Met tekeningen op schaal en projecten van klanten.</div>
  </div>
  <div style="padding:32px 72px 0;display:flex;gap:44px;font-size:13.5px;color:#3A3733;border-bottom:1px solid #DDD6CA;padding-bottom:22px">
    <span>Panelen <b>tot 280 cm</b> hoog, 122 cm breed</span><span>Vanaf <b>€ 26,33 per m²</b></span><span><b>Gratis stalen</b> · € 6,95 verzending</span><span>Studio <b>Herwen</b> op afspraak</span>
  </div>
  <div style="padding:52px 72px 0"><div class="k">Per ruimte</div><div class="s" style="font-size:38px;margin-top:8px">Waar komt je wand?</div></div>
  <div style="padding:26px 72px 0;display:grid;grid-template-columns:repeat(3,1fr);gap:28px 28px">{room_cards()}</div>
  <div style="padding:64px 72px 0;display:grid;grid-template-columns:4fr 8fr;gap:56px;align-items:start">
    <div><div class="k">Per materiaal</div><div class="s" style="font-size:38px;margin-top:8px">Kies je uitstraling</div><div class="note" style="margin-top:10px">Elke tegel linkt naar de collectie.</div></div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px">{''.join(f'<div><img src="{S}{f}.jpg" style="width:100%;aspect-ratio:1;object-fit:cover"><div style="font-size:13.5px;margin-top:8px">{n} →</div></div>' for f, n, _ in MAT)}</div>
  </div>
  <div style="padding:64px 72px 0;display:grid;grid-template-columns:4fr 8fr;gap:56px">
    <div><div class="k">Zelf aan de slag</div><div class="s" style="font-size:38px;margin-top:8px">Plaatsen en onderhoud</div></div>
    <div>
      <div class="faq"><span><span class="s" style="font-size:24px">Bamboe wandpanelen: wat zijn het?</span><br><span class="note">Opbouw, uitvoeringen Linea en Signature, waar ze wel en niet passen</span></span><span class="lnk">Lezen →</span></div>
      <div class="faq"><span><span class="s" style="font-size:24px">Wandpanelen over tegels plaatsen</span><br><span class="note">Ondergrond, lijm, volgorde · met tekening</span></span><span class="lnk">Lezen →</span></div>
      <div class="faq"><span><span class="s" style="font-size:24px">Hoeveel panelen heb ik nodig?</span><br><span class="note">Rekenhulp: maat invullen, aantal en prijs zien</span></span><span class="lnk">Berekenen →</span></div>
      <div class="faq"><span><span class="s" style="font-size:24px">Hoeken en randen afwerken</span><br><span class="note">Welk profiel waar</span></span><span class="lnk">Lezen →</span></div>
      <div class="faq" style="border-bottom:1px solid #DDD6CA"><span><span class="s" style="font-size:24px">Je wandpanelen onderhouden</span><br><span class="note">Bestaand artikel, opgeschoond</span></span><span class="lnk">Lezen →</span></div>
    </div>
  </div>
  <div style="padding:64px 72px 0"><div class="k">Uit de praktijk</div><div class="s" style="font-size:38px;margin-top:8px">Projecten van klanten</div></div>
  <div style="padding:22px 72px 0;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">
    <div><div style="position:relative;height:180px;overflow:hidden"><img src="inspiratie/kantoor.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real">Echte foto</span></div><div class="eyeb" style="margin-top:10px">Kantoor</div><div style="font-size:14px;margin-top:4px">619 Jade + Akupaneel 302 Walnut</div></div>
    <div><div style="position:relative;height:180px;overflow:hidden"><img src="inspiratie/keuken.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real">Echte foto</span></div><div class="eyeb" style="margin-top:10px">Keuken</div><div style="font-size:14px;margin-top:4px">670 Pandora Slate · glans</div></div>
    <div><div style="position:relative;height:180px;overflow:hidden"><img src="{S}leer-646.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real" style="background:rgba(140,106,74,.9)">Decor</span></div><div class="eyeb" style="margin-top:10px">Uitbouw</div><div style="font-size:14px;margin-top:4px">646 Khaki leer + antraciet profielen</div></div>
    <div><div style="position:relative;height:180px;overflow:hidden"><img src="{S}marmer-666.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real" style="background:rgba(140,106,74,.9)">Decor</span></div><div class="eyeb" style="margin-top:10px">Toilet</div><div style="font-size:14px;margin-top:4px">666 White Slate · over de tegels</div></div>
  </div>
  <div class="note" style="padding:10px 72px 0">Zolang er geen goede na-foto is, toont de kaart het decor zelf (gelabeld 'Decor') in plaats van een foto tijdens het werk.</div>
  <div style="padding:64px 72px 72px;display:grid;grid-template-columns:4fr 8fr;gap:56px">
    <div><div class="k">Veelgestelde vragen</div><div class="s" style="font-size:38px;margin-top:8px">Kort antwoord</div></div>
    <div>
      <div class="faq"><span>Wat is het verschil tussen Linea en Signature?</span><span>+</span></div>
      <div class="faq"><span>Hoeveel panelen heb ik nodig voor mijn wand?</span><span>+</span></div>
      <div class="faq"><span>Kan ik wandpanelen in de badkamer gebruiken?</span><span>+</span></div>
      <div class="faq" style="border-bottom:1px solid #DDD6CA"><span>Kan ik eerst een staal bekijken?</span><span>+</span></div>
    </div>
  </div>
  {PIN(1, 92, 26)}
  {PIN(2, 200, 26)}
  {PIN(3, 452, 26)}
  {PIN(4, 560, 26)}
  {PIN(5, 1180, 26)}
</div>
{LEG(['Kruimelpad + ItemList-schema met alle gidsen', 'Eén H1 met zoekwoord; titel in Google: &quot;Wandpanelen inspiratie en advies per ruimte | PureDeco&quot;', 'Elke ruimtekaart is een interne link naar een gids met een eigen zoekwoord', 'Tekeningen zijn code (SVG): geen zware openingsfoto, dus snel (LCP = tekst)', 'Materiaaltegels linken naar de collecties: inspiratie stuurt door naar de winkel'])}

<!-- 4 Ruimtegids -->
<div class="sec"><span class="num">4</span><span class="h2">Een ruimtegids</span><span class="note">voorbeeld: badkamer · zelfde opbouw voor elke ruimte</span></div>
<div class="frame" style="margin-top:24px;width:1296px">
  <div class="nav"><div style="display:flex;gap:28px"><span>Collecties</span><span style="border-bottom:1px solid #151413">Inspiratie</span><span>Projecten</span><span>Studio</span></div><b>PureDeco</b><div style="display:flex;gap:22px;justify-content:flex-end"><span>Professionals</span><span style="border:1px solid #151413;padding:6px 12px">Samples</span></div></div>
  <div style="padding:18px 72px 0" class="note">Home · Inspiratie · Badkamer</div>
  <div style="padding:36px 72px 0;display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:start">
    <div>
      <div class="k">Gids · Badkamer</div>
      <div class="s" style="font-size:58px;line-height:1;margin-top:14px">Wandpanelen in de badkamer</div>
      <div class="box" style="padding:18px 20px;margin-top:24px;background:#EFEAE1">
        <div class="eyeb">Kort antwoord</div>
        <div style="font-size:15px;line-height:1.7;margin-top:8px">Ja. De panelen zijn waterbestendig en komen in één stuk van 280 cm hoog, dus zonder voegen per tegel. Kies Signature (8 mm, klik) voor een naadloze wand op een vlakke ondergrond, of Linea (5 mm) met een zichtbare naad.</div>
      </div>
      <div class="toc" style="margin-top:24px"><div class="eyeb" style="margin-bottom:6px">In deze gids</div><a>Welke decors passen</a><a>Linea of Signature</a><a>Wat kost een badkamerwand</a><a>Plaatsen, ook over tegels</a><a>Onderhoud</a><a style="border-bottom:1px solid #DDD6CA">Veelgestelde vragen</a></div>
    </div>
    <div><div style="background:#F5F2EC;border:1px solid #E2DBCF;padding:18px 14px 6px">{D["badkamer"]}</div><div class="note" style="margin-top:8px">Tekening op schaal · wand in 851 Travertine Ivory</div></div>
  </div>
  <div style="padding:64px 72px 0"><div class="eyeb">01</div><div class="s" style="font-size:38px;margin-top:6px">Welke decors passen in de badkamer</div></div>
  <div style="padding:22px 72px 0;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">
    <div class="pc"><img src="{S}travertin-851.jpg" style="width:100%;aspect-ratio:1;object-fit:cover"><div class="eyeb" style="margin-top:10px">Travertinlook · 851</div><div class="ttl" style="font-size:22px">Travertine Ivory</div><div style="font-size:13.5px;margin-top:4px">€ 179,95 <span class="note">· ≈ € 52,68 per m²</span></div></div>
    <div class="pc"><img src="{S}marmer-666.jpg" style="width:100%;aspect-ratio:1;object-fit:cover"><div class="eyeb" style="margin-top:10px">Marmer glans · 666</div><div class="ttl" style="font-size:22px">White Slate</div><div style="font-size:13.5px;margin-top:4px">€ 99,95 <span class="note">· ≈ € 29,26 per m²</span></div></div>
    <div class="pc"><img src="{S}marmer-692.jpg" style="width:100%;aspect-ratio:1;object-fit:cover"><div class="eyeb" style="margin-top:10px">Marmerlook · 692</div><div class="ttl" style="font-size:22px">Urban Smoke</div><div style="font-size:13.5px;margin-top:4px">€ 139,95 <span class="note">· ≈ € 40,97 per m²</span></div></div>
    <div class="pc"><img src="{S}hout-811.jpg" style="width:100%;aspect-ratio:1;object-fit:cover"><div class="eyeb" style="margin-top:10px">Hout · 811</div><div class="ttl" style="font-size:22px">Walnut Classic</div><div style="font-size:13.5px;margin-top:4px">vanaf € 139,95 <span class="note">· ≈ € 40,97 per m²</span></div></div>
  </div>
  <div class="note" style="padding:8px 72px 0">Prijzen en prijs per m² komen live uit de winkel (zelfde berekening als op de collectiekaarten).</div>
  <div style="padding:56px 72px 0;display:grid;grid-template-columns:1fr 1fr;gap:56px">
    <div><div class="eyeb">02</div><div class="s" style="font-size:34px;margin-top:6px">Linea of Signature</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px">
        <div class="box" style="padding:14px"><svg viewBox="0 0 200 60"><rect x="10" y="22" width="88" height="10" fill="#D8CFC2" stroke="#151413"/><rect x="102" y="22" width="88" height="10" fill="#D8CFC2" stroke="#151413"/><line x1="100" y1="14" x2="100" y2="40" stroke="#8C6A4A" stroke-dasharray="2 2"/></svg><div style="font-size:13.5px;margin-top:8px"><b>Linea</b> · 5 mm, stomp<br><span class="note">zichtbare naad</span></div></div>
        <div class="box" style="padding:14px"><svg viewBox="0 0 200 60"><path d="M10 22h86v4h6v6H10z" fill="#D8CFC2" stroke="#151413"/><path d="M190 22h-88v4h-6v6h94z" fill="#C9BFB1" stroke="#151413"/></svg><div style="font-size:13.5px;margin-top:8px"><b>Signature</b> · 8 mm, klik<br><span class="note">naadloos op vlakke ondergrond</span></div></div>
      </div></div>
    <div><div class="eyeb">03</div><div class="s" style="font-size:34px;margin-top:6px">Wat kost een badkamerwand</div>
      <div class="box" style="padding:18px 20px;margin-top:16px">
        <div class="eyeb">Rekenvoorbeeld</div>
        <table class="t" style="margin-top:6px"><tr><td>Wand</td><td>2,44 m breed × 2,60 m hoog</td></tr><tr><td>Panelen</td><td>2 × 122 × 280 cm (ingekort tot 260)</td></tr><tr><td>Decor</td><td>692 Urban Smoke · Linea</td></tr><tr><td><b>Totaal panelen</b></td><td><b>€ 279,90</b></td></tr></table>
        <div style="margin-top:12px"><span class="lnk">Reken je eigen wand uit →</span></div>
      </div></div>
  </div>
  <div style="padding:56px 72px 0;display:grid;grid-template-columns:1fr 1fr;gap:56px">
    <div><div class="eyeb">04</div><div class="s" style="font-size:34px;margin-top:6px">Plaatsen, ook over tegels</div><div style="font-size:14.5px;line-height:1.75;color:#3A3733;margin-top:10px">Stappen met kleine tekeningen, uit de montagehandleiding. Link naar de volledige gids 'Wandpanelen over tegels plaatsen'.</div></div>
    <div><div class="eyeb">Uit de praktijk</div><div style="display:grid;grid-template-columns:150px 1fr;gap:16px;margin-top:10px;align-items:center"><div style="position:relative;height:110px;overflow:hidden"><img src="{S}marmer-666.jpg" style="width:100%;height:100%;object-fit:cover"><span class="real" style="background:rgba(140,106,74,.9)">Decor</span></div><div><div class="ttl" style="font-size:22px">Toilet vernieuwd over de tegels</div><div class="note">666 White Slate · glans</div></div></div></div>
  </div>
  <div style="padding:56px 72px 64px;display:grid;grid-template-columns:1fr 1fr;gap:56px">
    <div><div class="eyeb">Veelgestelde vragen</div><div class="faq" style="margin-top:8px"><span>Kan ik panelen in de douche gebruiken?</span><span>+</span></div><div class="faq"><span>Moet ik de tegels eerst verwijderen?</span><span>+</span></div><div class="faq" style="border-bottom:1px solid #DDD6CA"><span>Hoe maak ik de panelen schoon?</span><span>+</span></div></div>
    <div class="box" style="padding:24px 26px;background:#151413;color:#F5F2EC;border:0"><div class="k" style="color:#C9B49A">Eerst voelen</div><div class="s" style="font-size:30px;margin-top:8px">Bestel gratis stalen van deze decors</div><div style="margin-top:16px;display:flex;gap:18px;font-size:13.5px"><span style="border-bottom:1px solid #F5F2EC">Stalen kiezen →</span><span style="border-bottom:1px solid #F5F2EC">Plan een bezoek in Herwen →</span></div></div>
  </div>
  {PIN(1, 92, 26)}
  {PIN(2, 316, 26)}
  {PIN(3, 488, 26)}
  {PIN(4, 790, 26)}
  {PIN(5, 1296, 640)}
</div>
{LEG(['Article-schema met echte datum en wijzigingsdatum + BreadcrumbList', 'Kort antwoord meteen bovenaan: kans op een uitgelicht fragment in Google', 'Inhoudsopgave met ankers: Google toont soms directe links naar een kopje', 'Echte prijzen uit de winkel + ItemList-schema; links naar de productpagina’s', 'Rekenvoorbeeld beantwoordt &quot;wat kost een badkamerwand&quot;'])}
<div class="note" style="margin-top:12px">Teksten in 'Kort antwoord' en FAQ worden vóór plaatsing gecontroleerd; alleen wat klopt (zoals 'waterbestendig', al goedgekeurd in de collectieteksten).</div>

<!-- 5 Mobiel -->
<div class="sec"><span class="num">5</span><span class="h2">Op mobiel</span></div>
<div style="display:flex;gap:48px;margin-top:28px;align-items:flex-start">
  <div class="frame" style="width:390px">
    <div style="height:56px;padding:0 18px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #DDD6CA"><span>☰</span><b class="s" style="font-size:24px">PureDeco</b><span style="font-size:12px">⌕</span></div>
    <div style="padding:28px 20px 0"><div class="k">Inspiratie &amp; advies</div><div class="s" style="font-size:42px;line-height:1;margin-top:10px">Wandpanelen voor elke ruimte</div><div style="font-size:14px;line-height:1.65;color:#3A3733;margin-top:12px">Per ruimte: decors, plaatsen en kosten.</div></div>
    <div style="padding:22px 20px 0;display:grid;grid-template-columns:1fr 1fr;gap:16px 12px">{''.join(f'<div><div style="background:#F5F2EC;border:1px solid #E2DBCF;padding:6px 4px 0">{D[k]}</div><div class="ttl" style="font-size:18px;margin-top:8px">{ti.replace("Wandpanelen in de ","").replace("Wandpanelen in het ","").replace("Wandpanelen op ","").capitalize()}</div></div>' for k, ti, _ in ROOMS)}</div>
    <div style="padding:30px 20px 0"><div class="k">Per materiaal</div></div>
    <div style="padding:12px 20px 30px;display:flex;gap:10px;overflow:hidden">{''.join(f'<div style="flex:none"><img src="{S}{f}.jpg" style="width:96px;height:96px;object-fit:cover"><div style="font-size:12px;margin-top:6px">{n}</div></div>' for f, n, _ in MAT[:4])}</div>
  </div>
  <div class="frame" style="width:390px">
    <div style="height:56px;padding:0 18px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #DDD6CA"><span>☰</span><b class="s" style="font-size:24px">PureDeco</b><span style="font-size:12px">⌕</span></div>
    <div style="padding:14px 20px 0" class="note">Home · Inspiratie · Badkamer</div>
    <div style="padding:16px 20px 0"><div class="s" style="font-size:40px;line-height:1">Wandpanelen in de badkamer</div></div>
    <div style="padding:16px 12px 0"><div style="background:#F5F2EC;border:1px solid #E2DBCF;padding:8px 6px 2px">{D["badkamer"]}</div></div>
    <div style="padding:16px 20px 0"><div class="box" style="padding:14px 16px;background:#EFEAE1"><div class="eyeb">Kort antwoord</div><div style="font-size:14px;line-height:1.65;margin-top:6px">Ja. De panelen zijn waterbestendig en komen in één stuk van 280 cm hoog…</div></div></div>
    <div style="padding:18px 20px 26px" class="toc"><a>Welke decors passen</a><a>Linea of Signature</a><a>Wat kost een badkamerwand</a><a style="border-bottom:1px solid #DDD6CA">Plaatsen, ook over tegels</a></div>
  </div>
</div>

<!-- 6 Contentplan -->
<div class="sec"><span class="num">6</span><span class="h2">Contentplan</span><span class="note">bestaande URL's blijven; nieuwe pagina's in dezelfde blog</span></div>
<table class="t" style="margin-top:22px;background:#F5F2EC">
  <tr><th>#</th><th>Pagina</th><th>URL</th><th>Titel in Google</th><th>Wat</th></tr>
  <tr><td>1</td><td><b>Inspiratie (hub)</b></td><td>/blogs/nieuws</td><td>Wandpanelen inspiratie en advies per ruimte | PureDeco</td><td>Nieuw ontwerp (thema)</td></tr>
  <tr><td>2</td><td><b>Bamboe wandpanelen: wat zijn het?</b></td><td>/blogs/nieuws/de-voordelen-van-bamboepanelen-…</td><td>Bamboe wandpanelen: opbouw, uitvoeringen en waar ze passen</td><td>Bestaand artikel herschrijven (zelfde URL), beweringen controleren</td></tr>
  <tr><td>3</td><td><b>Wandpanelen in de badkamer</b></td><td>/blogs/nieuws/wandpanelen-badkamer</td><td>Wandpanelen in de badkamer: decors, plaatsen en kosten</td><td>Nieuw</td></tr>
  <tr><td>4</td><td><b>Wandpanelen over tegels plaatsen</b></td><td>/blogs/nieuws/wandpanelen-over-tegels-plaatsen</td><td>Wandpanelen over tegels plaatsen: zo doe je dat</td><td>Nieuw</td></tr>
  <tr><td>5</td><td><b>Wandpanelen in de keuken</b></td><td>/blogs/nieuws/wandpanelen-keuken</td><td>Wandpanelen in de keuken: achterwand zonder voegen</td><td>Nieuw, met keukenproject</td></tr>
  <tr><td>6</td><td><b>Wandpanelen in het toilet</b></td><td>/blogs/nieuws/wandpanelen-toilet</td><td>Wandpanelen in het toilet: snel een nieuwe wand</td><td>Nieuw, met toiletproject</td></tr>
  <tr><td>7</td><td><b>Woonkamer</b> · <b>Slaapkamer</b> · <b>Kantoor</b></td><td>/blogs/nieuws/wandpanelen-woonkamer …</td><td>per ruimte</td><td>Nieuw (na 3–6)</td></tr>
  <tr><td>8</td><td><b>Hoeken en randen afwerken</b></td><td>/blogs/nieuws/wandpanelen-hoeken-afwerken</td><td>Wandpanelen afwerken: hoeken, randen en profielen</td><td>Nieuw, linkt naar accessoires</td></tr>
  <tr><td>9</td><td>4 projecten</td><td>bestaande URL's</td><td>Project: … | PureDeco</td><td>Opschonen: oude links, lege opsommingen, labels; uitbouw = 646 Khaki</td></tr>
  <tr><td>10</td><td>'5 Creatieve toepassingen'</td><td>/blogs/nieuws/tips-…-1</td><td>—</td><td>Kopie van onderhoud: herschrijven tot '6 plekken voor wandpanelen' (verwijst naar de gidsen) of noindex</td></tr>
</table>
<div class="note" style="margin-top:10px">Volgorde op basis van de zoekdata: 2 en 3 eerst (meeste vertoningen, slechtste positie). Teksten schrijf ik, jij keurt goed; niets gaat live zonder akkoord.</div>

<!-- 7 Technisch -->
<div class="sec"><span class="num">7</span><span class="h2">Technische SEO</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:56px;margin-top:20px">
  <ul class="l">
    <li><b>Eén H1</b> per pagina met het zoekwoord; H2's per vraag; geen kopjes voor opmaak.</li>
    <li><b>Titel en meta per gids</b> via pd-seo (zoals collecties), 50–60 en 140–160 tekens.</li>
    <li><b>Schema:</b> Article (echte datum en wijzigingsdatum, auteur PureDeco), BreadcrumbList, ItemList (decors) en FAQ-opmaak (helpt de structuur; Google toont FAQ's nog maar zelden als extra weergave).</li>
    <li><b>Interne links:</b> hub → gidsen → collecties en producten; producten en collecties linken terug naar de passende gids ('Advies voor de badkamer').</li>
    <li><b>Ankers</b> (inhoudsopgave) zodat Google per vraag kan doorlinken.</li>
  </ul>
  <ul class="l">
    <li><b>Snelheid:</b> tekeningen als code, scans 600 px in WebP, foto's alleen klein en lazy; eerste beeld is tekst (snelle LCP).</li>
    <li><b>Alt-teksten</b> beschrijvend ('Badkamerwand in 851 Travertine Ivory, tekening'), visualisaties gelabeld.</li>
    <li><b>Dubbele inhoud weg</b> (artikel 10), oude links (/product/marmer/) naar huidige collecties.</li>
    <li><b>Blognaam</b> 'Nieuws' → 'Inspiratie' (kruimelpad, RSS); URL blijft.</li>
    <li><b>Datums</b> niet meer op kaarten; wel 'bijgewerkt op' in het artikel (vertrouwen + versheid).</li>
  </ul>
</div>

<div class="box" style="padding:28px 32px;margin-top:48px">
  <div class="k">Jouw keuzes</div>
  <ol class="l">
    <li>Akkoord op deze opzet (hub + ruimtegidsen, beeldtaal met scans en tekeningen)?</li>
    <li>Mag ik starten met het thema (hub en gids-sjabloon) en de eerste twee teksten (bamboe, badkamer) als concept voor jou?</li>
    <li>Opschonen van de bestaande artikelen en de blognaam 'Inspiratie': akkoord?</li>
  </ol>
</div>

</div></div>
</x-dc>
</body>
</html>
'''
out = os.path.join(HERE, '..', 'InspiratieV2.dc.html')
open(out, 'w').write(html)
print('ok', out)
