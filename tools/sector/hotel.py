# Sectorbeeld hotel: decor van Puredeco op de wand achter het bed in een aangeleverde foto (visualisatie).
import cv2, numpy as np, sys
BB='/home/user/baet/media/beeldbank/'
S='/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/hotel/'
src=cv2.imread(S+'src.jpg').astype(np.float32)/255
h,w=src.shape[:2]
QUAD=np.float32([[0,-220],[812,262],[812,603],[0,600]])   # wand: plafondlijn, hoek, bovenkant houten band
W_CM,H_CM,PX=270,165,6
SEAMS=[]
SECTION=(8,252)                                            # 2 panelen (244 cm) symmetrisch achter het hoofdbord (28-232 cm)                                     # zichtbare wand in cm, 6 px per cm in de textuur

def bbox(img):
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); ys,xs=np.where(g<235)
    return img[ys.min()+24:ys.max()-24, xs.min()+24:xs.max()-24]

def canvas(decor):
    tex=bbox(cv2.imread(BB+decor+'-0.jpg'))
    Wp,Hp=W_CM*PX,H_CM*PX
    if decor=='678':                       # doorlopend marmer: 2 panelen (244 x 280) gespiegeld, as achter het midden van het bed
        pair=cv2.resize(tex,(244*PX,280*PX))
        row=np.concatenate([cv2.flip(pair,1),pair,cv2.flip(pair,1),pair],1)
        Hi=cv2.getPerspectiveTransform(QUAD,np.float32([[0,0],[W_CM,0],[W_CM,H_CM],[0,H_CM]]))
        ax=float(cv2.perspectiveTransform(np.float32([[[470,600]]]),Hi)[0,0,0])   # midden van het bed op de wand
        start=int((2*244-ax)*PX)            # spiegelas tussen paneel 2 en 3 van de rij
        c=row[:Hp, start:start+Wp]
    else:                                  # hout: panelen van 122 cm met naad
        pan=cv2.resize(tex,(122*PX,280*PX))
        row=np.concatenate([pan if i%2==0 else cv2.flip(pan,0) for i in range(5)],1).astype(np.float32)
        for i in range(1,5): row[:, i*122*PX-1:i*122*PX+1]*=0.8
        start=int((122-SECTION[0])*PX)      # paneelrand op het linker uiteinde van de wandsectie
        SEAMS[:]=list(SECTION)               # LED aan beide uiteinden
        c=row[:Hp, start:start+Wp]
    return c.astype(np.float32)/255

