const { chromium } = require('playwright');
const fs=require('fs');
const MODE=process.argv[2]||'new';
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const p=await (await b.newContext({viewport:{width:1440,height:1000}})).newPage();
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/811-hout-walnut-classic?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(3500);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
await p.evaluate(()=>document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove()));
const H=await p.evaluate(()=>document.documentElement.scrollHeight);
for(let y=0;y<H;y+=700){await p.evaluate(y=>window.scrollTo(0,y),y);await p.waitForTimeout(100);}
if(MODE==='new'){ const inj=require('./tint-inject.js'); const data=JSON.parse(fs.readFileSync('tint-data.json','utf8'));
  await p.evaluate(`(${inj.toString()})(${JSON.stringify({data,desk:true})})`); await p.waitForTimeout(1500);
  await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(800);
  await p.screenshot({path:'td-top.png'});
  const r=await p.evaluate(()=>{const e=document.querySelector('.tw');const r=e.getBoundingClientRect();return {y:Math.round(r.top+scrollY),h:Math.round(r.height)}});
  await p.evaluate(y=>window.scrollTo(0,y),r.y-100); await p.waitForTimeout(1500);
  Object.assign(r,await p.evaluate(()=>{const e=document.querySelector('.tw');const q=e.getBoundingClientRect();return {y:Math.round(q.top+scrollY),h:Math.round(q.height)}}));
  await p.screenshot({path:'td-tw.png',clip:{x:0,y:r.y,width:1440,height:Math.min(r.h,1000)},fullPage:true});
  await p.evaluate(()=>window.__twMode('vis')); await p.waitForTimeout(2500);
  await p.screenshot({path:'td-tw2.png',clip:{x:0,y:r.y,width:1440,height:Math.min(r.h,1000)},fullPage:true});
} else {
  const r=await p.evaluate(()=>{const e=document.querySelector('.pd-more');const r=e.getBoundingClientRect();return {y:Math.round(r.top+scrollY),h:Math.round(r.height)}});
  await p.evaluate(y=>window.scrollTo(0,y),r.y-100); await p.waitForTimeout(1500);
  await p.screenshot({path:'td-nu.png',clip:{x:0,y:r.y,width:1440,height:Math.min(r.h,1000)},fullPage:true});
}
await b.close();})();
