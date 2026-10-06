# Sectorbeeld horeca: Puredeco-decor op de bakstenen wand van een aangeleverde cafefoto (visualisatie).
import cv2, numpy as np, sys
BB='/home/user/baet/media/beeldbank/'
S='/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/horeca/'
src=cv2.imread(S+'src.jpg').astype(np.float32)/255
h,w=src.shape[:2]
X0,X1,FLOOR=470,1655,1132              # panelenvlak: van het einde van de bar tot voor de waterski's; vloerlijn
SOFFIT=np.int32([[1338,0],[2000,0],[2000,102],[1652,102],[1348,212],[1338,212]])
hsv=cv2.cvtColor((src*255).astype(np.uint8),cv2.COLOR_BGR2HSV)
H,Sa,V=[hsv[...,i].astype(np.float32) for i in range(3)]

def fg_mask():
    m=np.zeros((h,w),np.uint8)
    cv2.fillPoly(m,[SOFFIT],1)
    # tafelblad en poten
    cv2.fillPoly(m,[np.int32([[945,790],[1440,798],[1890,870],[1910,880],[1910,935],[1015,885],[945,845]])],1)
    cv2.fillPoly(m,[np.int32([[1003,880],[1032,880],[1030,1333],[1000,1333]])],1)
    cv2.fillPoly(m,[np.int32([[1868,900],[1912,900],[1915,1333],[1872,1333]])],1)
    zone=np.zeros((h,w),np.uint8)
    cv2.fillPoly(zone,[np.int32([[870,770],[1720,770],[1720,1333],[870,1333]])],1)
    # gele zittingen en ruggen
    yel=((H>18)&(H<34)&(Sa>90)&(V>45)).astype(np.uint8)&zone        # ook zittingen in de schaduw
    yel=cv2.morphologyEx(yel,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
    n_,lbl,st,_=cv2.connectedComponentsWithStats(yel)
    for i in range(1,n_):
        if st[i,cv2.CC_STAT_AREA]<150: yel[lbl==i]=0
    m|=cv2.dilate(yel,np.ones((5,5),np.uint8))
    # verchroomde buizen: licht, weinig kleur, lang doorlopend (voegen in het metselwerk zijn kort en horizontaal)
    chrome=(((Sa<55)&(V>105))).astype(np.uint8)&zone
    chrome[:890]&=((Sa[:890]<40)&(V[:890]>170)).astype(np.uint8)    # boven de tafel is de steen zelf grijs: alleen echte glans
    wide=cv2.morphologyEx(chrome,cv2.MORPH_OPEN,np.ones((13,13),np.uint8))     # vlakken (lichte steen) eruit, alleen dunne buizen houden
    chrome=chrome&(1-cv2.dilate(wide,np.ones((5,5),np.uint8)))
    vert=cv2.morphologyEx(chrome,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_RECT,(1,45)))
    k=np.eye(25,dtype=np.uint8)
    diag1=cv2.morphologyEx(chrome,cv2.MORPH_OPEN,k)
    diag2=cv2.morphologyEx(chrome,cv2.MORPH_OPEN,np.fliplr(k).copy())
    m|=cv2.dilate(vert|diag1|diag2,np.ones((5,5),np.uint8))
    # hanglampen: snoeren en peren
    for x0,x1,y1 in [(1165,1195,345),(1245,1280,240)]:
        z=np.zeros((h,w),np.uint8); z[:y1,x0:x1]=1
        m|=(z&(((V<70))|((V>200)&(H<35)))).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    return m

def texture(decor,Wp,Hp):
    if decor=='691': return cv2.imread(BB+'691-2.jpg')[40:-40,40:-40]     # volvlaks opname van het oppervlak
    tex=cv2.imread(BB+decor+'-0.jpg'); g=cv2.cvtColor(tex,cv2.COLOR_BGR2GRAY); ys,xs=np.where(g<235)
    tex=tex[ys.min()+40:ys.max()-40, xs.min()+24:xs.max()-24]
    return tex

