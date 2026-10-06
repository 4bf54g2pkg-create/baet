# Lokale weergave van de homepage (pd-home + pd-home-cta) met nepdata.
import re, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from liquid import Environment, CachingFileSystemLoader
from markupsafe import Markup
TH='/home/user/baet/theme-h1/'
os.makedirs('snips',exist_ok=True)
for f in os.listdir(TH+'snippets'):
    if f.startswith('pd-'): open('snips/'+f,'w').write(open(TH+'snippets/'+f).read())
env=Environment(loader=CachingFileSystemLoader('snips', ext='.liquid'), autoescape=False)
def image_url(img, width=None, **k):
    if img is None: return ''
    return img['src'] if isinstance(img,dict) else str(img)
env.add_filter('image_url', image_url); env.add_filter('handle', lambda s: str(s).lower().replace(' ','-')); env.add_filter('url_encode', lambda s: str(s).replace(' ','+'))
env.add_filter('image_tag', lambda u, **k: Markup(f'<img src="{u}" alt="{k.get("alt","")}" loading="lazy">'))
env.add_filter('video_tag', lambda v, **k: Markup(f'<video src="{v}" class="{k.get("class","")}" muted playsinline></video>'))
SW={'811':'#6A4E3A','810':'#2E2622','824':'#A79A86','851':'#D8CCB4','843':'#8E8A84','830':'#9C8268'}
def P(handle, title, n=4):
    code=re.search(r'\b(\d{3})\b',title).group(1)
    media=[{'src':f'sw-{code}.svg'}]+[{'src':'room.svg'} for _ in range(n-1)]
    return {'handle':handle,'title':title,'url':'#','media':media,'featured_image':media[0]}
ps=[P('811-hout-walnut-classic','Wandpaneel Hout 811 Walnut Classic 8 mm Naadloos'),P('810-hout-noir-oak','Wandpaneel Hout 810 Noir Oak'),
    P('824-japanse-stof-japandi-taupe-dark','Wandpaneel Japandi 824 Taupe',5),P('wandpaneel-travertine-ivory-851','Wandpaneel Travertine Ivory 851 | Travertinlook | Puredeco',5),
    P('843-art-stucco-light-shadow','Wandpaneel Art 843 Stucco Shadow',6),P('830-leer-leather-taup','Wandpaneel Leer 830 Taupe',3)]
for code,c in SW.items(): open(f'sw-{code}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400"><rect width="400" height="400" fill="{c}"/></svg>')
all_products={p['handle']:p for p in ps}
BBK='/home/user/baet/media/beeldbank/'
for h,t_,fs in [('concrete-smoke-691-betonlook','Wandpaneel Concrete Smoke 691',['691-0.png','691-1.png','691-2.jpg']),
                ('wandpaneel-travertine-ivory-851','Wandpaneel Travertine Ivory 851',['851-0.png','851-1.png','851-2.png','851-3.png','851-4.png']),
                ('812-hout-walnut-deep','Wandpaneel Hout 812 Walnut Deep',['812-0.jpg','812-1.png','812-2.png','812-3.jpg'])]:
    m=[{'src':BBK+f} for f in fs]; all_products[h]={'handle':h,'title':t_,'url':'#','media':m,'featured_image':m[0]}
cols={h:{'url':'#','products_count':5,'image':{'src':'room.svg'},'products':[ps[0]]} for h in ['hout-1','japandi','kunst','doorlopend-marmer']}
cols['leer']={'url':'#','products_count':3,'image':None,'products':[ps[5]]}
images={f'pd-montage-stap-{i}.jpg':{'src':f'/tmp/claude-0/-home-user-baet/20c8e88a-a0d2-5581-8005-f8ed232319d0/scratchpad/steps/pd-montage-stap-{i}.jpg'} for i in range(1,6)}
shop={'metafields':{'puredeco':{'montage_video':{'value':'film.mp4'},'montage_video_mobile':{'value':'filmp.mp4'}}}}
def prep(src): return re.sub(r'\{%\s*schema\s*%\}.*?\{%\s*endschema\s*%\}','',src,flags=re.S)
def defaults(sec):
    s=json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}',open(TH+f'sections/{sec}.liquid').read(),re.S).group(1))
    return {x['id']:x.get('default') for x in s.get('settings',[]) if 'id' in x and x.get('default') is not None}
