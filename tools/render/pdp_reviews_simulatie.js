const { chromium, devices } = require('playwright');
const fs=require('fs');
const DEV=process.argv[2]||'m';
const R=[["Martijn V.","Eerst in de showroom wezen kijken. Goed geholpen en in het echt zijn de panelen nog mooier dan op de foto's."],
["Erik van Dijk","Voor ons kantoor wandpanelen uitgezocht. Netjes advies gekregen en de ruimte ziet er een stuk strakker uit."],
["Sandra K.","We waren al bij meerdere winkels geweest maar vonden deze toch echt het mooist. Vooral de afwerking is een stuk beter."],
["Michael B.","Voor een zakelijk project verschillende leveranciers vergeleken. Deze panelen sprongen er qua uitstraling echt uit."],
["Richard B.","Zelf gemonteerd afgelopen weekend. Was eigenlijk makkelijker dan gedacht. Bedankt voor de tips!"],
["Linda K.","Voor onze salon op zoek geweest naar iets moois voor achter de balie. Erg tevreden met het resultaat."],
["Fatima E.","Fijn geholpen in de showroom, ze namen rustig de tijd. Uiteindelijk een hele mooie kleur uitgezocht."],
["Peter H.","Als interieurbouwer kijk ik vooral naar de afwerking. Mooie panelen en prettig contact gehad."],
["Dennis R.","Heb bij verschillende aanbieders gekeken maar deze panelen zijn toch van een ander niveau. Zeker qua afwerking."],
["Monique S.","We twijfelden tussen twee kleuren. Gelukkig even langsgegaan om ze in het echt te bekijken. Dat maakte de keuze een stuk makkelijker."]];
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const c=await b.newContext(DEV==='m'?{...devices['iPhone 13']}:{viewport:{width:1440,height:1000}});
const p=await c.newPage();
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/812-hout-walnut-deep?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(4000);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
await p.evaluate((R)=>{
 document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove());
 const serif=getComputedStyle(document.querySelector('.pdh__title')).fontFamily;
 const desk=innerWidth>=990;
 const css=document.createElement('style'); css.textContent=`
 .rv-tag{display:inline-block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;background:#9B3D2E;color:#fff;padding:3px 7px;margin-left:8px;vertical-align:middle}
 .rv-star{display:flex;align-items:center;gap:8px;margin:6px 0 2px;font-size:13.5px;color:#151413;text-decoration:none}
 .rv-star .s{color:#151413;letter-spacing:2px;font-size:14px}
 .rv-star u{text-underline-offset:3px;color:#3A3733}
 .rv{background:#EFEAE1;padding:${desk?'88px 0':'56px 0'}}
 .rv__top{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;margin-bottom:22px}
 .rv__k{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A;margin:0 0 8px}
 .rv__t{font-family:${serif};font-weight:400;font-size:${desk?'48px':'34px'};line-height:1.05;margin:0;color:#151413}
 .rv__sum{display:flex;align-items:center;gap:14px}
 .rv__big{font-family:${serif};font-size:${desk?'56px':'44px'};line-height:1;color:#151413}
 .rv__sum .s{letter-spacing:3px;font-size:16px;color:#151413}.rv__sum small{display:block;font-size:12.5px;color:#6E675E;margin-top:2px}
 .rv__row{display:grid;${desk?'grid-template-columns:repeat(3,1fr);gap:16px':'grid-auto-flow:column;grid-auto-columns:82%;gap:12px;overflow-x:auto;margin-right:-20px;padding-right:20px;scrollbar-width:none'}}
 .rv__c{background:#FBF9F5;border:1px solid #E4DDD1;padding:20px;display:flex;flex-direction:column;gap:10px}
 .rv__c .s{letter-spacing:2px;font-size:13px;color:#151413}
 .rv__q{font-family:${serif};font-size:${desk?'21px':'20px'};line-height:1.35;color:#151413;margin:0}
 .rv__n{margin-top:auto;font-size:13px;color:#3A3733}.rv__n b{font-weight:600;color:#151413}
 .rv__ft{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-top:20px;font-size:13.5px}
 .rv__ft button{font:inherit;font-size:13.5px;padding:11px 16px;border:1px solid #151413;background:transparent;color:#151413}
 .rv__src{font-size:12px;color:#6E675E}`; document.head.appendChild(css);
 // sterren onder de titel
 const t=document.querySelector('.pdh__title');
 const a=document.createElement('a'); a.className='rv-star'; a.href='#rv';
 a.innerHTML='<span class="s">★★★★★</span><b>5,0</b><u>10 reviews over Puredeco</u><span class="rv-tag">Voorbeeld</span>';
 t.after(a);
 // sectie
 const sec=document.createElement('section'); sec.className='pd-s rv'; sec.id='rv';
 const cards=R.slice(0,desk?6:10).map(r=>`<article class="rv__c"><span class="s">★★★★★</span><p class="rv__q">“${r[1]}”</p><p class="rv__n"><b>${r[0]}</b></p></article>`).join('');
 sec.innerHTML=`<div class="pd-wrap"><div class="rv__top"><div><p class="rv__k">Reviews <span class="rv-tag">Voorbeeld · niet gepubliceerd</span></p><h2 class="rv__t">Wat klanten zeggen</h2></div><div class="rv__sum"><span class="rv__big">5,0</span><div><span class="s">★★★★★</span><small>op basis van 10 reviews over Puredeco</small></div></div></div><div class="rv__row">${cards}</div><div class="rv__ft"><span class="rv__src">Reviews via Judge.me</span>${desk?'<button type="button">Toon alle 10 reviews</button>':''}</div></div>`;
 const faq=document.querySelector('.pd-faq'); faq.before(sec);
},R);
await p.waitForTimeout(1200);
const g=s=>p.evaluate(s=>Math.round(document.querySelector(s).getBoundingClientRect().top+scrollY),s);
const ty=await g('.pdh__title'); await p.evaluate(y=>scrollTo(0,y-(innerWidth<990?140:260)),ty); await p.waitForTimeout(900);
await p.screenshot({path:`rv-${DEV}-1.png`});
const ry=await g('#rv'); 
for(let s=ty;s<ry;s+=600){await p.evaluate(s=>scrollTo(0,s),s);await p.waitForTimeout(80);}
await p.evaluate(y=>scrollTo(0,y-(innerWidth<990?40:60)),ry); await p.waitForTimeout(1200);
await p.screenshot({path:`rv-${DEV}-2.png`});
if(DEV==='m'){await p.evaluate(()=>document.querySelector('.rv__row').scrollLeft=330);await p.waitForTimeout(600);await p.screenshot({path:`rv-${DEV}-3.png`});}
await b.close();})();
