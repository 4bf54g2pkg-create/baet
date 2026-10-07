# Maakt vierkante materiaalstalen per decor uit de productfoto (paneel op wit) in media/beeldbank.
import cv2, numpy as np, os, glob
BB='/home/user/baet/media/beeldbank/'; OUT='/home/user/baet/media/stalen/'
codes='602 607 615 810 811 812 619 620 821 823 824 646 830 831 840 841 842 843 632 670 678 689 691 851'.split()
for c in codes:
    src = BB+'691-2.jpg' if c=='691' else sorted(glob.glob(BB+c+'-0.*'))[0]
    im=cv2.imread(src)
    if im is None: print('skip',c); continue
    g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); ys,xs=np.where(g<232)
    x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max()
    w=x1-x0; h=y1-y0; s=int(min(w,h)*0.62)
    cx,cy=(x0+x1)//2,(y0+y1)//2
    crop=im[cy-s//2:cy+s//2, cx-s//2:cx+s//2]
    cv2.imwrite(OUT+f'staal-{c}.jpg',cv2.resize(crop,(600,600),interpolation=cv2.INTER_AREA),[cv2.IMWRITE_JPEG_QUALITY,90])
print('ok')