def prep2(src):
    src=prep(src)
    src=re.sub(r"\{%-?\s*form 'contact'[^%]*-?%\}",'<form class="pp-form__form">',src)
    return re.sub(r'\{%-?\s*endform\s*-?%\}','</form>',src)
if len(sys.argv)>1 and sys.argv[1]=='samples':
    BB='/home/user/baet/media/beeldbank/'
    titles=[('Wandpaneel Hout 811 Walnut Classic 8 mm Naadloos','811-0.jpg'),('Wandpaneel Hout 812 Walnut Deep','812-0.jpg'),('Wandpaneel Hout 810 Noir Oak','810-0.jpg'),('Wandpaneel Japandi 824 Taupe','824-0.jpg'),('Wandpaneel Japandi 823 Taupe Dark','823-0.jpg'),('Wandpaneel Leer 830 Taupe','830-0.jpg'),('Wandpaneel Art 843 Stucco Shadow','843-0.jpg'),('Wandpaneel Marmer 670 Pandora Slate','670-0.jpg'),('Wandpaneel Marmer Doorlopend 678 Italian Gold Slate','678-0.jpg'),('Wandpaneel Travertine Ivory 851 | Travertinlook | Puredeco','851-0.png'),('Wandpaneel Concrete Smoke 691 | Betonlook | Puredeco','691-0.png')]
    prods=[{'title':ti,'url':'#','featured_image':{'src':BB+im},'selected_or_first_available_variant':{'id':1000+i}} for i,(ti,im) in enumerate(titles)]
    ss=defaults('pd-samples'); ss['collection']={'products':prods}
    out=env.from_string(prep(open(TH+'sections/pd-samples.liquid').read())).render(section={'settings':ss},collections={})
elif len(sys.argv)>1 and sys.argv[1]=='projects':
    out=env.from_string(prep2(open(TH+'sections/pd-projects.liquid').read())).render(section={'settings':defaults('pd-projects')},all_products=all_products,form={})
else:
    hs=defaults('pd-home'); hs['hero_image']={'src':'hero.jpg'}; hs['story_image']={'src':'story.jpg'}; hs['show_stone']=True; hs['story_caption']='812 Walnut Deep · visualisatie'; hs['hero_caption']='811 Walnut Classic · interieur: visualisatie'; hs['hero_caption_photo']='811 Walnut Classic · Signature · echte productfoto'
    out=env.from_string(prep(open(TH+'sections/pd-home.liquid').read())).render(section={'settings':hs},all_products=all_products,collections=cols,images=images,shop=shop)
    out+='<div style="padding:80px 96px;font:28px serif">[Instafeed: Bij klanten en in projecten]</div>'
    out+=env.from_string(prep(open(TH+'sections/pd-home-cta.liquid').read())).render(section={'settings':defaults('pd-home-cta')})
css=open(TH+'assets/puredeco-premium.css').read()
html=f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>@font-face{{font-family:'Cormorant';src:url(../film/cormorant.woff2);font-weight:300 700}}@font-face{{font-family:'Instrument Sans';src:url(../film/instrument.woff2);font-weight:400 700}}
html{{font-size:62.5%}}body{{margin:0;background:#F5F2EC;font-family:'Instrument Sans',sans-serif;font-size:1.5rem;color:#151413}}:root{{--font-heading-family:'Cormorant',Georgia,serif;--font-body-family:'Instrument Sans',sans-serif}}
.hdr{{height:64px;border-bottom:1px solid #DDD6CA;display:flex;align-items:center;justify-content:center;font-size:20px}}</style>
<style>{css}</style></head><body class="template-index"><div class="hdr">PureDeco (header theme)</div>{out}</body></html>'''
open('page.html','w').write(html); print('ok',len(html))
