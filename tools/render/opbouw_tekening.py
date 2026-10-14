# Twee lagen, trapsgewijs: kern van behandeld bamboe (vol) met daarop de toplaag van gerecycled PVC (korter)
def svg():
    W,D,Dv=560,170,90
    x0,base=20,250
    o=[]
    # kern
    t=46; w=W; yt=base-t
    o.append(f'<rect x="{x0}" y="{yt}" width="{w}" height="{t}" fill="#C8B07A"/>')
    for k in range(1,12): o.append(f'<path d="M{x0} {yt+k*3.8:.1f}H{x0+w}" stroke="#B89E66" stroke-width=".6"/>')
    o.append(f'<polygon points="{x0+w},{yt} {x0+w+D},{yt-Dv} {x0+w+D},{yt-Dv+t} {x0+w},{yt+t}" fill="#B0965F"/>')
    o.append(f'<polygon points="{x0},{yt} {x0+w},{yt} {x0+w+D},{yt-Dv} {x0+D},{yt-Dv}" fill="#D9C38F"/>')
    for k in range(1,24):
        a=k/24; o.append(f'<path d="M{x0+D*a:.1f} {yt-Dv*a:.1f}L{x0+w+D*a:.1f} {yt-Dv*a:.1f}" stroke="#C6AD73" stroke-width=".8"/>')
    core_anchor=(x0+w-95+D/2, yt-Dv/2)
    # toplaag
    t2=10; w2=W-200; yt2=yt-t2
    o.append(f'<rect x="{x0}" y="{yt2}" width="{w2}" height="{t2}" fill="#57402F"/>')
    o.append(f'<polygon points="{x0+w2},{yt2} {x0+w2+D},{yt2-Dv} {x0+w2+D},{yt2-Dv+t2} {x0+w2},{yt2+t2}" fill="#4A3628"/>')
    o.append(f'<polygon points="{x0},{yt2} {x0+w2},{yt2} {x0+w2+D},{yt2-Dv} {x0+D},{yt2-Dv}" fill="#6A4E3A"/>')
    for k in range(1,26):
        a=k/26; o.append(f'<path d="M{x0+w2*a:.1f} {yt2}L{x0+w2*a+D:.1f} {yt2-Dv}" stroke="#80604A" stroke-width="{0.6+0.6*(k%4==0)}" opacity=".75"/>')
    top_anchor=(x0+w2/2+D/2, yt2-Dv/2)
    for n,(ax,ay) in ((1,top_anchor),(2,core_anchor)):
        o.append(f'<g class="pd-op__n"><circle cx="{ax:.0f}" cy="{ay:.0f}" r="15"/><text x="{ax:.0f}" y="{ay+5:.0f}" text-anchor="middle">{n}</text></g>')
    return f'<svg class="pd-op__svg" viewBox="10 {yt2-Dv-10} {W+D+20} {base-(yt2-Dv-10)+10}" role="img" aria-label="Opbouw van een Puredeco-wandpaneel: toplaag van gerecycled PVC met het decor, op een kern van behandeld bamboe">'+''.join(o)+'</svg>'
s=svg()
liquid='''{%- comment -%}
  Puredeco · opbouw van een wandpaneel (rapport Exclusief, 14 okt 2026).
  Feit van Puredeco: toplaag van gerecycled PVC met het decor; kern van behandeld bamboe. Door de behandeling is de kern waterbestendig.
  Gebruik: {% render 'pd-opbouw', tone: 'dark' %} (homepage) of tone: 'light' (productpagina, gids). legend: false = alleen tekening.
{%- endcomment -%}
<figure class="pd-op pd-op--{{ tone | default: 'light' }}">
  <div class="pd-op__draw">''' + s + '''</div>
  {%- unless legend == false -%}
  <ol class="pd-op__legend">
    <li><b>Toplaag van gerecycled PVC</b><span>Met het decor en de structuur: hout, steen, beton, leer of Japandi.</span></li>
    <li><b>Kern van behandeld bamboe</b><span>Stevig, en door de behandeling waterbestendig. Hierin frees je de sleuven om te buigen.</span></li>
  </ol>
  {%- endunless -%}
  <figcaption class="pd-op__cap">Schematisch, niet op schaal.</figcaption>
</figure>
'''
open('/home/user/baet/theme-h1/snippets/pd-opbouw.liquid','w').write(liquid)
css='''<style>body{margin:0;background:#1B1917;width:760px}.pd-op__n circle{fill:#F5F2EC}.pd-op__n text{font:600 15px Arial;fill:#151413}</style>'''
open('t.html','w').write(css+s)
print(len(liquid))
