# Maakt theme-h1/snippets/pd-vergelijk.liquid (vergelijking Puredeco met zes soorten wanden).
# Bron gegevens: openbare productinformatie NL/BE, okt 2026 (zie docs/ontwerp-puredeco-finish/Vergelijking.html) en Puredeco (14 okt 2026).
import html
def sec(kind):
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
    elif kind=='teg':
        s+=['<rect x="5" y="40" width="140" height="6" fill="#CFC8BC"/>']
        s+=[f'<rect x="{5+i*35}" y="26" width="33" height="14" fill="#EDE8E0" stroke="#B9B1A5"/>' for i in range(4)]
    elif kind=='mic':
        s+=['<rect x="5" y="34" width="140" height="12" fill="#D6D0C6"/>','<rect x="5" y="30" width="140" height="4" fill="#9E968B"/>']
    return '<svg viewBox="0 10 150 42" aria-hidden="true" focusable="false">'+''.join(s)+'</svg>'

COLS=[('pd','Puredeco','Behandeld bamboe, 5 of 8 mm'),('bam','Andere bamboepanelen','Ook bamboehoutskool'),('spc','SPC-panelen','Steen-kunststof'),('pvc','Holle PVC-panelen','Kunststof banen'),('hpl','HPL op multiplex','Badkamerpanelen'),('teg','Tegels','Keramisch'),('mic','Microcement','Naadloos stucwerk')]
DEFAULT=['bam','spc','teg']
ROWS=[
('Uitstraling','Formaat',[('g','122 × 280 cm, van vloer tot plafond'),('n','60–122 × 280 cm'),('n','Tot 122 × 280 cm, ook stroken en tegels'),('w','Banen van 25–37,5 cm'),('w','60 cm breed, 240–302 cm'),('w','Klein tot groot formaat'),('g','Naadloos')]),
('Uitstraling','Naden',[('g','Om de 122 cm; 8 mm met klik, vrijwel naadloos'),('n','Stomp, of veer-en-groef bij 8 mm'),('n','Stomp of klik'),('w','Om de 25–37,5 cm'),('w','Om de 60 cm'),('w','Voeg rond elke tegel'),('g','Geen')]),
('Uitstraling','Decor en structuur',[('g','Hoogwaardige toplaag: de nerf van hout zie én voel je'),('n','Verschilt per aanbieder'),('n','Verschilt per product'),('n','Verschilt per product'),('n','Verschilt per product'),('g','Echte keramiek'),('n','Hangt af van de stukadoor')]),
('Uitstraling','Doorlopend marmer',[('g','Ja, de tekening loopt over drie panelen'),('w','Niet gevonden'),('n','Verschilt per product'),('w','Nee'),('w','Nee'),('n','Bij grote tegels'),('w','Nee')]),
('Materiaal','Opbouw',[('g','Toplaag van gerecycled PVC op een dichte, stevige kern van behandeld bamboe'),('n','Bamboe- of bamboehoutskoolvezel, vaak met PVC en kalk; verschilt per aanbieder'),('n','Steenpoeder met PVC'),('w','Hol PVC-profiel met kamers'),('g','HPL op watervast multiplex'),('g','Keramiek op lijm'),('n','Cementgebonden laag')]),
('Materiaal','Dikte',[('g','5 of 8 mm'),('n','Meestal 5 mm, soms 8 mm'),('n','3–4 mm; oneffenheden kunnen doordrukken'),('n','5–10 mm'),('n','10–11 mm'),('n','Tegel en lijmbed'),('g','Dunne laag')]),
('Gebruik','Badkamer en keuken',[('g','Ja, waterbestendig door de behandelde kern'),('g','Ja, volgens aanbieder'),('g','Ja'),('n','Ja, naden afkitten'),('g','Ja'),('g','Ja'),('n','Ja, met topcoat')]),
('Gebruik','Ronde wand',[('g','Ja, infrezen en verwarmen'),('n','Soms, volgens aanbieder'),('w','Nee'),('w','Niet opgegeven'),('w','Nee'),('n','Kleine tegels of mozaïek'),('g','Ja, volgt de wand')]),
('Gebruik','Brandklasse (opgegeven)',[('g','B1'),('n','B1 of "brandvertragend"'),('w','Meestal niet opgegeven'),('w','Meestal niet opgegeven'),('n','D-s1,d0'),('g','A1, onbrandbaar'),('w','Niet opgegeven')]),
('Plaatsen','Tillen en plaatsen',[('g','Licht: geen zware platen of tegels tillen'),('n','Verschilt per aanbieder'),('n','Steenpoeder maakt het zwaarder per mm'),('g','Licht'),('n','± 8 kg per m²'),('w','Zwaar, plus lijm en voegsel'),('n','Geen panelen; natte verwerking')]),
('Plaatsen','Over bestaande tegels',[('g','Ja, lijmen zonder breekwerk'),('g','Ja'),('g','Ja, op een vlakke wand'),('n','Lijmen of op regelwerk'),('g','Ja, lijmen of regelwerk'),('w','Slopen, of erover tegelen met lijm en voegen'),('n','Met voorbereiding')]),
('Plaatsen','Wie plaatst',[('g','Zelf, met montagekit'),('g','Zelf'),('g','Zelf'),('g','Zelf'),('g','Zelf of vakman'),('w','Meestal een tegelzetter'),('w','Stukadoor')]),
('Kosten en service','Indicatie per m²',[('n','€ 26–53, materiaal'),('n','€ 20–60, materiaal'),('n','€ 24–50, materiaal'),('n','€ 21–43, materiaal'),('n','± € 70–90, materiaal'),('w','€ 45–155, incl. plaatsen'),('w','€ 120–150, incl. plaatsen')]),
('Kosten en service','Stalen en advies',[('g','Tot 5 stalen gratis, Studio Herwen op afspraak'),('n','Verschilt per aanbieder'),('n','Verschilt per aanbieder'),('n','Verschilt per aanbieder'),('n','Verschilt per aanbieder'),('n','Verschilt per aanbieder'),('n','Verschilt per aanbieder')]),
]
LAB={'g':'sterk','n':'verschilt of gemiddeld','w':'minder'}
e=html.escape
def cls(c):
    return 'pv-c'+(' is-pd' if c=='pd' else '')+('' if c=='pd' or c in DEFAULT else ' is-off')
