const { chromium, devices } = require('playwright');
const fs=require('fs');
const DEV=process.argv[2]||'m', H=process.argv[3]||'812-hout-walnut-deep';
(async()=>{
const b=await chromium.launch({channel:'chromium',proxy:{server:process.env.HTTPS_PROXY},args:['--ignore-certificate-errors-spki-list='+fs.readFileSync('spki.txt','utf8').trim()]});
const c=await b.newContext(DEV==='m'?{...devices['iPhone 13']}:{viewport:{width:1440,height:1000}});
const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
for(let i=0;i<3;i++){await p.goto('https://puredeco.nl/products/'+H+'?preview_theme_id=194824929546',{waitUntil:'load',timeout:90000});await p.waitForTimeout(4000);if(!(await p.title()).includes('Just a moment'))break;await p.waitForTimeout(15000);}
await p.evaluate(()=>document.querySelectorAll('#shopify-pc__banner,#PBarNextFrameWrapper').forEach(x=>x.remove()));
console.log(H, JSON.stringify(await p.evaluate(()=>({line:(document.querySelector('.pdr-line')||{}).innerText,own:(document.querySelector('.pdh__rating')||{}).innerText,
 n:document.querySelectorAll('.pdr__c').length, sum:(document.querySelector('.pdr__sum')||{}).innerText, first:[...document.querySelectorAll('.pdr__c')].slice(0,9).map(c=>c.innerText.replace(/\s+/g,' ').slice(0,110))}))),null,1);
const t=await p.evaluate(()=>document.querySelector('.pdh__title').getBoundingClientRect().top+scrollY-(innerWidth<990?140:260));
await p.evaluate(y=>scrollTo(0,y),t); await p.waitForTimeout(800); await p.screenshot({path:`rt-${DEV}-1.png`});
const y=await p.evaluate(()=>document.querySelector('#pd-reviews').getBoundingClientRect().top+scrollY);
for(let s=t;s<y;s+=600){await p.evaluate(s=>scrollTo(0,s),s);await p.waitForTimeout(80);}
await p.evaluate(y=>scrollTo(0,y-40),y); await p.waitForTimeout(1500); await p.screenshot({path:`rt-${DEV}-2.png`});
console.log('errors',errs);
await b.close();})();
