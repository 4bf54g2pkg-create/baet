# Artboard "Vergelijking op topniveau"
# Mini-doorsneden (schematisch) per wandtype
def sec(kind):
    W,H=150,64
    s=[]
    if kind=='pd':
        s+=['<rect x="5" y="20" width="140" height="5" fill="#6A4E3A"/>','<rect x="5" y="25" width="140" height="22" fill="#D9C38F"/>']
        s+=[f'<path d="M5 {27+i*4}H145" stroke="#C2A96F" stroke-width=".7"/>' for i in range(5)]
    elif kind=='bam':
        s+=['<rect x="5" y="22" width="140" height="3" fill="#8A7A6A"/>','<rect x="5" y="25" width="140" height="13" fill="#B7B0A4"/>']
        s+=[f'<circle cx="{10+(i*13)%135}" cy="{28+(i*7)%8}" r="1" fill="#6E675E"/>' for i in range(22)]
    elif kind=='spc':
        s+=['<rect x="5" y="24" width="140" height="2" fill="#8A7A6A"/>','<path d="M5 26H135V29H141V33H135V36H5Z" fill="#9C9A96"/>']
    elif kind=='pvc':
        s+=['<rect x="5" y="20" width="140" height="20" fill="none" stroke="#9C9A96" stroke-width="2"/>']
        s+=[f'<path d="M{5+i*14} 20V40" stroke="#9C9A96" stroke-width="1.5"/>' for i in range(1,10)]
    elif kind=='hpl':
        s+=['<rect x="5" y="16" width="140" height="3" fill="#3A3733"/>']
        s+=[f'<rect x="5" y="{19+i*4}" width="140" height="4" fill="{"#E3C99A" if i%2 else "#CDAE78"}"/>' for i in range(7)]
        s+=['<path d="M145 25h4v8h-4" fill="#CDAE78"/>']
    elif kind=='teg':
        s+=['<rect x="5" y="40" width="140" height="6" fill="#CFC8BC"/>']
        s+=[f'<rect x="{5+i*35}" y="26" width="33" height="14" fill="#EDE8E0" stroke="#B9B1A5"/>' for i in range(4)]
    elif kind=='mic':
        s+=['<rect x="5" y="34" width="140" height="12" fill="#D6D0C6"/>','<rect x="5" y="30" width="140" height="4" fill="#9E968B"/>']
    s.append('<path d="M5 52H145" stroke="#151413" stroke-width=".6" stroke-dasharray="3 3"/>' if kind not in('teg','mic') else '<path d="M5 46H145" stroke="#151413" stroke-width=".6"/>')
    return f'<svg viewBox="0 0 {W} {H}" aria-hidden="true">'+''.join(s)+'</svg>'

