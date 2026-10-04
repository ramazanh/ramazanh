const {chromium}=require('playwright');
const files=process.argv.slice(2);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const f of files){for(const [w,h] of [[360,560],[390,664]]){
const p=await b.newPage({viewport:{width:w,height:h}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<!doctype html><meta name=viewport content="width=device-width"><body>'+require('fs').readFileSync(f+'.html','utf8'));
const over=[];
async function m(label){await p.waitForTimeout(700);const d=await p.evaluate(()=>[document.documentElement.scrollHeight,innerHeight,document.body.className]);if(d[0]>d[1]+2)over.push(label+':'+(d[0]-d[1])+'('+d[2]+')');}
await m('landing');
// advance landing
const lv=f.split('_').pop();
if(await p.$('#go1')){await p.click('#go1');await m('found')}
if(await p.$('.opt')&&await p.$('#cont')){await (await p.$$('.opt'))[0].click();await p.waitForTimeout(150);await p.click('#cont');await m('look')}
const ch=await p.$$('.chip3');if(ch.length){await ch[2].click();await p.waitForTimeout(900);await m('tip');await p.click('#more');await m('q1')}
for(let i=0;i<60;i++){
  const kick=await p.$eval('.kicker',e=>e.textContent).catch(()=>'');
  if(/Plan ready/i.test(kick)){await m('gate');await p.click('#skip');await p.waitForTimeout(500);break}
  if(/Did you know|not alone/i.test(kick)){await m('break:'+kick.slice(0,8));await p.click('#go');await p.waitForTimeout(200);continue}
  const btns=await p.$$('.opt:not([disabled])');
  if(btns.length){
    const id=await p.$eval('.q',e=>e.textContent.slice(0,22));
    await btns[0].click();await p.waitForTimeout(500);
    const nx=await p.$('#nx');
    if(nx){await m('reply:'+id);await nx.click();await p.waitForTimeout(200)}else{await p.waitForTimeout(1000);await m('q:'+id)}
  }
}
await p.waitForTimeout(300);
console.log(f,w+'x'+h,'overflow:',over.length?over.join(' | '):'none',errs.length?errs:'');
await p.close()}}
await b.close()})();
