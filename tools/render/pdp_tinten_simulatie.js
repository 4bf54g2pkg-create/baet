module.exports = function(arg){
 const D=arg.data, cur='811', desk=arg.desk;
 const serif=getComputedStyle(document.querySelector('.pdh__title')).fontFamily;
 const css=document.createElement('style'); css.textContent=`
 .tn{margin:4px 0 22px;padding:0 0 18px;border-bottom:1px solid #E4DDD1}
 .tn__h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px}
 .tn__h span{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#6E675E}
 .tn__h b{font-weight:500;font-size:13px;color:#151413}
 .tn__sw{display:grid;grid-template-columns:repeat(6,1fr);gap:7px}
 .tn__s{display:block;aspect-ratio:1;position:relative;outline:1px solid rgba(0,0,0,.08);outline-offset:-1px}
 .tn__s img{width:100%;height:100%;object-fit:cover;display:block}
 .tn__s.is{outline:2px solid #151413;outline-offset:2px}
 .tn__sc{display:flex;justify-content:space-between;font-size:11px;color:#8C857A;margin-top:7px}
 .tn__sc i{flex:1;height:1px;margin:7px 8px 0;background:linear-gradient(90deg,#CDBBA2,#2A1D12)}
 .tw{padding:${desk?'88px 0':'56px 0'};background:#F5F2EC}
 .tw__top{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;margin-bottom:${desk?'26px':'18px'}}
 .tw__k{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#8C6A4A;margin:0 0 8px}
 .tw__t{font-family:${serif};font-weight:400;font-size:${desk?'48px':'36px'};line-height:1.05;margin:0;color:#151413}
 .tw__lead{font-size:14.5px;line-height:1.6;color:#3A3733;margin:10px 0 0;max-width:520px}
 .tw__tg{display:inline-flex;border:1px solid #151413}
 .tw__tg button{font:inherit;font-size:13px;padding:9px 14px;background:transparent;border:0;color:#151413}
 .tw__tg button.on{background:#151413;color:#F5F2EC}
 .tw__scale{display:flex;align-items:center;gap:10px;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#6E675E;margin:0 0 14px}
 .tw__scale i{flex:1;height:2px;background:linear-gradient(90deg,#CDBBA2,#9C9690 35%,#7B4E3F 70%,#21160D)}
 .tw__row{display:grid;${desk?'grid-template-columns:repeat(6,1fr);gap:16px':'grid-auto-flow:column;grid-auto-columns:46%;gap:12px;overflow-x:auto;margin-right:-20px;padding-right:20px;scrollbar-width:none'}}
 .tw__c{display:flex;flex-direction:column;text-decoration:none;color:#151413;background:#fff;border:1px solid #E4DDD1}
 .tw__c.is{border-color:#151413;box-shadow:inset 0 0 0 1px #151413}
 .tw__im{position:relative;aspect-ratio:${desk?'3/4':'1/1'};overflow:hidden;background:#EFEAE1}
 .tw__im img{width:100%;height:100%;object-fit:cover;display:block}
 .tw__b{position:absolute;left:8px;top:8px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;background:#151413;color:#F5F2EC;padding:4px 7px}
 .tw__v{position:absolute;right:8px;bottom:8px;font-size:10px;letter-spacing:.08em;background:rgba(245,242,236,.92);color:#3A3733;padding:3px 6px}
 .tw__tx{padding:12px 12px 14px;display:flex;flex-direction:column;gap:2px;flex:1}
 .tw__code{font-size:11px;letter-spacing:.18em;color:#8C6A4A}
 .tw__name{font-family:${serif};font-size:22px;line-height:1.1}
 .tw__fin{font-size:12px;color:#6E675E;margin-top:2px}
 .tw__pr{font-size:14px;margin-top:8px}.tw__pr small{color:#6E675E;font-size:12px;${desk?'':'display:block'}}
 .tw__smp{margin-top:12px;font:inherit;font-size:13px;padding:9px 10px;border:1px solid #151413;background:#FBF9F5;color:#151413;text-align:center}
 .tw__c.is .tw__smp{background:#151413;color:#F5F2EC}
 .tw__ft{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-top:18px;font-size:13.5px;color:#3A3733}
 .tw__ft a{color:#151413;text-underline-offset:3px}
 `; document.head.appendChild(css);
 // A: decorkiezer in koopkolom
 const c0=D.find(x=>x.c===cur);
 const row=document.createElement('div'); row.className='tn';
 row.innerHTML=`<div class="tn__h"><span>Hout · ${D.length} decors</span><b>${c0.c} ${c0.n}</b></div><div class="tn__sw">${D.map(x=>`<a class="tn__s${x.c===cur?' is':''}" href="${x.u}" aria-label="${x.c} ${x.n}"><img src="${x.sw}" alt=""></a>`).join('')}</div><div class="tn__sc"><span>Licht</span><i></i><span>Donker</span></div>`;
 const price=document.querySelector('.pdh__price'); price.after(row);
 // B: tintenwaaier i.p.v. Meer uit de houtcollectie
 const more=document.querySelector('.pd-more'); const wrap=more.querySelector('.pd-wrap');
 more.className='pd-s tw'; 
 wrap.innerHTML=`<div class="tw__top"><div><p class="tw__k">Hout · ${D.length} decors</p><h2 class="tw__t">Vergelijk de houttinten</h2><p class="tw__lead">Van licht naar donker, naast elkaar. Bestel de tinten die je twijfelt als staal en leg ze tegen je wand.</p></div><div class="tw__tg" role="tablist"><button class="on" data-m="sw">Close-up</button><button data-m="vis">In een interieur</button></div></div>
 <div class="tw__scale"><span>Licht</span><i></i><span>Donker</span></div>
 <div class="tw__row">${D.map(x=>`<a class="tw__c${x.c===cur?' is':''}" href="${x.u}"><span class="tw__im"><img data-sw="${x.sw}" data-vis="${x.vis}" src="${x.sw}" alt="">${x.c===cur?'<span class="tw__b">Je bekijkt dit decor</span>':''}<span class="tw__v" hidden>Visualisatie</span></span><span class="tw__tx"><span class="tw__code">${x.c}</span><span class="tw__name">${x.n}</span><span class="tw__fin">${x.f}</span><span class="tw__pr">${x.p} <small>per paneel</small></span><span class="tw__smp">+ Gratis staal</span></span></a>`).join('')}</div>
 <div class="tw__ft"><span>Tot 5 stalen gratis · alleen € 6,95 verzending</span><a href="/pages/sample">Bekijk alle stalen →</a></div>`;
 window.__twMode=function(m){document.querySelectorAll('.tw__tg button').forEach(b=>b.classList.toggle('on',b.dataset.m===m));document.querySelectorAll('.tw__im img').forEach(i=>i.src=i.dataset[m]);document.querySelectorAll('.tw__v').forEach(v=>v.hidden=m!=='vis');};
};
