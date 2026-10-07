import re, json, sys, os
from liquid import Environment, CachingFileSystemLoader
from markupsafe import Markup
TH='/home/user/baet/theme-h1/'
os.makedirs('snips',exist_ok=True)
for f in os.listdir(TH+'snippets'):
    if f.startswith('pd-'): open('snips/'+f,'w').write(open(TH+'snippets/'+f).read())
env=Environment(loader=CachingFileSystemLoader('snips', ext='.liquid'), autoescape=False)
def money(c): 
    c=int(c or 0); s=f"{c/100:,.2f}".replace(',','X').replace('.',',').replace('X','.'); return '€'+s
def image_url(img, width=None, **k): 
    if img is None: return ''
    return img['src'] if isinstance(img,dict) else str(img)
def image_tag(url, **k):
    cls=k.get('class',''); alt=k.get('alt','')
    return Markup(f'<img src="{url}" alt="{alt}" class="{cls}" loading="lazy">')
def video_tag(v, **k):
    cls=k.get('class','')
    return Markup(f'<video src="{v}" class="{cls}" muted playsinline preload="metadata"></video>')
env.add_filter('money', money); env.add_filter('image_url', image_url); env.add_filter('image_tag', image_tag)
env.add_filter('video_tag', video_tag); env.add_filter('json', lambda x: json.dumps(x if not isinstance(x,list) else [str(i) for i in x]))
env.add_filter('payment_type_svg_tag', lambda t, **k: Markup(f'<svg class="pdh__pay-icon" viewBox="0 0 38 24"><rect width="38" height="24" rx="3" fill="#fff" stroke="#ccc"/><text x="19" y="15" font-size="7" text-anchor="middle">{t}</text></svg>'))
env.add_filter('structured_data', lambda p: '{}'); env.add_filter('t', lambda s, **k: s)
env.add_filter('external_video_tag', lambda v, **k: '')
class Val(str):
    def __new__(cls, v, sel=False):
        o=str.__new__(cls,v); o.selected=sel; return o
pack={'src':'wood.svg','media_type':'image','alt':''}
media=[pack]+[{'src':'room.svg','media_type':'image','alt':''} for _ in range(3)]
vs=[('260 cm x 122 cm','5mm Stomp',13995,True,0),('260 cm x 122 cm','8mm Naadloos',16995,True,43),('280 cm x 122 cm','5mm Stomp',13995,True,4),('280 cm x 122 cm','8mm Naadloos',17995,True,4)]
variants=[{'id':52941931446538+i,'price':p,'compare_at_price':0,'available':a,'inventory_management':'shopify','inventory_quantity':q,'inventory_policy':'deny','options':[f,fi],'sku':None} for i,(f,fi,p,a,q) in enumerate(vs)]
product={'title':'Wandpaneel Hout 811 Walnut Classic 8 mm Naadloos','handle':'811-hout-walnut-classic','url':'#','description':'<p>Beschrijving…</p>',
 'media':media,'featured_image':pack,'images':media,'variants':variants,'selected_or_first_available_variant':variants[0],'has_only_default_variant':False,
 'options_with_values':[{'name':'Formaat','values':[Val('260 cm x 122 cm',True),Val('280 cm x 122 cm')]},{'name':'Afwerking','values':[Val('5mm Stomp',True),Val('8mm Naadloos')]}],
 'metafields':{'custom':{'sibling_products':{'value':None}},'reviews':{},'puredeco':{'project_video':{'value':'proj.mp4'},'project_steps':{'value':'Op maat zagen@0|Plaatsen@2|Klaar@6.2'},'project_caption':{'value':'in een toilet'}}},
 'collections':[{'handle':'hout-1','title':'Hout','products_count':6,'url':'#','products':[{'title':'Wandpaneel Hout 810 Noir Oak','handle':'810','url':'#','featured_image':{'src':'wood.svg'},'price_min':13995,'price_varies':True,'options_with_values':[{'name':'Afwerking','values':['5mm Stomp','8mm Naadloos']}]},{'title':'Wandpaneel Hout 812 Walnut Deep','handle':'812','url':'#','featured_image':{'src':'wood.svg'},'price_min':13995,'price_varies':True,'options_with_values':[{'name':'Afwerking','values':['5mm Stomp','8mm Naadloos']}]},{'title':'Wandpaneel Hout 602 Wood Classic','handle':'602','url':'#','featured_image':{'src':'wood.svg'},'price_min':13995,'price_varies':True,'options_with_values':[{'name':'Afwerking','values':['5mm Stomp','8mm Naadloos']}]},{'title':'Wandpaneel Hout 607 Wood White Oak','handle':'607','url':'#','featured_image':{'src':'wood.svg'},'price_min':13995,'price_varies':True,'options_with_values':[{'name':'Afwerking','values':['5mm Stomp','8mm Naadloos']}]}]}]}