out=[]
out.append('''{%- comment -%}
  Puredeco · vergelijking met zes soorten wanden (artboard Vergelijking, 14 okt 2026). Gegenereerd door tools/vergelijking/maak_snippet.py; pas daar aan.
  Gegevens: openbare productinformatie van aanbieders in NL/BE (okt 2026), soorten en geen merken. Puredeco: bevestigd door Puredeco
  (toplaag gerecycled PVC, kern behandeld bamboe, licht, dichte kern, hoogwaardige toplaag, B1, 8 mm klik).
  Desktop: Puredeco + 3 gekozen soorten (of alle zeven). Mobiel: Puredeco + 1 soort, rij voor rij.
{%- endcomment -%}
<section class="ph-s pv" aria-labelledby="pv-h" data-pv>
  <div class="ph-wrap">
    <div class="pv-head">
      <div><p class="ph-k ph-k--bronze">Vergelijken</p><h2 class="ph-h2 pv-h" id="pv-h">Puredeco naast de wanden waar je tussen twijfelt</h2></div>
      <p class="pv-lead">Zeven soorten wanden naast elkaar. Geen merken, wel de gegevens die aanbieders zelf opgeven.</p>
    </div>
    <div class="pv-bar" role="group" aria-label="Kies waarmee je Puredeco vergelijkt">
      <span class="pv-bar__l">Vergelijk met</span>''')
for k,n,sub in COLS[1:]:
    out.append(f'<button type="button" class="pv-chip" data-pv-col="{k}" aria-pressed="{"true" if k in DEFAULT else "false"}"><span class="pv-chip__i">{sec(k)}</span>{e(n)}</button>')
