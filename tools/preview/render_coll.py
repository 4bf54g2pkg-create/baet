# Lokale weergave van de collectiepagina (pd-collection) met de houtcollectie en beelden uit de beeldbank.
import re, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from liquid import Environment, CachingFileSystemLoader
from markupsafe import Markup
TH='/home/user/baet/theme-h1/'; BB='/home/user/baet/media/beeldbank/'
os.makedirs('snips',exist_ok=True)
for f in os.listdir(TH+'snippets'):
    if f.startswith('pd-'): open('snips/'+f,'w').write(open(TH+'snippets/'+f).read())
env=Environment(loader=CachingFileSystemLoader('snips', ext='.liquid'), autoescape=False)
env.add_filter('image_url', lambda img, **k: '' if img is None else (img['src'] if isinstance(img,dict) else str(img)))
env.add_filter('image_tag', lambda u, **k: Markup(f'<img src="{u}" alt="{k.get("alt","")}" class="{k.get("class","")}" loading="lazy">'))
env.add_filter('money', lambda c: '€ ' + f"{c/100:.2f}".replace('.',','))
env.add_filter('json', lambda v: json.dumps(v, ensure_ascii=False))
env.add_filter('handle', lambda s: str(s).lower().replace(' ','-'))
def P(handle,title,files,price,cmp,opts,varies=False):
    m=[{'src':BB+f} for f in files if os.path.exists(BB+f)]
    return {'handle':handle,'title':title,'url':'#','media':m,'featured_image':m[0],'price_min':price,'price_varies':varies,'compare_at_price_max':cmp,
            'selected_or_first_available_variant':{'id':str(abs(hash(handle))%10**9)},'options_with_values':[{'name':k,'values':v} for k,v in opts]}
def F(code): return [f for f in sorted(os.listdir(BB)) if f.startswith(code+'-')]
prods=[P('602','Wandpaneel Hout 602 Wood Classic',F('602'),9995,12495,[('Formaat',['280 × 122 cm']),('Afwerking',['5mm Stomp'])]),
       P('607','Wandpaneel Hout 607 Wood White Oak',F('607'),9995,12495,[('Formaat',['280 × 122 cm']),('Afwerking',['5mm'])]),
       P('615','Wandpaneel Hout 615 Wood Radiata',F('615'),8995,12495,[('Formaat',['280 × 122 cm']),('Afwerking',['5mm Stomp'])]),
       P('810','Wandpaneel Hout 810 Noir Oak',F('810'),13995,0,[('Formaat',['260 cm x 122 cm','280 cm x 122 cm']),('Afwerking',['5mm Stomp','8mm Naadloos'])],True),
       P('811','Wandpaneel Hout 811 Walnut Classic 8 mm Naadloos',F('811'),13995,0,[('Formaat',['260 cm x 122 cm','280 cm x 122 cm']),('Afwerking',['5mm Stomp','8mm Naadloos'])],True),
       P('812','Wandpaneel Hout 812 Walnut Deep',F('812'),13995,0,[('Formaat',['280 cm x 122 cm']),('Afwerking',['8mm Naadloos','5mm Stomp'])],True)]
desc='<p>Onze houtlook wandpanelen brengen de warmte van massief hout in huis, zonder de nadelen: geen onderhoud met olie of lak, geen kans op kromtrekken door vocht.</p><div class="x" data-a="1"><section class="y"><p data-start="0">Elk paneel heeft een realistische <strong>houtnerf</strong>-textuur.</p><ul><li data-x="1">Buigbaar</li><li>Sterke bamboekern</li></ul><form class="z"></form></section></div>'
coll={'title':'Hout','handle':'hout-1','url':'#','description':desc,'products':prods,'products_count':6,'image':{'src':BB+'812-1.png'},
      'metafields':{'custom':{'seo_h1':{'value':'Houten wandpanelen'}}},
      'filters':[{'type':'list','label':'Afwerking','values':[{'label':'5 mm stomp','count':6,'active':False,'url_to_add':'#'},{'label':'8 mm naadloos','count':3,'active':True,'url_to_remove':'#'}],'active_values':[1]}],
      'sort_options':[{'value':'manual','name':'Uitgelicht'},{'value':'price-ascending','name':'Prijs, laag naar hoog'}],'default_sort_by':'manual','sort_by':None}
src=open(TH+'sections/pd-collection.liquid').read()
schema=json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}',src,re.S).group(1))
src=re.sub(r'\{%\s*schema\s*%\}.*?\{%\s*endschema\s*%\}','',src,flags=re.S)
src=re.sub(r'\{%-?\s*paginate[^%]*-?%\}|\{%-?\s*endpaginate\s*-?%\}','',src)
tpl=json.load(open(TH+'templates/collection.json'))['sections']['pd_collection']
blocks=[dict(id=k,type=v['type'],settings=v['settings'],shopify_attributes='') for k,v in tpl['blocks'].items()]
out=env.from_string(src).render(section={'settings':tpl['settings'],'blocks':blocks},collection=coll,paginate={'pages':1,'current_offset':0},canonical_url='https://puredeco.nl/collections/hout-1',request={'origin':'https://puredeco.nl'},page_description='Houtlook wandpanelen met bamboekern')
css=open(TH+'assets/puredeco-premium.css').read()
html=f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>@font-face{{font-family:'Cormorant';src:url(../film/cormorant.woff2);font-weight:300 700}}@font-face{{font-family:'Instrument Sans';src:url(../film/instrument.woff2);font-weight:400 700}}
html{{font-size:62.5%}}body{{margin:0;background:#F5F2EC;font-family:'Instrument Sans',sans-serif;font-size:1.5rem;color:#151413}}:root{{--font-heading-family:'Cormorant',Georgia,serif}}
.hdr{{height:64px;border-bottom:1px solid #DDD6CA;display:flex;align-items:center;justify-content:center;font-size:20px}}</style>
<style>{css}</style></head><body class="template-collection"><div class="hdr">PureDeco (header theme)</div><div style="padding:16px 96px;font-size:13px;color:#6E675E">Home / Hout</div>{out}</body></html>'''
open('page.html','w').write(html); print('ok',len(html))
