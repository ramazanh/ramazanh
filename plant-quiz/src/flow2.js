const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const k of ['c','d']){
const p=await b.newPage({viewport:{width:400,height:740}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<!doctype html><meta name=viewport content="width=device-width"><body>'+require('fs').readFileSync('quiz_'+k+'.html','utf8'));
await p.waitForTimeout(500);await p.screenshot({path:k+'_q1.png'});
const dis=await p.$eval('#cont',e=>e.disabled);
await (await p.$$('.opt'))[0].click();await p.waitForTimeout(200);await p.screenshot({path:k+'_q2.png'});
const lab=await p.$eval('#cont',e=>e.textContent);
await p.click('#cont');await p.waitForTimeout(1800);
await (await p.$$('.chip3'))[2].click();await p.waitForTimeout(800);
await p.click('#try');await p.click('#more');await p.waitForTimeout(300);
const seq=[];
for(let i=0;i<60;i++){
  const kick=await p.$eval('.kicker',e=>e.textContent).catch(()=>'');
  if(/Plan ready/i.test(kick)){seq.push('GATE');await p.click('#skip');await p.waitForTimeout(300);break}
  seq.push(kick.slice(0,12));
  if(/Did you know|not alone/i.test(kick)){await p.click('#go');await p.waitForTimeout(250);continue}
  const btns=await p.$$('.opt:not([disabled])');
  if(btns.length){await btns[0].click();await p.waitForTimeout(450);const nx=await p.$('#nx');if(nx){await nx.click();await p.waitForTimeout(150)}else await p.waitForTimeout(1100)}
}
console.log(k,'disabledAtStart',dis,'afterPick',lab.trim(),'| first q:',seq[0],'| n',seq.length,'res',!!(await p.$('.res')),errs,await p.evaluate(()=>document.documentElement.scrollWidth));
}
await b.close()})();
