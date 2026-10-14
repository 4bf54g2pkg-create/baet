const { chromium, devices } = require('playwright');
const fs=require('fs');
const DEV=process.argv[2]||'m';
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const c=await b.newContext(DEV==='m'?{...devices['iPhone 13']}:{viewport:{width:1440,height:1000}});
const p=await c.newPage();
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/811-hout-walnut-classic?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(4000);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
const H0=await p.evaluate(()=>document.documentElement.scrollHeight);
for(let y=0;y<H0;y+=600){await p.evaluate(y=>window.scrollTo(0,y),y);await p.waitForTimeout(90);}
await p.evaluate(()=>window.scrollTo(0,0));
await p.evaluate((M)=>{
 document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove());
 const $=s=>document.querySelector(s);
 const mob=`
 .section-breadcrumb{display:none!important}
 .header__search{display:none!important}
 .sim-search{display:flex;align-items:center;justify-content:center;width:44px;height:44px;background:none;border:0;padding:0;color:#151413}
 .header-section{position:relative!important;top:auto!important}
 .pdh__stage{aspect-ratio:1/1!important;height:auto!important}
 shopify-chat::part(activator){transform:translateY(-78px) scale(.86)}
 .pdh__intro{display:none!important}
 .pdh__bar{transform:none!important;opacity:1!important;visibility:visible!important;display:grid!important;grid-template-columns:auto minmax(0,1fr);gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom))!important;align-items:stretch;height:auto!important}
 .pdh__bar-name,.pdh__bar-price{display:none!important}
 .sim-bsmp{display:flex;align-items:center;gap:8px;border:1px solid #151413;background:#FBF9F5;color:#151413;font:inherit;font-size:14px;padding:0 12px 0 6px;height:50px;white-space:nowrap}
 .sim-bsmp img{width:36px;height:36px;object-fit:cover;display:block}
 .pdh__bar-cta{height:50px!important;width:100%!important;display:flex!important;align-items:center;justify-content:center;gap:8px;font-size:15px!important}
 body{padding-bottom:72px}`;
 const css=document.createElement('style'); css.textContent=`
 .rez-mixed-stock-subtext-wrapper,.rez-mixed-stock-subtext,.rez-button-wrapper{display:none!important}
 .pdh__buy{display:grid!important;grid-template-columns:118px minmax(0,1fr)!important;gap:8px!important}
 .pdh__qty{width:118px!important;display:grid!important;grid-template-columns:34px minmax(0,1fr) 34px!important;padding:0!important}.pdh__qty input{width:100%!important;min-width:0!important}.pdh__qty button{width:34px!important;padding:0!important}
 .pdh__cta{min-width:0!important;width:100%!important}
 .pd-choice{display:none!important}
 .pdh__head{margin-bottom:0!important}.pdh__title{margin-bottom:4px!important}
 .pdh__price{margin:8px 0 16px!important;padding:0 0 16px!important}
 .pdh__label{margin-bottom:10px!important}
 .pdh__finishes{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
 .pdh__fs-face{aspect-ratio:auto!important;height:78px!important}
 .pdh__finish-desc{display:none!important}
 .pdh__finish-text{gap:2px!important;padding-top:10px!important}
 .pdh__finish-name{font-size:22px!important;line-height:1.1!important}
 .pdh__finish-spec{font-size:12px!important;line-height:1.35!important}
 .pdh__finish-note{font-size:11.5px!important;margin-top:6px!important;line-height:1.4!important}
 .pdh__opt{margin-bottom:14px!important}
 .pd-usp-chips{display:grid!important;grid-template-columns:1fr 1fr;gap:6px!important}
 .pdh__stock{margin:12px 0 0!important}.pdh__klarna{margin-top:8px!important}
 .pdc{padding:16px!important;margin:4px 0 12px!important}
 .pdc__preview,.pdc__note,.pdc__hint{display:none!important}
 .pdc__head{margin-bottom:8px!important}.pdc__fields{gap:12px!important;margin:8px 0 10px!important}
 .pdc__input input{font-size:26px!important}.pdc__stats{margin:0!important}
 .sim-ind{display:block;margin:10px 0 0;font-size:13px;color:#151413;text-decoration:underline;text-underline-offset:3px}
 .sim-vis{position:absolute;left:12px;top:12px;font-size:10.5px;letter-spacing:.1em;background:rgba(245,242,236,.92);color:#3A3733;padding:4px 8px;z-index:2}
 .pdh__slide{position:relative}
 .tn__note{font-size:11.5px;color:#6E675E;margin:6px 0 0}
 ${M==='m'?mob:''}`; document.head.appendChild(css);
 if(M==='m'){const icons=$('.header__icons--right'); if(icons){const s=document.createElement('button');s.className='sim-search';s.innerHTML='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>';icons.prepend(s);}
   const bar=$('.pdh__bar'); const bs=document.createElement('button'); bs.className='sim-bsmp'; bs.innerHTML='<img src="/cdn/shop/files/pd-staal-811.jpg?width=120" alt="">Gratis staal'; bar.prepend(bs);
   bar.querySelector('.pdh__bar-cta').innerHTML='In winkelmand <span style="opacity:.75" class="sim-bt">· € 179,95</span>';}
 // Visualisatie-label op gegenereerde interieurbeelden
 document.querySelectorAll('.pdh__slide img').forEach(i=>{ if(/generated/.test(i.currentSrc||i.src)){const l=document.createElement('span');l.className='sim-vis';l.textContent='Visualisatie';i.parentElement.appendChild(l);} });
 document.querySelectorAll('.pdh__finish').forEach(l=>{const sp=l.querySelector('.pdh__finish-spec'); if(l.dataset.finish==='sig') sp.textContent='8 mm · klik · naadloos*'; else sp.textContent='5 mm · stomp · zichtbare naad';});
 const fnote=$('.pdh__finish-note'); if(fnote) fnote.textContent='* Naadloos op een vlakke, rechte wand.';
 const form=$('.pdh__form'), buy=$('.pdh__buy'), calc=$('.pdc'), stock=$('.pdh__stock'), smp=$('.pdh-smp'), chips=$('.pd-usp-chips'), bend=$('.pd-usp-bend'), kl=$('.pdh__klarna');
 const fin=form.querySelector('.pdh__opt--finish'), fmt=[...form.querySelectorAll('fieldset.pdh__opt')].find(f=>!f.classList.contains('pdh__opt--finish'));
 fmt.before(fin); fin.after(fmt);
 fmt.after(calc); calc.after(buy); buy.after(stock); stock.after(kl);
 const ind=document.createElement('a'); ind.className='sim-ind'; ind.textContent='Bekijk de indeling van je wand ▾'; calc.querySelector('.pdc__stats').after(ind);
 form.after(smp); smp.style.marginTop='14px'; smp.after(chips); chips.style.marginTop='18px'; chips.after(bend);
},DEV);
const inj=require('./tint-inject.js'); const data=JSON.parse(fs.readFileSync('tint-data2.json','utf8'));
await p.evaluate(`(${inj.toString()})(${JSON.stringify({data,desk:DEV!=='m'})})`);
await p.evaluate(()=>{const n=document.createElement('p');n.className='tn__note';n.textContent='607, 602 en 615 zijn er alleen als Linea (5 mm).';document.querySelector('.tn').appendChild(n);
 const f=document.querySelector('.tw__ft');const d=document.createElement('p');d.style.cssText='font-size:12px;color:#8C857A;margin:10px 0 0';d.textContent='Kleuren op een scherm kunnen afwijken. Een staal laat het echte decor zien.';f.after(d);});
