# Maakt theme-h1/snippets/pd-waarom.liquid: compacte vergelijking (drie kaarten) voor de homepage.
src=open('/home/user/baet/tools/vergelijking/maak_snippet.py').read().split("COLS=")[0]
ns={}; exec(src,ns); sec=ns['sec']
CARDS=[('teg','Tegels','Geen tegels. Geen breekwerk.','Eén paneel van 122 × 280 cm gaat direct op de bestaande wand. Licht genoeg om zelf te tillen, klaar zonder tegelzetter.'),
('pvc','Hol kunststof of SPC-panelen','Geen hol kunststof. Echt bamboe.','Een dichte kern van behandeld bamboe, onder een toplaag waarvan je de nerf ziet én voelt. Stevig, waterbestendig en toch licht.'),
('hpl','Badkamerpanelen van 60 cm','Geen naad om de 60 cm.','122 cm breed: de helft minder naden. In 8 mm met klik vrijwel naadloos, en te buigen voor een ronde wand.')]
out=['''{%- comment -%}
  Puredeco · waarom Puredeco, kort en krachtig (14 okt 2026, na "kort maar krachtig"). Gegenereerd door tools/vergelijking/maak_waarom.py.
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
        <p class="pw-alt">In plaats van {alt[0].lower()+alt[1:]}</p>
        <h3 class="pw-t">{t}</h3>
        <p class="pw-d">{d}</p>
      </article>''')
out.append('''    </div>
  </div>
</section>
''')
open('/home/user/baet/theme-h1/snippets/pd-waarom.liquid','w').write('\n'.join(out))