def run(decor,out,led=True):
    # schaal: baksteen ~21 cm over ~66 px  -> ~3,1 px per cm; paneel 122 cm ~ 380 px
    PXCM=3.1
    pw=int(122*PXCM); ph=int(280*PXCM)
    t=texture(decor,pw,ph)
    if decor in ('691',): pan=cv2.resize(t,(pw,ph))
    else: pan=cv2.resize(t,(pw,ph))
    n=int(np.ceil((X1-X0)/pw))+1
    row=np.concatenate([pan if i%2==0 else cv2.flip(pan,0) for i in range(n)],1).astype(np.float32)/255
    for i in range(1,n): row[:, i*pw-1:i*pw+1]*=0.82
    # panelen symmetrisch in de sectie
    off=int((n*pw-(X1-X0))/2)
    wall=np.zeros_like(src)
    seg=row[:, off:off+(X1-X0)]
    stack=np.concatenate([cv2.flip(seg,0),seg],0); stack[ph-2:ph+1]*=0.55     # wand hoger dan 280 cm: tweede rij met horizontale naad
    wall[:FLOOR, X0:X1]=stack[2*ph-FLOOR:, :]
    sec=np.zeros((h,w),np.float32); sec[:FLOOR, X0:X1]=1
    fg=fg_mask().astype(np.float32)
    # licht uit de baksteen: sterk vervaagde luminantie (de lampen geven warme vlekken)
    lum=cv2.cvtColor((src*255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255
    wallpx=sec*(1-fg)
    den=cv2.GaussianBlur(wallpx,(0,0),28)+1e-4
    light=np.dstack([cv2.GaussianBlur(src[...,i]*wallpx,(0,0),28)/den for i in range(3)])
    gray=light.mean(2,keepdims=True)
    tint=light/np.maximum(gray,1e-3); tint=1+(tint-1)*0.25
    E=np.clip(gray/0.50,0.3,1.25)            # baksteen heeft een lage albedo (~0,50)
    comp=wall*E*tint
    if led:
        xs=np.arange(w,dtype=np.float32)[None,:]
        L=np.zeros((1,w),np.float32); line=np.zeros((1,w),np.float32)
        for xe in (X0,X1):
            d=np.abs(xs-xe)
            L+=1.9*np.exp(-d/30)+0.5*np.exp(-d/120); line+=(d<2.5)
        L=np.broadcast_to(L,(h,w)).copy(); L[FLOOR:]=0; line=np.broadcast_to(line,(h,w)).copy(); line[FLOOR:]=0
        warm=np.float32([0.52,0.78,1.0])
        detail=wall-cv2.GaussianBlur(wall,(0,0),3)
        comp=comp+(wall+detail*2.2)*L[...,None]*warm*sec[...,None]*0.9
    # schaduw onder het tafelblad en achter de stoelen
    sh=np.zeros((h,w),np.float32)
    cv2.fillPoly(sh,[np.int32([[945,845],[1910,890],[1910,1132],[945,1132]])],1)
    sh=cv2.GaussianBlur(sh,(0,0),35)
    yy=np.arange(h,dtype=np.float32)[:,None]
    depth=np.clip((yy-850)/300,0,1)
    comp*=(1-sh*(0.55-0.2*depth))[...,None]
    comp=cv2.GaussianBlur(comp,(0,0),0.6)
    rng=np.random.default_rng(2); comp+=rng.normal(0,0.01,comp.shape).astype(np.float32)
    # plint-schaduw op de vloerlijn
    a=sec*(1-cv2.GaussianBlur(fg,(0,0),0.8))
    res=src*(1-a[...,None])+comp*a[...,None]
    if led:
        outw=(1-sec)*(1-fg); outw[FLOOR:]=0; outw[:, :X0-0][:, :]=outw[:, :X0]; 
        res=res+outw[...,None]*src*L[...,None]*warm*0.5
        lit=np.clip(line,0,1)*(1-fg)
        res=np.maximum(res,lit[...,None]*np.float32([0.82,0.94,1.0]))+cv2.GaussianBlur(lit,(0,0),5)[...,None]*warm*0.35
    cv2.imwrite(out,(np.clip(res,0,1)*255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,93])
    cv2.imwrite(S+'fg.png',cv2.resize(fg_mask()*255,(1000,666)))

for d in sys.argv[1:]:
    run(d.replace('led',''),S+f'horeca-{d}.jpg',led=d.endswith('led'))