def run(decor,out,led=False):
    c=canvas(decor)
    Hm=cv2.getPerspectiveTransform(np.float32([[0,0],[c.shape[1],0],[c.shape[1],c.shape[0]],[0,c.shape[0]]]),QUAD)
    warped=cv2.warpPerspective(c,Hm,(w,h),flags=cv2.INTER_AREA)
    poly=np.zeros((h,w),np.uint8); cv2.fillPoly(poly,[QUAD.astype(np.int32)],1)
    full=poly.copy()
    if decor!='678':
        sec=np.zeros(c.shape[:2],np.float32); sec[:,int(SECTION[0]*PX):int(SECTION[1]*PX)]=1
        poly=(cv2.warpPerspective(sec,Hm,(w,h),flags=cv2.INTER_LINEAR)>0.5).astype(np.uint8)
    # belichting van de oorspronkelijke wand: lichtsterkte en lichtkleur uit de geverfde wand (albedo ~0,82)
    lum=cv2.cvtColor((src*255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255
    wallpx=((lum>0.55)&(full>0)).astype(np.float32)
    k=(0,0); sig=40
    den=cv2.GaussianBlur(wallpx,k,sig)+1e-4
    light=np.dstack([cv2.GaussianBlur(src[...,i]*wallpx,k,sig)/den for i in range(3)])
    gray=light.mean(2,keepdims=True)
    tint=light/np.maximum(gray,1e-3); tint=1+(tint-1)*0.6
    E=np.clip(gray/0.82,0.78,1.3)
    warped=cv2.GaussianBlur(warped,(0,0),0.7)
    comp=warped*E*tint
    rng=np.random.default_rng(1); comp+=rng.normal(0,0.008,comp.shape).astype(np.float32)
    if led:
        # LED aan de zijkant van het paneel: verticale lichtlijnen in de naden naast het middelste paneel, strijklicht opzij over het hout
        Hp,Wp=c.shape[:2]; u=np.arange(Wp,dtype=np.float32)[None,:]/PX
        L=np.zeros((1,Wp),np.float32); line=np.zeros((1,Wp),np.float32)
        for us in SEAMS:
            d=np.abs(u-us)
            L+=2.1*np.exp(-d/10)+0.6*np.exp(-d/40)
            line+=(d<0.8).astype(np.float32)
        L=np.broadcast_to(L,(Hp,Wp)).astype(np.float32); line=np.broadcast_to(line,(Hp,Wp)).astype(np.float32)
        Lw_=cv2.warpPerspective(L,Hm,(w,h),flags=cv2.INTER_LINEAR)
        warm=np.float32([0.52,0.78,1.0])
        detail=warped-cv2.GaussianBlur(warped,(0,0),3)
        comp=comp*0.9+(warped+detail*2.5)*Lw_[...,None]*warm
        Ln=cv2.warpPerspective(line,Hm,(w,h),flags=cv2.INTER_LINEAR)
        glow=cv2.GaussianBlur(Ln,(0,0),4)
        comp=np.maximum(comp,np.clip(Ln*1.4,0,1)[...,None]*np.float32([0.82,0.94,1.0]))+glow[...,None]*warm*0.45
    # zachte schaduw langs plafond en hoek
    edge=np.zeros((h,w),np.float32); cv2.polylines(edge,[QUAD[:2].astype(np.int32)],False,1,6); cv2.line(edge,(812,262),(812,603),1,8)
    comp*=1-0.12*cv2.GaussianBlur(edge,(0,0),6)[...,None]
    # voorgrond die blijft: hanglampen en snoeren, hoofdbord
    # voorgrond (hanglampen, snoeren, hoofdbord) als matte: dekking uit het verschil met de lokale wandkleur
    Lw=gray[...,0]; Lf=0.14
    a=np.clip((Lw-lum)/np.maximum(Lw-Lf,0.2),0,1)
    a=np.where((a>0.3)&(lum<0.5),a,0)
    zone=np.zeros((h,w),np.float32)
    for x0,x1 in [(5,65),(85,112),(748,806)]: zone[:,x0:x1]=1
    zone[570:,170:800]=1
    a=np.clip(a*zone*1.15,0,1)
    cl=cv2.morphologyEx(a,cv2.MORPH_CLOSE,np.ones((61,1),np.uint8))*zone; cl[530:]=0
    a=np.maximum(a,cl)   # glimlicht op de buizen dichten (niet onder de buisuiteinden)
    a[575:,170:800]=np.where(a[575:,170:800]>0.35,1,a[575:,170:800]*0.5)
    fg=np.where(a[...,None]>0.8,src,np.float32([0.12,0.12,0.13]))
    new=src*(1-poly[...,None])+comp*poly[...,None]
    res=new*(1-a[...,None]*poly[...,None])+fg*(a[...,None]*poly[...,None])
    if led:
        # LED-licht valt ook op de geverfde wand naast de panelen; de LED-lijn zelf ligt op de rand van de sectie
        outw=(full*(1-poly)).astype(np.float32)[...,None]*(1-a[...,None])
        res=res+outw*src*Lw_[...,None]*warm*0.55
        lit=np.clip(Ln*1.4,0,1)[...,None]*(full[...,None])*(1-a[...,None])
        res=np.maximum(res,lit*np.float32([0.82,0.94,1.0]))+glow[...,None]*warm*0.25*full[...,None]
    # contactschaduw onder plafond en bij de hoek
    cv2.imwrite(out,(np.clip(res,0,1)*255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,93])

for d in sys.argv[1:]:
    led=d.endswith('led'); dec=d.replace('led','')
    run(dec,S+f'hotel-{d}.jpg',led)