product['metafields']['custom']['sibling_products']={'value':product['collections'][0]['products']}; product['metafields']['custom']['sample_pairs']={'value':''}
shop={'enabled_payment_types':['ideal','klarna','visa','master','apple_pay','paypal'],'metafields':{'puredeco':{'montage_video':{'value':'film.mp4'},'montage_video_mobile':{'value':'filmp.mp4'}}}}
import glob as _g
for _i,_p in enumerate(product['collections'][0]['products']):
    _p.setdefault('available',True); _p.setdefault('selected_or_first_available_variant',{'id':900+_i})
_imgs={os.path.basename(f).replace('staal-','pd-staal-'):{'src':f,'width':600} for f in _g.glob('/home/user/baet/media/stalen/staal-*.jpg')}
ctx=dict(product=product, shop=shop, all_products={'eindprofielen':{'url':'#','price_min':2395}}, collection=None, images=_imgs)
def prep(src):
    src=re.sub(r'\{%\s*schema\s*%\}.*?\{%\s*endschema\s*%\}','',src,flags=re.S)
    src=re.sub(r"\{%-?\s*form 'product'[^%]*-?%\}",'<form id="pdh-form-S1" class="pdh__form" novalidate>',src)
    src=re.sub(r"\{%-?\s*form 'customer'[^%]*-?%\}",'<form class="pdf__form">',src)
    src=re.sub(r'\{%-?\s*endform\s*-?%\}','</form>',src)
    src=re.sub(r'\{%-?\s*render block\s*-?%\}','<button class="pde__cta" style="width:100%;border:0">[Product Samples-app] Sample aanvragen</button>',src)
    return src
out=''
for sec in ['pd-product-hero','pd-product-details']:
    src=prep(open(TH+f'sections/{sec}.liquid').read())
    out+=env.from_string(src).render(section={'id':'S1' if sec=='pd-product-hero' else 'S2','settings':{},'blocks':[{'type':'@app'}]}, **ctx)
def defaults(sec):
    s=json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}',open(TH+f'sections/{sec}.liquid').read(),re.S).group(1))
    return {x['id']:x.get('default','') for x in s.get('settings',[]) if 'id' in x}
L=lambda *n:{'links':[{'title':x,'url':'#'} for x in n]}
linklists={'pd-footer-collecties':L('Hout','Japandi','Leer','Art','Doorlopend marmer','Akupanelen','Accessoires'),
 'pd-footer-service':L('Gratis samples','Veelgestelde vragen','Bezorging en retour','Studio Herwen','Contact'),
 'pd-footer-zakelijk':L('Puredeco Projects','Zakelijk account','Inloggen zakelijk','Verkooppartners')}
fs=defaults('pd-footer'); fs.update(menu_1='pd-footer-collecties',menu_2='pd-footer-service',menu_3='pd-footer-zakelijk')
out+=env.from_string(prep(open(TH+'sections/pd-footer.liquid').read())).render(section={'id':'F1','settings':fs},linklists=linklists,form={},settings={'social_instagram_link':'#','social_pinterest_link':'#'},routes={'root_url':'/'},**ctx)
css=open(TH+'assets/puredeco-premium.css').read()
html=f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>@font-face{{font-family:'Cormorant';src:url(../film/cormorant.woff2);font-weight:300 700}}@font-face{{font-family:'Instrument Sans';src:url(../film/instrument.woff2);font-weight:400 700}}
html{{font-size:62.5%}}body{{margin:0;background:#F5F2EC;font-family:'Instrument Sans',sans-serif;font-size:1.5rem;color:#151413}}:root{{--font-heading-family:'Cormorant',Georgia,serif;--font-body-family:'Instrument Sans',sans-serif}}
*{{box-sizing:border-box}} img{{max-width:100%}} a{{color:inherit}} button{{font:inherit}}
.hdr{{height:64px;border-bottom:1px solid #DDD6CA;display:flex;align-items:center;justify-content:center;font-size:20px}}</style>
<style>{css}</style></head><body class="product-template"><div class="hdr">PureDeco (header theme)</div>{out}</body></html>'''
open('page.html','w').write(html)
print('ok', len(html))
