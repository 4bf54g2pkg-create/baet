# Maakt theme-h1/snippets/pd-waarom.liquid: compacte vergelijking (drie kaarten) voor de homepage.
src=open('/home/user/baet/tools/vergelijking/maak_snippet.py').read().split("COLS=")[0]
ns={}; exec(src,ns); sec=ns['sec']
CARDS=[('teg','tegels','Geen tegels. Geen breekwerk.','Eén paneel van 122 × 280 cm gaat direct op de bestaande wand. Licht genoeg om zelf te tillen, klaar zonder tegelzetter.'),
('hpl','smalle panelen','Geen naad om de 60 cm of 1 meter.','Onze panelen zijn 122 cm breed: minder naden, een rustigere wand. In 8 mm met klik sluiten ze vrijwel naadloos aan.'),
('pvc','hol kunststof','Een kern met een hoge dichtheid.','Behandeld bamboe: dicht en stevig, en toch licht. Waterbestendig en te buigen voor een ronde wand.'),
('spc','SPC-panelen','Ziet eruit als echt. Voelt ook zo.','Hout, leer, Japandi-stof, travertin: hoogwaardige toplagen met een structuur die je voelt. Bij hout volg je de nerf met je vingers. Die keuze vind je bij SPC niet.')]
out=['''{%- comment -%}
  Puredeco · waarom Puredeco, kort en krachtig (14 okt 2026). Feiten Puredeco: 122 cm breed (andere panelen vaak 60 cm of 1 m), kern met hoge dichtheid, toplagen hout/leer/stof die je ziet en voelt (bij SPC niet beschikbaar). Gegenereerd door tools/vergelijking/maak_waarom.py.
  Alleen feiten die kloppen: geen merken, geen "beter dan". De volledige vergelijking staat in snippets/pd-vergelijk.liquid (voor een aparte pagina).
{%- endcomment -%}
<section class="ph-s pw" aria-labelledby="pw-h">
  <div class="ph-wrap">
    <div class="pw-head">
      <div><p class="ph-k ph-k--bronze">Waarom Puredeco</p><h2 class="ph-h2 pw-h" id="pw-h">Alles wat een wand moet zijn. In één paneel.</h2></div>
      <a class="pw-cta" href="/pages/sample">Voel het verschil: bestel gratis stalen →</a>
    </div>
    <div class="pw-cards">''']
for k,alt,t,d in CARDS:
    out.append(f'''      <article class="pw-card">
        <div class="pw-vs" aria-hidden="true"><span class="pw-vs__me">{sec("pd")}</span><i>vs</i><span>{sec(k)}</span></div>
        <p class="pw-alt">In plaats van {alt}</p>
        <h3 class="pw-t">{t}</h3>
        <p class="pw-d">{d}</p>
      </article>''')
out.append('''    </div>
  </div>
</section>
''')
open('/home/user/baet/theme-h1/snippets/pd-waarom.liquid','w').write('\n'.join(out))