await p.fill('[data-pdc-w]','4,80'); await p.fill('[data-pdc-h]','2,60'); await p.waitForTimeout(500);
if(DEV==='m') await p.evaluate(()=>{document.querySelector('.sim-bt').textContent='· '+document.querySelector('[data-pdh-total]').textContent;});
await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(1500);
const g=s=>p.evaluate(s=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();return {y:Math.round(r.top+scrollY),b:Math.round(r.bottom+scrollY)}},s);
if(DEV==='m'){
  const t=await g('.pdh__title'), tw=await g('.tw'), cta=await g('.pdh__cta');
  const stops=[0,t.y-130,cta.y-330,tw.y-60];
  for(let i=0;i<stops.length;i++){await p.evaluate(y=>window.scrollTo(0,y),stops[i]);await p.waitForTimeout(1000);await p.screenshot({path:`fm-s${i+1}.png`});}
  await p.evaluate(()=>{document.querySelectorAll('.pdh__bar,shopify-chat').forEach(e=>e.style.setProperty('display','none','important'));window.scrollTo(0,0)}); await p.waitForTimeout(800);
  const he=await g('.pd-hero-section'); await p.screenshot({path:'fm-full.png',fullPage:true}); fs.writeFileSync('fm.json',JSON.stringify({he,tw,cta}));
  console.log(JSON.stringify({he,tw,cta}));
} else {
  await p.screenshot({path:'fd-1.png'});
  const he=await g('.pd-hero-section'); await p.setViewportSize({width:1440,height:he.b+20}); await p.waitForTimeout(800);
  await p.screenshot({path:'fd-col.png',clip:{x:840,y:180,width:600,height:he.b-180}});
  await p.setViewportSize({width:1440,height:1000}); const tw=await g('.tw'); await p.evaluate(y=>window.scrollTo(0,y-100),tw.y); await p.waitForTimeout(1500);
  const tw2=await g('.tw'); await p.screenshot({path:'fd-tw.png',clip:{x:0,y:tw2.y,width:1440,height:tw2.b-tw2.y},fullPage:true});
  console.log(JSON.stringify({he,tw2}));
}
await b.close();})();
