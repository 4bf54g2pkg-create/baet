# Trapsgewijze doorsnede van de vier lagen (oblique), lagen van onder naar boven steeds korter
def layers_svg(dark=True, fs=22, fs2=12.5):
    W,D,Dv,step=470,120,66,104
    x0=30; base=300
    ink='#F5F2EC' if dark else '#151413'
    sub='#BDB4A6' if dark else '#6E675E'
    L=[('Gerecyclede onderlaag','De achterkant, hier komt de montagekit op',11,'#BDB6AA','#A9A295','#9B9487',None),
       ('Kern van bamboe','Stevig en vormvast',36,'#D9C38F','#C8B07A','#B39A64','fibre'),
       ('Gerecycled PVC','Waterbestendig',14,'#E9E3D8','#D6CEC0','#C9C0B1',None),
       ('Toplaag met decor','Het decor onder een beschermende laag',10,'#6A4E3A','#57402F','#4A3628','grain')]
    out=[]; y=base; anchors=[]
    for i,(n,s,t,top,front,side,pat) in enumerate(L):
        w=W-i*step
        yt=y-t   # top of this layer (front edge)
        out.append(f'<rect x="{x0}" y="{yt}" width="{w}" height="{t}" fill="{front}"/>')
        out.append(f'<polygon points="{x0+w},{yt} {x0+w+D},{yt-Dv} {x0+w+D},{yt-Dv+t} {x0+w},{yt+t}" fill="{side}"/>')
        out.append(f'<polygon points="{x0},{yt} {x0+w},{yt} {x0+w+D},{yt-Dv} {x0+D},{yt-Dv}" fill="{top}"/>')
        if pat=='grain':
            for k in range(1,22):
                a=k/22
                out.append(f'<path d="M{x0+w*a:.1f} {yt} L{x0+w*a+D:.1f} {yt-Dv}" stroke="#80604A" stroke-width="{0.6+0.6*(k%4==0)}" opacity=".75"/>')
        if pat=='fibre':
            for k in range(1,20):
                a=k/20
                out.append(f'<path d="M{x0+D*a:.1f} {yt-Dv*a:.1f} L{x0+w+D*a:.1f} {yt-Dv*a:.1f}" stroke="#C2A96F" stroke-width=".8"/>')
            for k in range(1,10):
                out.append(f'<path d="M{x0} {yt+k*3.6:.1f}H{x0+w}" stroke="#BEA46B" stroke-width=".5"/>')
        # anker: midden van het zichtbare stuk bovenvlak (deel dat niet door de volgende laag bedekt wordt)
        if i<3:
            ax=x0+w-step/2+D/2; ay=yt-Dv/2
        else:
            ax=x0+w/2+D/2; ay=yt-Dv/2
        anchors.append((ax,ay,n,s))
        y=yt
    lab_x=x0+W+D+40
    ys=[300,226,152,78][::-1]
    out2=[]
    for (ax,ay,n,s),ly in zip(anchors[::-1],[112,172,232,292]):
        out2.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="3" fill="{ink}"/>')
        out2.append(f'<path d="M{ax:.1f} {ay:.1f}L{lab_x-40:.1f} {ly-6}H{lab_x-8}" stroke="{sub}" stroke-width=".8" fill="none"/>')
        out2.append(f'<text x="{lab_x}" y="{ly-2}" fill="{ink}" font-family="Cormorant,Georgia,serif" font-size="{fs}">{n}</text>')
        out2.append(f'<text x="{lab_x}" y="{ly+fs2+6}" fill="{sub}" font-family="Instrument Sans,Arial,sans-serif" font-size="{fs2}">{s}</text>')
    return f'<svg viewBox="0 70 {lab_x+max(250,fs2*22):.0f} 250" role="img" aria-label="Opbouw van een Puredeco-wandpaneel in vier lagen">'+''.join(out)+''.join(out2)+'</svg>'
if __name__=='__main__':
    open('layers-test.html','w').write('<body style="background:#1B1917;margin:0;width:900px">'+layers_svg()+'</body>')
