import cv2, numpy as np
from PIL import Image, ImageFilter
S=2
src=cv2.imread('orig.png')
up=cv2.resize(src,None,fx=S,fy=S,interpolation=cv2.INTER_LANCZOS4)
bl=cv2.GaussianBlur(up,(0,0),2.0); up=cv2.addWeighted(up,1.35,bl,-0.35,0)
def wipe(img,box,thr):
    x0,y0,x1,y1=[v*S for v in box]
    a=cv2.GaussianBlur(img,(0,0),3).astype(np.float32)
    top=a[y0-6,x0:x1]; bot=a[y1+6,x0:x1]
    h=y1-y0; t=np.linspace(0,1,h)[:,None,None]
    fill=top[None]*(1-t)+bot[None]*t
    fill+=np.random.normal(0,1.6,fill.shape)
    m=np.zeros((h,x1-x0),np.float32); m[:]=1
    m=cv2.GaussianBlur(m,(0,0),6); m=np.clip((m-0.05)/0.5,0,1)[...,None]
    roi=img[y0:y1,x0:x1].astype(np.float32)
    img[y0:y1,x0:x1]=np.clip(roi*(1-m)+fill*m,0,255).astype(np.uint8)
    return img
up=wipe(up,(520,196,815,312),70)
up=wipe(up,(720,1030,895,1160),70)
im=Image.fromarray(cv2.cvtColor(up,cv2.COLOR_BGR2RGB)).convert('RGBA')
logo=Image.open('logo-w.png')
def place(w,angle,cx,cy,alpha,shear=0.0,blur=0.7):
    l=logo.resize((w*S,int(logo.size[1]*w*S/logo.size[0])),Image.LANCZOS)
    if shear:
        W,H=l.size; l=l.transform((W,H+int(abs(shear)*W)),Image.AFFINE,(1,0,0,shear,1,-max(0,shear)*W*0),Image.BICUBIC)
    l=l.rotate(angle,resample=Image.BICUBIC,expand=True)
    a=l.split()[3].point(lambda v:int(v*alpha)); l.putalpha(a)
    l=l.filter(ImageFilter.GaussianBlur(blur))
    im.alpha_composite(l,(int(cx*S-l.size[0]/2),int(cy*S-l.size[1]/2)))
place(250,4.5,666,252,0.9)
place(150,24,805,1098,0.85)
im.convert('RGB').save('disp-fix.jpg',quality=92)
im.convert('RGB').crop((960,360,1820,860)).save('chk-top.jpg'); im.convert('RGB').crop((1360,1900,1920,2360)).save('chk-bot.jpg')