COLS=[('pd','Puredeco','Bamboe, 5 of 8 mm'),('bam','Andere bamboepanelen','Ook bamboehoutskool'),('spc','SPC-panelen','Steen-kunststof'),('pvc','Holle PVC-panelen','Kunststof banen'),('hpl','HPL op multiplex','Badkamerpanelen'),('teg','Tegels','Keramisch'),('mic','Microcement','Naadloos stucwerk')]
# status: g = sterk, n = neutraal/verschilt, w = zwak
ROWS=[
('Uitstraling','Formaat',[('g','122 × 280 cm, van vloer tot plafond'),('n','60–122 × 280 cm'),('n','Tot 122 × 280 cm, ook stroken en tegels'),('w','Banen van 25–37,5 cm'),('w','60 cm breed, 240–302 cm'),('w','Klein tot groot formaat'),('g','Naadloos')]),
('Uitstraling','Naden',[('g','Om de 122 cm. 8 mm met klik: vrijwel naadloos'),('n','Stomp, of veer-en-groef bij 8 mm'),('n','Stomp of klik'),('w','Om de 25–37,5 cm'),('w','Om de 60 cm'),('w','Voeg rond elke tegel'),('g','Geen')]),
('Uitstraling','Doorlopend marmer',[('g','Ja, de tekening loopt over drie panelen'),('w','Niet gevonden'),('n','Verschilt per product'),('w','Nee'),('w','Nee'),('n','Bij grote tegels'),('w','Nee')]),
('Materiaal','Opbouw',[('g','Toplaag van gerecycled PVC, kern van behandeld bamboe'),('n','Bamboe- of bamboehoutskoolvezel, vaak met PVC en kalk; verschilt per aanbieder'),('n','Steenpoeder met PVC'),('w','Hol PVC-profiel met kamers'),('g','HPL op watervast multiplex'),('g','Keramiek op lijm'),('n','Cementgebonden laag')]),
('Materiaal','Dikte',[('g','5 of 8 mm'),('n','Meestal 5 mm, soms 8 mm'),('n','3–4 mm'),('n','5–10 mm'),('n','10–11 mm'),('n','Tegel en lijmbed'),('g','Dunne laag')]),
('Gebruik','Badkamer en keuken',[('g','Ja, waterbestendig'),('g','Ja, volgens aanbieder'),('g','Ja'),('n','Ja, naden afkitten'),('g','Ja'),('g','Ja'),('n','Ja, met topcoat')]),
('Gebruik','Ronde wand',[('g','Ja, infrezen en verwarmen'),('n','Soms, volgens aanbieder'),('w','Nee'),('w','Niet opgegeven'),('w','Nee'),('n','Kleine tegels of mozaïek'),('g','Ja, volgt de wand')]),
('Gebruik','Brandklasse (opgegeven)',[('g','B1'),('n','B1 of "brandvertragend"'),('w','Meestal niet opgegeven'),('w','Meestal niet opgegeven'),('n','D-s1,d0'),('g','A1, onbrandbaar'),('w','Niet opgegeven')]),
('Plaatsen','Over bestaande tegels',[('g','Ja, lijmen zonder breekwerk'),('g','Ja'),('g','Ja, op een vlakke wand'),('n','Lijmen of op regelwerk'),('g','Ja, lijmen of regelwerk'),('w','Slopen, of erover tegelen met lijm en voegen'),('n','Met voorbereiding')]),
('Plaatsen','Wie plaatst',[('g','Zelf, met montagekit'),('g','Zelf'),('g','Zelf'),('g','Zelf'),('g','Zelf of vakman'),('w','Meestal een tegelzetter'),('w','Stukadoor')]),
('Kosten','Indicatie per m²',[('g','€ 26–53, materiaal'),('n','€ 20–60, materiaal'),('n','€ 24–50, materiaal'),('n','€ 21–43, materiaal'),('n','± € 70–90, materiaal'),('w','€ 45–155, incl. plaatsen'),('w','€ 120–150, incl. plaatsen')]),
]
ICON={'g':'<i class="st st-g" title="sterk"></i>','n':'<i class="st st-n" title="verschilt"></i>','w':'<i class="st st-w" title="minder"></i>'}

def matrix(cols_idx, compact=False):
    cls='mx all' if len(cols_idx)>5 else 'mx'
    head='<tr><th class="lbl"></th>'+''.join(f'<th class="{"pd" if i==0 else ""}"><div class="mini">{sec(COLS[i][0])}</div><b>{COLS[i][1]}</b><span>{COLS[i][2]}</span></th>' for i in cols_idx)+'</tr>'
    body=''; grp=None
    for g,lab,vals in ROWS:
        if g!=grp:
            body+=f'<tr class="grp"><td colspan="{len(cols_idx)+1}">{g}</td></tr>'; grp=g
        body+=f'<tr><th class="lbl">{lab}</th>'+''.join(f'<td class="{"pd" if i==0 else ""}">{ICON[vals[i][0]]}<span>{vals[i][1]}</span></td>' for i in cols_idx)+'</tr>'
    return f'<table class="{cls}">{head}{body}</table>'

chips=''.join(f'<span class="chip{" on" if i in (1,2,5) else ""}">{sec(c[0])}{c[1]}</span>' for i,c in enumerate(COLS) if i>0)

mobile_rows=''.join(f'<div class="mr"><p class="ml">{lab}</p><div class="mc"><div class="pd">{ICON[v[0][0]]}{v[0][1]}</div><div>{ICON[v[2][0]]}{v[2][1]}</div></div></div>' for g,lab,v in ROWS[:8])

