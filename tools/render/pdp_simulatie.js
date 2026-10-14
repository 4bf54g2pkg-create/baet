const { chromium, devices } = require('playwright');
const fs=require('fs');
const OPT=process.argv[2]||'nu', DEV=process.argv[3]||'d';
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const c=await b.newContext(DEV==='m'?{...devices['Pixel 5']}:{viewport:{width:1440,height:1000}});
const p=await c.newPage();
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/811-hout-walnut-classic?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(3500);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
await p.evaluate((OPT)=>{
 document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove());
 if(OPT==='nu') return;
 const css=document.createElement('style'); css.textContent=`
  .pdh__buy{grid-template-columns:auto minmax(0,1fr)!important}
  .pdh__buy .rez-mixed-stock-subtext-wrapper,.pdh__buy .rez-button-wrapper{display:none!important}
  .pdh__cta{min-width:0}
  @media(min-width:990px){.pdh__media{position:sticky;top:96px;align-self:start}}
  .pdh__finish-swatch{height:110px!important;overflow:hidden}
  .sim-calc{display:flex;align-items:center;gap:10px;width:100%;margin:12px 0 0;padding:14px 16px;border:1px solid #DDD6CA;background:#FBF9F5;font:inherit;font-size:14px;color:#151413;text-align:left;cursor:pointer}
  .sim-calc b{font-weight:600}.sim-calc span{margin-left:auto;font-size:18px}
  .sim-two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px;margin-top:10px}.sim-two .pdh-smp{overflow:hidden;width:100%}
  .pd-choice{display:none!important}
 `; document.head.appendChild(css);
 const form=document.querySelector('.pdh__form'), buy=document.querySelector('.pdh__buy'), calc=document.querySelector('.pdc'), stock=document.querySelector('.pdh__stock'), smp=document.querySelector('.pdh-smp'), segs=[...form.querySelectorAll('fieldset.pdh__opt')].find(f=>!f.classList.contains('pdh__opt--finish'));
 const cta=document.querySelector('.pdh__cta');
 document.querySelectorAll('.pdh__buy .rez-mixed-stock-subtext-wrapper,.pdh__buy .rez-button-wrapper').forEach(e=>e.style.display='none');
 document.querySelector('.pdh__qty').style.width='max-content';
 if(OPT==='A'||OPT==='C'){
   document.querySelectorAll('.pdh__finish-text *').forEach(e=>{ if(getComputedStyle(e).fontStyle==='italic') e.style.display='none'; });
   const fn=document.querySelector('.pdh__finish-note'); if(fn) fn.style.display='none';
   const bend=document.querySelector('.pd-usp-bend'); if(bend) bend.style.display='none';
   const st2=document.createElement('style'); st2.textContent=`.pdh__finish{display:grid!important;grid-template-columns:76px 1fr;gap:12px;align-items:center;padding:8px!important}
    .pdh__finish-swatch{height:76px!important;width:76px!important;overflow:hidden;display:block}
    
    .pdh__fs-sec{display:none!important} .pdh__fs-face{height:100%!important;aspect-ratio:auto!important;width:100%!important}
    .pdh__finish-text{padding:0!important}
    .pdh__head{margin-bottom:0}
    @media(min-width:990px){.pdh__inner{padding-top:24px!important}}`; document.head.appendChild(st2);
   const chips=document.querySelector('.pd-usp-chips'); if(chips){ chips.dataset.move='1'; }
   const after=segs; after.after(buy);
   const btn=document.createElement('button'); btn.type='button'; btn.className='sim-calc'; btn.innerHTML='▦ <b>Hoeveel panelen heb ik nodig?</b> Bereken voor je wand <span>+</span>';
   buy.after(btn); btn.after(calc); calc.style.display='none';
   btn.after(stock); 
   if(OPT==='A'){ stock.after(smp); const ch=document.querySelector('.pd-usp-chips'); if(ch) smp.after(ch); }

   if(OPT==='C'){ // staal en knop even groot naast elkaar, aantal erboven
     const two=document.createElement('div'); two.className='sim-two'; buy.after(two); two.appendChild(smp); two.appendChild(cta);
     smp.style.margin='0'; smp.style.minWidth='0'; cta.style.minWidth='0'; cta.style.height='auto'; buy.style.gridTemplateColumns='max-content';
   }
 }
 if(OPT==='B'){
   calc.querySelector('.pdc__preview').style.display='none'; calc.querySelector('.pdc__note').style.display='none';
   if(cta) cta.textContent='4 panelen in winkelmand · € 719,80';
   buy.after(smp);
 }
},OPT);
await p.waitForTimeout(800);
const name=`sim-${OPT}-${DEV}.png`;
if(DEV==='d'){ await p.screenshot({path:name}); await p.setViewportSize({width:1440,height:2400}); await p.waitForTimeout(500); await p.screenshot({path:`sim-${OPT}-d-col.png`,clip:{x:840,y:195,width:600,height:2100}}); }
else { await p.setViewportSize({width:393,height:851}); await p.screenshot({path:name,fullPage:true}); }
const ctaInfo=await p.evaluate(()=>{const c=document.querySelector('.pdh__cta');const r=c.getBoundingClientRect();return {y:Math.round(r.top+scrollY),right:Math.round(r.right),vw:innerWidth,w:Math.round(r.width)}});
console.log(OPT,DEV,JSON.stringify(ctaInfo));
await b.close();})();
