# Genereert de Puredeco-beeldset uit echte catalogusbeelden (media/beeldbank) en projectstills (media/stills-670).
import os, subprocess
BB='/home/user/baet/media/beeldbank/'; ST='/home/user/baet/media/stills-670/'
OUT='/home/user/baet/media/banners/'; T='/home/user/baet/tools/banners/'
HEAD=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:C;src:url({T}cormorant.woff2);font-weight:300 700}}@font-face{{font-family:I;src:url({T}instrument.woff2);font-weight:400 700}}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:100%;height:100%;overflow:hidden;background:#F5F2EC;font-family:I;color:#151413;font-variant-ligatures:none}}
.g{{filter:sepia(.07) saturate(.95) contrast(1.03) brightness(.99)}}
.cover{{width:100%;height:100%;object-fit:cover;display:block}}
.tex{{background-repeat:no-repeat;filter:sepia(.05) contrast(1.02)}}
</style></head><body>'''
def page(name,w,h,body):
    p=T+'_'+name+'.html'; open(p,'w').write(HEAD+body+'</body></html>')
    subprocess.run(['node',T+'render.js',p,str(w),str(h),OUT+name+'.png'],check=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',OUT+name+'.png','-q:v','2',OUT+name+'.jpg'],check=True)
    os.remove(OUT+name+'.png')
def tex(img,pos='50% 50%',size='520%'):
    return f'background-image:url({BB}{img});background-position:{pos};background-size:{size}'

# 1 · Homepage hero (tekst staat live op de site, links op het donkere vlak)
page('home-hero-desktop',2400,1200,f'''<div style="display:grid;grid-template-columns:960px 1fr;height:100%">
<div style="background:linear-gradient(180deg,#2B241E,#221C17)"></div>
<div style="position:relative"><img class="cover g" src="{BB}851-2.png" style="object-position:50% 46%">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(34,28,23,.55),rgba(34,28,23,0) 22%)"></div></div></div>''')
page('home-hero-mobile',1080,1600,f'''<img class="cover g" src="{BB}851-2.png" style="object-position:58% 50%">''')

# 2 · Collectiebanners: sfeer + het materiaal van dichtbij
coll=[('hout','hout-2.png','812-0.jpg','50% 50%','600%','50% 55%'),('japandi','823-2.png','823-0.jpg','50% 50%','560%','50% 50%'),
('leer','830-1.png','830-2.jpg','50% 75%','260%','40% 50%'),('art','843-4.png','843-5.jpg','50% 50%','150%','50% 50%'),
('marmer','678-1.png','678-0.jpg','50% 45%','330%','50% 55%'),('steen','851-1.png','851-4.png','50% 50%','200%','50% 50%')]
for n,room,mat,tp,ts,rp in coll:
    page(f'collectie-{n}',2400,900,f'''<div style="display:grid;grid-template-columns:1fr 760px;gap:24px;height:100%;background:#F5F2EC">
<img class="cover g" src="{BB}{room}" style="object-position:{rp}"><div class="tex" style="{tex(mat,tp,ts)}"></div></div>''')
    page(f'collectie-{n}-kaart',1600,1000,f'''<img class="cover g" src="{BB}{room}" style="object-position:{rp}">''')

# 3 · Puredeco Projects: hero + sectoren (visualisaties uit de catalogus, juiste decor)
page('projects-hero',1600,2000,f'''<img class="cover g" src="{BB}678-2.png" style="object-position:45% 50%">''')
for n,img,pos in [('hotels','678-1.png','50% 50%'),('horeca','689-1.png','35% 50%'),('kantoren','810-2.png','50% 50%'),('retail','823-2.png','40% 50%')]:
    page(f'sector-{n}',1200,1500,f'''<img class="cover g" src="{BB}{img}" style="object-position:{pos}">''')

# 4 · The Puredeco Edit: drie echte stalen
sw=[('811-0.jpg','50% 50%','620%',-5,120,180),('824-0.jpg','50% 50%','620%',2,560,120),('851-4.png','50% 50%','260%',-2,1000,200)]
cards=''.join(f'<div class="tex" style="position:absolute;left:{x}px;top:{y}px;width:420px;height:600px;{tex(i,p,s)};transform:rotate({r}deg);box-shadow:0 40px 60px -30px rgba(21,20,19,.45),0 2px 0 rgba(255,255,255,.4) inset"></div>' for i,p,s,r,x,y in sw)
page('edit-samplebox',1600,1200,f'''<div style="position:relative;height:100%;background:radial-gradient(120% 90% at 30% 20%,#F7F4EE,#E6DFD3)">{cards}
<div style="position:absolute;left:120px;right:120px;bottom:120px;height:2px;background:rgba(21,20,19,.08)"></div></div>''')