html=f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>Vergelijking op topniveau</title><style>
@font-face{{font-family:'Cormorant';src:url('../../tools/banners/cormorant.woff2') format('woff2');font-weight:300 700}}
@font-face{{font-family:'Instrument Sans';src:url('../../tools/banners/instrument.woff2') format('woff2');font-weight:400 700}}
*{{box-sizing:border-box}}body{{margin:0;background:#DCD5CA;font-family:'Instrument Sans',Arial,sans-serif;color:#151413}}
.board{{width:1600px;margin:0 auto;padding:56px;background:#F5F2EC}}
.k{{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A;margin:0}}
h1{{font-family:Cormorant,Georgia,serif;font-weight:500;font-size:60px;line-height:1;margin:10px 0 0}}
h2{{font-family:Cormorant,Georgia,serif;font-weight:500;font-size:36px;line-height:1.08;margin:8px 0 10px}}
p,li{{font-size:14.5px;line-height:1.7;color:#3A3733}}
.lead{{max-width:1100px;font-size:16px}}
.sec{{margin-top:64px;display:grid;grid-template-columns:330px 1fr;gap:44px;align-items:start}}
.num{{font-family:Cormorant,Georgia,serif;font-size:54px;color:#8C6A4A;line-height:1}}
.frame{{background:#fff;border:1px solid #DDD6CA;box-shadow:0 18px 40px rgba(21,20,19,.08);position:relative}}
.tag{{position:absolute;top:-11px;left:16px;background:#151413;color:#F5F2EC;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;padding:4px 9px;z-index:2}}
/* het blok zelf */
.blk{{padding:56px 56px 40px;background:#FBF9F5}}
.blk h3{{font-family:Cormorant,Georgia,serif;font-weight:500;font-size:48px;line-height:1.04;margin:10px 0 0;max-width:760px}}
.blk .in{{display:flex;justify-content:space-between;align-items:end;gap:40px}}
.blk .in p{{max-width:430px;margin:0}}
.cbar{{display:flex;align-items:center;gap:10px;margin:30px 0 22px;flex-wrap:wrap}}
.cbar .l{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#6E675E;margin-right:6px}}
.chip{{display:inline-flex;align-items:center;gap:8px;border:1px solid #DDD6CA;background:#fff;padding:6px 12px 6px 6px;font-size:13px;border-radius:999px;color:#3A3733}}
.chip svg{{width:44px;height:19px;background:#F5F2EC;border-radius:999px}}
.chip.on{{border-color:#151413;color:#151413;box-shadow:inset 0 0 0 1px #151413}}
.chip.all{{padding:6px 14px;text-decoration:underline;border:0;background:none}}
.mx{{width:100%;border-collapse:separate;border-spacing:0;font-size:13.5px;table-layout:fixed}}.mx.all{{font-size:12.5px}}.mx.all td,.mx.all th{{overflow-wrap:anywhere;hyphens:auto}}.mx.all th.lbl{{width:120px}}.mx.all th,.mx.all td{{padding:11px 10px}}.mx.all tr:first-child th b{{font-size:18px}}
.mx th,.mx td{{text-align:left;vertical-align:top;padding:13px 16px;border-bottom:1px solid #E7E1D6}}
.mx thead th,.mx tr:first-child th{{border-bottom:1px solid #151413;padding-bottom:16px;vertical-align:bottom}}
.mx tr:first-child th b{{display:block;font-family:Cormorant,Georgia,serif;font-weight:500;font-size:22px;line-height:1.1;margin-top:10px}}
.mx tr:first-child th span{{display:block;font-size:12px;color:#6E675E;font-weight:400;margin-top:2px}}
.mini svg{{width:100%;max-width:150px;height:auto;display:block}}
.mx th.lbl{{width:190px;font-weight:600;color:#151413}}
.mx td span{{display:block;padding-left:18px;line-height:1.45}}
.st{{display:inline-block;width:10px;height:10px;border-radius:50%;vertical-align:-1px;margin-right:4px}}
.st-g{{background:#2F6B4F}}.st-n{{background:linear-gradient(90deg,#B08A3E 50%,transparent 50%);box-shadow:inset 0 0 0 1.5px #B08A3E}}.st-w{{box-shadow:inset 0 0 0 1.5px #B9B1A5}}
.mx td .st{{position:absolute;margin-top:4px}}.mx td{{position:relative}}
.mx .pd{{background:#fff;box-shadow:inset 1px 0 0 #E7E1D6,inset -1px 0 0 #E7E1D6}}
.mx tr:first-child th.pd{{background:#151413;color:#F5F2EC;border-top:3px solid #8C6A4A}}
.mx tr:first-child th.pd span{{color:#C9BFAF}}
.mx tr:first-child th.pd .mini svg{{background:#F5F2EC}}
.mx td.pd{{font-weight:500;color:#151413}}
.grp td{{padding:22px 16px 8px !important;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#8C6A4A;border-bottom:0 !important;background:transparent !important;box-shadow:none !important}}
.legend{{display:flex;gap:22px;margin-top:16px;font-size:12.5px;color:#6E675E}}
.src{{margin-top:10px;font-size:12px;color:#6E675E;max-width:1100px}}
/* mobiel */
.phone{{width:390px;border:10px solid #151413;border-radius:38px;overflow:hidden;background:#FBF9F5}}
.phone .pb{{padding:28px 18px}}
.phone h3{{font-family:Cormorant,Georgia,serif;font-weight:500;font-size:32px;line-height:1.05;margin:8px 0 14px}}
.phone .sel{{display:flex;gap:8px;overflow:hidden;margin:4px -18px 16px;padding:0 18px}}
.phone .sel .chip{{white-space:nowrap;font-size:12px}}
.phone .hd{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:6px}}
.phone .hd div{{padding:10px;background:#fff;border:1px solid #E7E1D6;font-family:Cormorant,Georgia,serif;font-size:19px}}
.phone .hd div.pd{{background:#151413;color:#F5F2EC;border-top:3px solid #8C6A4A}}
.phone .hd svg{{width:100%;height:auto;display:block;background:#F5F2EC;margin-bottom:6px}}
.mr{{border-bottom:1px solid #E7E1D6;padding:10px 0}}
.ml{{margin:0 0 4px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8C6A4A}}
.mc{{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:12.5px;line-height:1.4}}
.mc .pd{{font-weight:600}}
.facts{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.card{{background:#fff;border:1px solid #DDD6CA;padding:18px 20px}}
.card b{{display:block;font-family:Cormorant,Georgia,serif;font-weight:500;font-size:22px;margin-bottom:6px}}
.card ul{{margin:0;padding-left:18px}}.card li{{font-size:13.5px;line-height:1.6}}
.ask{{margin-top:60px;padding:26px 30px;background:#EFEAE1;border:1px solid #DDD6CA}}
.ask li{{font-size:14.5px;line-height:1.8}}
.dont{{color:#9B3D2E}}
</style></head><body><div class="board">
<p class="k">Artboard · voorstel · nog niets aangepast · alleen H1-test</p>
<h1>De vergelijking, op topniveau</h1>
<p class="lead">De huidige tabel is te kaal en te smal: vier soorten wanden, platte tekst en geen bron. Dit voorstel vergelijkt Puredeco met zes alternatieven waar een klant echt tussen twijfelt, waaronder SPC-panelen en andere bamboepanelen. Elke wand krijgt een kleine doorsnede, de rijen zijn gegroepeerd en een bolletje laat in één oogopslag zien waar een wand sterk is. Alle gegevens komen uit openbare productinformatie van aanbieders in Nederland en België (oktober 2026). We noemen soorten, geen merken. Zo is de vergelijking eerlijk én juridisch veilig.</p>

<section class="sec">
  <div><div class="num">01</div><h2>Desktop: kies waarmee je vergelijkt</h2>
    <p>Puredeco staat altijd links, als donkere kaart. Daarnaast drie alternatieven, standaard de drie waar klanten het meest tussen twijfelen: andere bamboepanelen, SPC en tegels. Met de knoppen wissel je, of je toont alle zeven.</p>
    <p>Bolletjes: <i class="st st-g"></i>sterk, <i class="st st-n"></i>verschilt of gemiddeld, <i class="st st-w"></i>minder. Ook bij Puredeco zijn ze eerlijk: tegels zijn bijvoorbeeld onbrandbaar.</p>
    <p>Rijen in vier groepen: uitstraling, materiaal, gebruik, plaatsen en kosten.</p></div>
  <div class="frame"><span class="tag">Homepage · onder "Het verschil zit vanbinnen"</span>
    <div class="blk">
      <div class="in"><div><p class="k">Vergelijken</p><h3>Puredeco naast de wanden waar je tussen twijfelt</h3></div><p>Zeven soorten wanden naast elkaar. Geen merken, wel de gegevens die aanbieders zelf opgeven.</p></div>
      <div class="cbar"><span class="l">Vergelijk met</span>{chips}<span class="chip all">Alle zeven tonen</span></div>
      {matrix([0,1,2,5])}
      <div class="legend"><span><i class="st st-g"></i>sterk</span><span><i class="st st-n"></i>verschilt of gemiddeld</span><span><i class="st st-w"></i>minder</span></div>
      <p class="src">Bron: openbare productinformatie van aanbieders in Nederland en België, oktober 2026. Algemene kenmerken van soorten wanden, geen merken. Prijzen zijn indicaties voor materiaal, of inclusief plaatsen waar dat staat. Brandklasse zoals opgegeven door de aanbieder.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div><div class="num">02</div><h2>Alle zeven naast elkaar</h2>
    <p>Na een klik op "Alle zeven tonen". Ook bruikbaar als losse pagina "Wandbekleding vergelijken", goed voor Google ("SPC of bamboe wandpanelen", "wandpanelen of tegels").</p></div>
  <div class="frame" style="overflow:hidden"><div class="blk" style="padding:30px">{matrix(list(range(7)))}</div></div>
</section>

<section class="sec">
  <div><div class="num">03</div><h2>Mobiel: één tegen één</h2>
    <p>Geen tabel om opzij te schuiven. Je kiest bovenaan één alternatief en ziet Puredeco en die wand als twee kolommen, rij voor rij.</p></div>
  <div style="display:flex;gap:40px;align-items:flex-start">
    <div class="phone"><div class="pb"><p class="k">Vergelijken</p><h3>Puredeco naast de wanden waar je tussen twijfelt</h3>
      <div class="sel">{''.join(f'<span class="chip{" on" if i==2 else ""}">{c[1]}</span>' for i,c in enumerate(COLS) if i>0)}</div>
      <div class="hd"><div class="pd">{sec('pd')}Puredeco</div><div>{sec('spc')}SPC-panelen</div></div>
      {mobile_rows}
    </div></div>
    <div class="facts" style="flex:1;grid-template-columns:1fr">
      <div class="card"><b>Wat het onderzoek liet zien</b><ul>
        <li><b style="display:inline;font-family:inherit;font-size:inherit">Andere bamboepanelen</b> claimen vaak hetzelfde als Puredeco: 122 × 280 cm, waterbestendig, B1, buigbaar. Daar kunnen we dus niet "beter" zeggen zonder bewijs.</li>
        <li>Wel aantoonbaar anders bij Puredeco: <b style="display:inline;font-family:inherit;font-size:inherit">8 mm met klik in de volle breedte van 122 cm</b> (bij anderen vonden we 8 mm alleen in 60 of 110 cm breed), <b style="display:inline;font-family:inherit;font-size:inherit">doorlopend marmer</b> over drie panelen, gratis stalen en Studio Herwen.</li>
        <li>Veel "bamboo charcoal"-panelen hebben volgens fabrieksopgaven een kern van vooral PVC en kalk, met wat bamboehoutskool. Als Puredeco een échte bamboekern heeft, is dat hét verschil, maar dan willen we een datasheet als bewijs.</li>
        <li>SPC is 3–4 mm dun: een oneffen ondergrond kan doordrukken. HPL op multiplex heeft om de 60 cm een naad. Tegels zijn onbrandbaar (A1) maar vragen een tegelzetter.</li>
      </ul></div>
      <div class="card"><b>Wat we bewust niet doen</b><ul>
        <li class="dont">Geen merknamen van concurrenten.</li>
        <li class="dont">Geen "beter dan de rest", "uniek" of "de beste" zonder bewijs. Dat mag niet bij vergelijkende reclame en het kost vertrouwen.</li>
        <li class="dont">Geen prijzen per merk; alleen bandbreedtes per soort, met datum.</li>
      </ul></div>
    </div>
  </div>
</section>

<div class="ask"><p class="k">Graag jouw akkoord en input</p><h2 style="font-size:30px">Om Puredeco écht als beste neer te zetten</h2><ol>
<li><b>Akkoord op 01–03</b>: ik bouw de vergelijking zo in H1-test (homepage, en desgewenst een losse pagina "Wandbekleding vergelijken").</li>
<li><b>Wat is aantoonbaar beter dan andere bamboepanelen?</b> Bijvoorbeeld: aandeel bamboe in de kern, dikte van de toplaag, dichtheid of gewicht per paneel, krasvastheid, UV-bestendigheid. Met een datasheet van je producent zet ik die cijfers in een extra rij. Dan kan de vergelijking wél laten zien waarom Puredeco beter is.</li>
<li><b>B1-testrapport</b> (DIN 4102-1): met het rapport erbij is B1 hard bewijs en geen claim meer. Andere aanbieders publiceren dat niet.</li>
<li><b>8 mm Signature</b>: is het een klik- of een veer-en-groefverbinding? Een verkooppunt noemt het veer-en-groef; op de site staat klik. Dit moet overal hetzelfde zijn.</li>
</ol></div>
</div></body></html>'''
open('/home/user/baet/docs/ontwerp-puredeco-finish/Vergelijking.html','w').write(html)
