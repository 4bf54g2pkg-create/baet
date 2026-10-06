# Vloer in het hotelbeeld passend bij 810 Noir Oak: blauw tapijt omgekleurd naar warm greige, patroon rustiger (licht en schaduw blijven).
import cv2, numpy as np, sys
S='/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/hotel/'
im=cv2.imread(S+sys.argv[1]); h,w=im.shape[:2]
lab=cv2.cvtColor(im,cv2.COLOR_BGR2LAB).astype(np.float32)
L,a,b=lab[...,0],lab[...,1]-128,lab[...,2]-128
area=np.zeros((h,w),np.uint8)
cv2.fillPoly(area,[np.int32([[0,1030],[275,1070],[835,1333],[0,1333]]),          # links van het bed
                   np.int32([[835,1333],[1148,905],[1150,870],[1320,860],[1560,930],[1540,1180],[1720,1333]])],1)   # rechts van het bed tot het raam
m=((b<5)&(L<205)&(area>0)).astype(np.uint8)
win=np.zeros((h,w),np.uint8); cv2.fillPoly(win,[np.int32([[1100,865],[1330,855],[1330,935],[1100,935]])],1)
m|=((b<0)&(L<245)&(win>0)&(area>0)).astype(np.uint8)   # zonnig stuk vloer bij het raam
m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
# kleine losse eilandjes weg
n,lbl,st,_=cv2.connectedComponentsWithStats(m)
for i in range(1,n):
    if st[i,cv2.CC_STAT_AREA]<1500: m[lbl==i]=0
mf=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.5)
Lb=cv2.GaussianBlur(L,(0,0),18)
L2=Lb+(L-Lb)*0.42+8                                   # rustiger patroon, iets lichter
a2=np.full_like(a,2.5); b2=np.full_like(b,11.0)       # warm greige
out=np.dstack([L2,a2+128,b2+128])
out=cv2.cvtColor(np.clip(out,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR).astype(np.float32)
res=im.astype(np.float32)*(1-mf[...,None])+out*mf[...,None]
cv2.imwrite(S+sys.argv[2],res.astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,93])
cv2.imwrite(S+'vm.png',cv2.resize((m*255),(1000,666)))
