import cv2, numpy as np
src=cv2.imread('../live/img/sr-orig.jpg')
# 2x opschalen (Lanczos) + lichte verscherping
up=cv2.resize(src,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
blur=cv2.GaussianBlur(up,(0,0),1.6); up=cv2.addWeighted(up,1.45,blur,-0.45,0)
def grade(img, tv_off=False):
    f=img.astype(np.float32)/255
    if tv_off:
        # tv-scherm (x 322-532, y 425-598 in 2x) uitzetten: donker glas met een zachte reflectie
        m=np.zeros(f.shape[:2],np.float32); pts=np.array([[326,429],[528,431],[528,592],[326,596]],np.int32)
        cv2.fillConvexPoly(m,pts,1.0); m=cv2.GaussianBlur(m,(3,3),0)[...,None]
        g=(np.linspace(0.10,0.05,f.shape[0])[:,None,None]*np.ones_like(f)).astype(np.float32)
        f=f*(1-m)+g*m
    # warmer wit (tl-licht is koel/groenig)
    f[...,2]*=1.07; f[...,1]*=1.025; f[...,0]*=0.94; f*=1.06
    # zachte S-curve + schaduwen iets op
    f=np.clip(f,0,1); f=f+0.06*(f*(1-f))*(2*f-1)*-1+0.03*(1-f)**2
    # lichte desaturatie van fel geel/groen
    hsv=cv2.cvtColor(np.clip(f,0,1).astype(np.float32),cv2.COLOR_BGR2HSV); hsv[...,1]*=0.95
    f=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    # vignet
    h,w=f.shape[:2]; y,x=np.ogrid[:h,:w]; d=((x-w*0.42)/(w*0.75))**2+((y-h*0.55)/(h*0.85))**2
    f=f*np.clip(1-0.22*d,0.7,1)[...,None].astype(np.float32)
    return (np.clip(f,0,1)*255).astype(np.uint8)
def crop(img,x0,y0,x1,y1,out_w):
    c=img[y0:y1,x0:x1]; return cv2.resize(c,(out_w,int(out_w*(y1-y0)/(x1-x0))),interpolation=cv2.INTER_LANCZOS4)
A=crop(grade(up),0,170,1250,950,1600)
B=crop(grade(up,True),0,170,1250,950,1600)
C=crop(grade(up,True),20,150,700,1000,1100)
cv2.imwrite('A-licht-kleur.jpg',A,[cv2.IMWRITE_JPEG_QUALITY,90])
cv2.imwrite('B-tv-uit.jpg',B,[cv2.IMWRITE_JPEG_QUALITY,90])
cv2.imwrite('C-staand.jpg',C,[cv2.IMWRITE_JPEG_QUALITY,90])
print(A.shape,B.shape,C.shape)