# 5 · In de praktijk · 670 Pandora Slate (echte projectbeelden)
page('praktijk-670',2400,1000,f'''<div style="display:grid;grid-template-columns:1fr 1fr 1.5fr;gap:24px;height:100%;background:#F5F2EC">
<img class="cover g" src="{ST}670-1.2.jpg" style="object-position:50% 60%"><img class="cover g" src="{ST}670-4.8.jpg" style="object-position:50% 45%">
<img class="cover g" src="{ST}670-6.6.jpg" style="object-position:50% 40%"></div>''')

# 6 · Social: post (4:5) en story (9:16), tekst mag in het beeld
def post(n,room,code,name,cat,pos='50% 50%'):
    page(f'social-{n}',1080,1350,f'''<div style="display:grid;grid-template-rows:1000px 1fr;height:100%">
<img class="cover g" src="{BB}{room}" style="object-position:{pos}">
<div style="padding:56px 64px;display:flex;justify-content:space-between;align-items:flex-end;background:#F5F2EC">
<div><div style="font-size:22px;letter-spacing:.22em;text-transform:uppercase;color:#6E675E">{cat} · {code}</div>
<div style="font-family:C;font-weight:500;font-size:96px;line-height:1;margin-top:18px">{name}</div></div>
<div style="text-align:right;font-size:22px;color:#6E675E;line-height:1.5"><span style="font-weight:600;color:#151413">Pure</span>Deco<br>Eén wand. Eén geheel.</div></div></div>''')
post('851','851-2.png','851','Travertine Ivory','Steen')
post('823','823-2.png','823','Taupe Dark','Japandi')
post('678','678-1.png','678','Italian Gold Slate','Marmer')
page('social-story-851',1080,1920,f'''<div style="position:relative;height:100%"><img class="cover g" src="{BB}851-2.png" style="object-position:55% 50%">
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(21,20,19,.72),rgba(21,20,19,0) 50%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:160px;color:#F5F2EC">
<div style="font-size:26px;letter-spacing:.22em;text-transform:uppercase;opacity:.85">Steen · 851 Travertine Ivory</div>
<div style="font-family:C;font-weight:500;font-size:128px;line-height:.95;margin-top:24px">Eén wand.<br>Eén geheel.</div>
<div style="margin-top:40px;font-size:30px;opacity:.9">Vraag gratis stalen aan · puredeco.nl</div></div></div>''')
print('klaar')

# Ronde 8b · homepage-hero met hout (615 Wood Radiata, catalogusbeeld 2560 px) en merkverhaalbeeld (811 Walnut Classic, echte productfoto)
page('home-hero-hout-desktop',2400,1200,f'''<img class="cover g" src="{BB}hout-1.jpg" style="object-position:50% 62%;filter:sepia(.16) saturate(1.05) contrast(1.04) brightness(.97)">''')
page('home-hero-hout-mobile',1080,1600,f'''<img class="cover g" src="{BB}hout-1.jpg" style="object-position:46% 60%;filter:sepia(.16) saturate(1.05) contrast(1.04) brightness(.97)">''')
page('merkverhaal-811',1200,1500,f'''<div class="tex" style="width:100%;height:100%;{tex('811-0.jpg','50% 50%','330%')}"></div>''')

# Ronde 8c · homepage-hero hout: warm walnootinterieur (catalogusbeeld "Wandpaneel hout") naast een rustig tekstvlak
page('home-hero-hout-desktop',2400,1200,f'''<div style="display:grid;grid-template-columns:900px 1fr;height:100%">
<div style="background:linear-gradient(180deg,#2E2119,#241A14)"></div>
<div style="position:relative"><img class="cover g" src="{BB}hout-2.png" style="object-position:62% 55%">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(36,26,20,.6),rgba(36,26,20,0) 20%)"></div></div></div>''')
page('home-hero-hout-mobile',1080,1600,f'''<img class="cover g" src="{BB}hout-2.png" style="object-position:58% 50%">''')