out.append('<button type="button" class="pv-all" data-pv-all aria-pressed="false">Alle zeven tonen</button>\n    </div>')
out.append('    <div class="pv-scroll"><table class="pv-t">\n      <thead><tr><th class="pv-lbl" scope="col"><span class="visually-hidden">Kenmerk</span></th>')
for k,n,sub in COLS:
    out.append(f'<th class="{cls(k)}" data-c="{k}" scope="col"><span class="pv-mini">{sec(k)}</span><b>{e(n)}</b><small>{e(sub)}</small></th>')
out.append('</tr></thead>\n      <tbody>')
grp=None
for g,lab,vals in ROWS:
    if g!=grp:
        out.append(f'<tr class="pv-grp"><th colspan="{len(DEFAULT)+2}" scope="colgroup">{e(g)}</th></tr>'); grp=g
    row=f'<tr><th class="pv-lbl" scope="row">{e(lab)}</th>'
    for (k,_,_),(st,txt) in zip(COLS,vals):
        row+=f'<td class="{cls(k)}" data-c="{k}"><i class="pv-st pv-st--{st}" role="img" aria-label="{LAB[st]}"></i>{e(txt)}</td>'
    out.append(row+'</tr>')
out.append('''      </tbody>
    </table></div>
    <p class="pv-legend"><span><i class="pv-st pv-st--g"></i>sterk</span><span><i class="pv-st pv-st--n"></i>verschilt of gemiddeld</span><span><i class="pv-st pv-st--w"></i>minder</span></p>
    <p class="pv-src">Bron: openbare productinformatie van aanbieders in Nederland en België, oktober 2026. Algemene kenmerken van soorten wanden, geen merken. Prijzen zijn indicaties voor materiaal, of inclusief plaatsen waar dat staat. Brandklasse zoals opgegeven door de aanbieder.</p>
  </div>
</section>
<script>
(function(){
  var r=document.querySelector('[data-pv]'); if(!r) return;
  var mq=window.matchMedia('(max-width: 749px)'); var sel=''' + repr(DEFAULT).replace("'",'"') + '''; var all=false;
  function shown(){ if(mq.matches) return sel.slice(0,1); return all?null:sel.slice(-3); }
  function apply(){
    var s=shown();
    r.querySelectorAll('[data-c]').forEach(function(el){ var c=el.getAttribute('data-c'); el.classList.toggle('is-off', c!=='pd' && s!==null && s.indexOf(c)<0); });
    r.querySelectorAll('[data-pv-col]').forEach(function(b){ var c=b.getAttribute('data-pv-col'); b.setAttribute('aria-pressed', (s===null||s.indexOf(c)>-1)?'true':'false'); });
    var a=r.querySelector('[data-pv-all]'); if(a){ a.setAttribute('aria-pressed', all?'true':'false'); a.textContent= all?'Drie tonen':'Alle zeven tonen'; }
    r.classList.toggle('is-all', all && !mq.matches);
    var n=(s===null?6:s.length)+2; r.querySelectorAll('.pv-grp th').forEach(function(th){ th.colSpan=n; });
  }
  r.addEventListener('click',function(ev){
    var b=ev.target.closest('[data-pv-col]');
    if(b){ var c=b.getAttribute('data-pv-col'); all=false;
      if(mq.matches){ sel=[c].concat(sel.filter(function(x){return x!==c;})); }
      else { var i=sel.indexOf(c); if(i>-1){ if(sel.length>1) sel.splice(i,1); } else { sel.push(c); if(sel.length>3) sel.shift(); } }
      apply(); return; }
    if(ev.target.closest('[data-pv-all]')){ all=!all; apply(); }
  });
  if(mq.addEventListener) mq.addEventListener('change',apply); else if(mq.addListener) mq.addListener(apply);
  apply();
})();
</script>
''')
open('/home/user/baet/theme-h1/snippets/pd-vergelijk.liquid','w').write('\n'.join(out))
print('ok')
