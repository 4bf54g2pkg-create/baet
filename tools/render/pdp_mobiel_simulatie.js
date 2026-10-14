const { chromium, devices } = require('playwright');
const fs=require('fs');
const OPT=process.argv[2]||'nu';
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const c=await b.newContext({...devices['iPhone 13']});
const p=await c.newPage();
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/811-hout-walnut-classic?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(4000);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
await p.evaluate((OPT)=>{
 document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove());
 if(OPT==='nu') return;
 const $=s=>document.querySelector(s);
 const css=document.createElement('style'); css.textContent=`
 /* basis voor alle opties */
 .section-breadcrumb{display:none!important}
 .header__search{display:none!important}
 .sim-search{display:flex;align-items:center;justify-content:center;width:44px;height:44px;background:none;border:0;padding:0;color:#151413}
 .pdh__stage{aspect-ratio:1/1!important;height:auto!important}
 .pdh__buy{display:grid!important;grid-template-columns:118px minmax(0,1fr)!important;gap:8px!important}
 .rez-mixed-stock-subtext-wrapper,.rez-mixed-stock-subtext,.rez-button-wrapper{display:none!important}
 .header-section{position:relative!important;top:auto!important}
 shopify-chat::part(activator){transform:translateY(-78px) scale(.86)}
 .pdh__qty{display:grid!important;grid-template-columns:34px minmax(0,1fr) 34px!important;padding:0!important}.pdh__qty input{width:100%!important;min-width:0!important}.pdh__qty button{width:34px!important;padding:0!important}
 .pdh__price{margin:8px 0 16px!important;padding:0 0 16px!important}
 .pdh__label{margin-bottom:10px!important}
 .pdh__qty{width:118px!important}.pdh__cta{min-width:0!important;width:100%!important}
 .pd-choice{display:none!important}
 .pdh__head{margin-bottom:0!important}.pdh__intro{display:none!important}
 .pdh__title{margin-bottom:4px!important}
 .pdh__finishes{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
 .pdh__fs-face{aspect-ratio:auto!important;height:78px!important}
 .pdh__finish-desc{display:none!important}
 .pdh__finish-text{gap:2px!important;padding-top:10px!important}
 .pdh__finish-name{font-size:22px!important;line-height:1.1!important}
 .pdh__finish-spec{font-size:12px!important;line-height:1.35!important}
 .pdh__finish-note{font-size:11.5px!important;margin-top:6px!important;line-height:1.4!important}
 .pdh__opt{margin-bottom:14px!important}
 .pd-usp-chips{display:grid!important;grid-template-columns:1fr 1fr;gap:6px!important}
 .pd-usp-chips li{justify-content:flex-start}
 .sim-calc{display:flex;align-items:center;gap:10px;width:100%;margin:10px 0 0;padding:13px 14px;border:1px solid #DDD6CA;background:#FBF9F5;font:inherit;font-size:14px;color:#151413;text-align:left}
 .sim-calc b{font-weight:600}.sim-calc span{margin-left:auto;font-size:18px}
 .sim-del{font-size:13px;line-height:1.45;margin:10px 0 0;color:#151413}
 .pdh__stock{margin:12px 0 0!important}
 .pdh__klarna{margin-top:8px!important}
 .pdh__bar{transform:none!important;opacity:1!important;visibility:visible!important;display:grid!important;grid-template-columns:auto minmax(0,1fr);gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom))!important;align-items:stretch;height:auto!important}
 .pdh__bar-name,.pdh__bar-price{display:none!important}
 .sim-bsmp{border:1px solid #151413;background:#FBF9F5;color:#151413;font:inherit;font-size:14px;padding:0 14px;height:50px;white-space:nowrap}
 .pdh__bar-cta{height:50px!important;width:100%!important;display:flex!important;align-items:center;justify-content:center;gap:8px;font-size:15px!important}
 body{padding-bottom:72px}
 `; document.head.appendChild(css);
 { const bar=$('.pdh__bar'); const bs=document.createElement('button'); bs.className='sim-bsmp'; bs.textContent='Gratis staal'; bar.prepend(bs);
   bar.querySelector('.pdh__bar-cta').innerHTML='In winkelmand <span style="opacity:.75" class="sim-bt">· € 179,95</span>'; }
 const icons=$('.header__icons--right'); if(icons){const s=document.createElement('button');s.className='sim-search';s.setAttribute('aria-label','Zoeken');s.innerHTML='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>';icons.prepend(s);}
 // kortere specs
 document.querySelectorAll('.pdh__finish').forEach(l=>{const sp=l.querySelector('.pdh__finish-spec'); if(l.dataset.finish==='sig') sp.textContent='8 mm · klik · naadloos*'; else sp.textContent='5 mm · stomp · zichtbare naad';});
 const fnote=$('.pdh__finish-note'); if(fnote) fnote.textContent='* Naadloos op een vlakke, rechte wand.';
 const inner=$('.pdh__inner'), form=$('.pdh__form'), buy=$('.pdh__buy'), calc=$('.pdc'), stock=$('.pdh__stock'), smp=$('.pdh-smp'), chips=$('.pd-usp-chips'), bend=$('.pd-usp-bend'), kl=$('.pdh__klarna'), price=$('.pdh__price');
 const fin=form.querySelector('.pdh__opt--finish'), fmt=[...form.querySelectorAll('fieldset.pdh__opt')].find(f=>!f.classList.contains('pdh__opt--finish'));
 // volgorde finish -> formaat
 fmt.before(fin); fin.after(fmt);
 const mkCalcBtn=()=>{const btn=document.createElement('button');btn.type='button';btn.className='sim-calc';btn.innerHTML='▦ <b>Hoeveel panelen heb ik nodig?</b><span>+</span>';return btn;};
 if(OPT==='D'){
   fmt.after(buy); buy.after(stock); stock.after(kl);
   form.after(smp); smp.style.marginTop='14px';
   const btn=mkCalcBtn(); smp.after(btn); btn.after(calc); calc.style.display='none';
   btn.after(chips); chips.style.marginTop='18px'; chips.after(bend);
 }
 if(OPT==='E'){
   const st=document.createElement('style'); st.textContent=`
    .pdc{padding:16px!important;margin:4px 0 12px!important}
    .pdc__preview,.pdc__note,.pdc__hint{display:none!important}
    .pdc__head{margin-bottom:8px!important}
    .pdc__fields{gap:12px!important;margin:8px 0 10px!important}
    .pdc__input input{font-size:26px!important}
    .pdc__stats{margin:0!important}
    .sim-ind{display:block;margin:10px 0 0;font-size:13px;color:#151413;text-decoration:underline;text-underline-offset:3px}`;
   document.head.appendChild(st);
   const h=calc.querySelector('.pdc__head .pdc__title, .pdc__head > *'); 
   fmt.after(calc); calc.after(buy); buy.after(stock); stock.after(kl);
   const ind=document.createElement('a'); ind.className='sim-ind'; ind.textContent='Bekijk de indeling van je wand ▾'; calc.querySelector('.pdc__stats').after(ind);
   form.after(smp); smp.style.marginTop='14px';
   smp.after(chips); chips.style.marginTop='18px'; chips.after(bend);
 }
 if(OPT==='F'){
   fmt.after(calc); calc.after(stock); stock.after(buy); buy.after(kl);
   form.after(smp); smp.style.marginTop='14px';
   smp.after(chips); chips.style.marginTop='18px'; chips.after(bend);
 }
},OPT);
await p.waitForTimeout(800);
if(process.argv[3]==='tint'){
  const inj=require('./tint-inject.js'); const data=JSON.parse(fs.readFileSync('tint-data.json','utf8'));
  await p.evaluate(`(${inj.toString()})(${JSON.stringify({data,desk:false})})`);
  await p.waitForTimeout(1500);
  const y1=await p.evaluate(()=>Math.round(document.querySelector('.pdh__title').getBoundingClientRect().top+scrollY)-120);
  await p.evaluate(y=>window.scrollTo(0,y),y1); await p.waitForTimeout(800); await p.screenshot({path:'tm-1.png'});
  const y2=await p.evaluate(()=>Math.round(document.querySelector('.tw').getBoundingClientRect().top+scrollY)-60);
  await p.evaluate(y=>window.scrollTo(0,y),y2); await p.waitForTimeout(1500); await p.screenshot({path:'tm-2.png'});
  await p.evaluate(()=>window.__twMode('vis')); await p.waitForTimeout(2500); await p.screenshot({path:'tm-3.png'});
  await p.evaluate((y)=>{window.__twMode('sw');document.querySelector('.tw__row').scrollLeft=640;window.scrollTo(0,y+250)},y2); await p.waitForTimeout(1200); await p.screenshot({path:'tm-4.png'});
  await b.close(); return;
}
if(process.argv[3]==='more'){
  const y=await p.evaluate(()=>Math.round(document.querySelector('.pd-more').getBoundingClientRect().top+scrollY)-170);
  for(let s=0;s<=y;s+=600){await p.evaluate(s=>window.scrollTo(0,s),s);await p.waitForTimeout(100);}
  await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(1500); await p.screenshot({path:'tm-nu.png'});
  await p.evaluate(y=>window.scrollTo(0,y+560),y); await p.waitForTimeout(1200); await p.screenshot({path:'tm-nu2.png'});
  await b.close(); return;
}
if(process.argv[3]==='full'){
  if(OPT==='E'){ await p.fill('[data-pdc-w]','4,80'); await p.fill('[data-pdc-h]','2,60'); await p.waitForTimeout(400); }
  // lazy beelden laden
  const H=await p.evaluate(()=>document.documentElement.scrollHeight);
  for(let y=0;y<H;y+=500){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(120); }
  await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(1200);
  const r=await p.evaluate(()=>{const bar=document.querySelector('.pdh__bar');const bh=bar?Math.round(bar.getBoundingClientRect().height):0;
    document.querySelectorAll('.pdh__bar,shopify-chat').forEach(e=>e.style.setProperty('display','none','important'));
    const he=document.querySelector('.pd-hero-section');const hr=he.getBoundingClientRect();
    const ft=document.querySelector('.shopify-section-group-footer-group, footer');
    return {heroEnd:Math.round(hr.bottom+scrollY),foot:ft?Math.round(ft.getBoundingClientRect().top+scrollY):document.documentElement.scrollHeight,bh}});
  console.log(OPT,'full',JSON.stringify(r));
  await p.screenshot({path:`mf-${OPT}.png`,fullPage:true});
  fs.writeFileSync(`mf-${OPT}.json`,JSON.stringify(r));
  await b.close(); return;
}
const m=await p.evaluate(()=>{const g=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();return Math.round(r.top+scrollY)};
 return {media:g('.pdh__media'),mediaEnd:Math.round(document.querySelector('.pdh__media').getBoundingClientRect().bottom+scrollY),title:g('.pdh__title'),price:g('.pdh__price'),cta:g('.pdh__cta'),ctaH:Math.round(document.querySelector('.pdh__cta').getBoundingClientRect().height),ctaR:Math.round(document.querySelector('.pdh__cta').getBoundingClientRect().right),smp:g('.pdh-smp'),vh:innerHeight,cta_txt:document.querySelector('.pdh__cta').innerText.replace(/\s+/g,' ')}});
console.log(OPT,JSON.stringify(m));
await p.screenshot({path:`ms-${OPT}-full.png`,fullPage:true});
const stops=OPT==="nu"?[0,640,1240,1840,2300]:[0, m.mediaEnd-140, m.mediaEnd-140+600];
for(let i=0;i<stops.length;i++){
  if(OPT==='E'&&i===2){ 
  await p.fill('[data-pdc-w]','4,80'); await p.fill('[data-pdc-h]','2,60'); await p.waitForTimeout(400);
  await p.evaluate(()=>{document.querySelector('.sim-bt').textContent='· '+document.querySelector('[data-pdh-total]').textContent;});

    const y=await p.evaluate(()=>Math.round(document.querySelector('.pdc').getBoundingClientRect().top+scrollY)-60); stops[i]=y; }
  await p.evaluate(y=>window.scrollTo(0,y),stops[i]); await p.waitForTimeout(900); await p.screenshot({path:`ms-${OPT}-s${i+1}.png`}); }
await b.close();})();
