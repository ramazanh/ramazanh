q=open('quiz.html').read()
i=q.index('<svg width="0" height="0"');j=q.index('</svg>',i)+6
defs=q[i:j]
def ic(n):return f'<svg viewBox="0 0 32 32" aria-hidden="true"><use href="#{n}"/></svg>'
def pl(n,cls=''):return f'<svg class="{cls}" viewBox="0 0 240 260" aria-hidden="true"><use href="#plant-{n}"/></svg>'
def bar(label,line,extra=''):
    return f'<div class="bar"><button class="cta" type="button">{label} <span aria-hidden="true">→</span></button><div class="tl">{line}</div></div>'
top='<div class="top"><div class="logo">'+ic('leaf')+'Green Thumb</div></div>'
def phone(pid,body,barhtml,cls=''):
    return f'<div class="phone {cls}"><div class="scroll" id="{pid}"><div class="in">{body}</div>{barhtml}</div></div>'

# ---- illustrations for the long read
def fig(svg,cap): return f'<figure class="ph"><div class="art">{svg}</div><figcaption>{cap}</figcaption></figure>'
S1='<svg viewBox="0 0 300 170" aria-hidden="true"><rect x="0" y="0" width="300" height="170" fill="none"/><g><rect x="132" y="-10" width="30" height="80" rx="15" fill="#F2C7A5" stroke="var(--edge)" stroke-width="3"/></g><path d="M80 66h140l-10 70a10 10 0 0 1-10 8H100a10 10 0 0 1-10-8z" fill="var(--pot)" stroke="var(--edge)" stroke-width="3" stroke-linejoin="round"/><rect x="70" y="54" width="160" height="20" rx="8" fill="var(--pot2)" stroke="var(--edge)" stroke-width="3"/><ellipse cx="150" cy="56" rx="72" ry="5" fill="#6B4A36"/><g stroke="var(--ink)" stroke-width="2.5" stroke-linecap="round" fill="none"><path d="M246 56v34M241 56h10M241 90h10"/></g><text x="252" y="78" font-size="13" font-weight="700" fill="var(--ink)">2 in</text></svg>'
S2='<svg viewBox="0 0 300 170" aria-hidden="true"><rect x="170" y="14" width="110" height="130" rx="6" fill="var(--sky)" stroke="var(--edge)" stroke-width="3"/><path d="M225 14v130M170 79h110" stroke="var(--edge)" stroke-width="3"/><circle cx="252" cy="42" r="14" fill="var(--sun)" stroke="var(--edge)" stroke-width="3"/><path d="M170 144 L40 160 L40 120Z" fill="var(--sun)" opacity=".35"/><g transform="translate(40 40)"><use href="#plant-other" x="0" y="0" width="100" height="108"/></g><path d="M20 160h260" stroke="var(--edge)" stroke-width="3" stroke-linecap="round"/></svg>'
S3='<svg viewBox="0 0 300 170" aria-hidden="true"><rect x="146" y="8" width="20" height="150" rx="9" fill="#B89B6E" stroke="var(--edge)" stroke-width="3"/><path d="M156 156 C130 130 180 112 156 84 C132 58 178 44 158 20" fill="none" stroke="var(--edge)" stroke-width="8" stroke-linecap="round"/><path d="M156 156 C130 130 180 112 156 84 C132 58 178 44 158 20" fill="none" stroke="var(--g1)" stroke-width="4" stroke-linecap="round"/><use href="#leafg" style="color:var(--g2)" transform="translate(140 126) rotate(-60) scale(.5) translate(-50 -78) rotate(180 50 50)"/><use href="#leafg" style="color:var(--g3)" transform="translate(166 96) rotate(60) scale(.55) translate(-50 -78) rotate(180 50 50)"/><use href="#leafg" style="color:var(--g2)" transform="translate(142 64) rotate(-55) scale(.5) translate(-50 -78) rotate(180 50 50)"/><use href="#leafg" style="color:var(--g3)" transform="translate(162 36) rotate(40) scale(.45) translate(-50 -78) rotate(180 50 50)"/></svg>'
S4='<svg viewBox="0 0 300 170" aria-hidden="true"><path d="M84 40h132l-12 90a10 10 0 0 1-10 8H106a10 10 0 0 1-10-8z" fill="var(--pot)" stroke="var(--edge)" stroke-width="3" stroke-linejoin="round"/><rect x="74" y="26" width="152" height="18" rx="7" fill="var(--pot2)" stroke="var(--edge)" stroke-width="3"/><g fill="none" stroke="#C9A77A" stroke-width="5" stroke-linecap="round"><path d="M138 138 C132 152 140 160 130 168"/><path d="M152 138 C154 152 148 160 156 168"/><path d="M166 138 C174 150 168 160 178 166"/></g><ellipse cx="152" cy="138" rx="22" ry="4" fill="#4B3426"/></svg>'
S5='<svg viewBox="0 0 300 170" aria-hidden="true"><path d="M92 20h116l-10 78a10 10 0 0 1-10 8H112a10 10 0 0 1-10-8z" fill="var(--pot)" stroke="var(--edge)" stroke-width="3" stroke-linejoin="round"/><rect x="82" y="8" width="136" height="16" rx="7" fill="var(--pot2)" stroke="var(--edge)" stroke-width="3"/><ellipse cx="150" cy="140" rx="84" ry="14" fill="var(--card)" stroke="var(--edge)" stroke-width="3"/><g fill="var(--water)" stroke="var(--edge)" stroke-width="2"><path d="M138 112c5 8 7 11 7 14a7 7 0 0 1-14 0c0-3 2-6 7-14z"/><path d="M162 116c4 7 6 9 6 12a6 6 0 0 1-12 0c0-3 2-5 6-12z"/></g></svg>'
S6='<svg viewBox="0 0 300 170" aria-hidden="true"><g transform="translate(180 6)"><use href="#plant-monstera" width="100" height="108"/></g><path d="M170 160h120" stroke="var(--edge)" stroke-width="3" stroke-linecap="round"/><g stroke="var(--edge)" stroke-width="3" stroke-linejoin="round"><ellipse cx="68" cy="128" rx="34" ry="30" fill="var(--sun)"/><circle cx="64" cy="82" r="24" fill="var(--sun)"/><path d="M44 66l6-24 14 14zM84 66l-6-24-14 14z" fill="var(--sun)"/><path d="M96 138c26 4 34-10 28-24" fill="none" stroke-linecap="round"/></g><g fill="var(--edge)"><circle cx="56" cy="82" r="3"/><circle cx="72" cy="82" r="3"/></g><path d="M20 160h120" stroke="var(--edge)" stroke-width="3" stroke-linecap="round"/></svg>'
secs=[
('Check the soil before you water.','Push a finger about 2 inches into the soil. If it feels dry, water. If it’s still damp, wait a few days.','A finger testing the soil in a pot.',S1),
('Bright, indirect light is a good start.','Many houseplants like bright light that doesn’t hit them directly. Strong sun through glass can burn leaves. Watch where light falls through the day.','A plant beside a window with soft light.',S2),
('Long vines can be normal.','Climbing plants like Monstera grow long on purpose. In nature they climb trees. A pole or trellis can help hold them up.','A Monstera vine climbing a wooden pole.',S3),
('Wait before you repot or trim.','A move is stressful for a plant. Give it a few weeks to settle before big changes. Repot later only if roots look crowded.','Roots peeking out of a pot’s bottom hole.',S4),
('Drainage holes help roots breathe.','Water needs a way out of the pot. Roots that sit wet can rot. No holes? Keep the plant in a plain pot with holes, set inside the pretty one.','Water draining from a pot into a saucer.',S5),
('Check if your plant is pet safe.','Many common houseplants can upset pets if chewed, and Monstera is one. Look up your plant’s name on the ASPCA plant list. If you’re unsure, keep it out of reach.','A cat sitting safely away from a plant.',S6)]
art=''
for n,(h,b,c,s) in enumerate(secs,1):
    art+=f'<section class="as"><h3 class="h3">{h}</h3>{fig(s,c)}<p>{b}</p></section>'
    if n==3:
        art+=f'<div class="inl"><p>Want help with your own plant?</p><button class="cta small" type="button">Show me one thing <span aria-hidden="true">→</span></button></div>'
    if n==4:
        art+='<blockquote class="pq">Waiting a little is often the kindest thing you can do.</blockquote>'
m3=phone('p3','<div class="top"><div class="logo">'+ic('leaf')+'Green Thumb</div></div><span class="tagp">Plant guide</span><h2 class="h">A gentle guide to caring for a plant you love</h2><p class="by">Plant care guide</p><p class="sub">Plants can be easier than they look. These six ideas fit most houseplants, big or small.</p>'+f'<div class="hero3">{pl("monstera","hp")}</div>'+art+'<div class="as"><p>You don’t need to fix everything today. Start with one small check, like the soil. Your plant will show you more over time. If you’d like help with your own plant, answer a few questions.</p></div><p class="fine">General plant-care tips. Not a substitute for a local nursery.</p>',bar('See what it needs','Not sure where to start? Answer one question.'))

m1=phone('p1',top+f'''<div class="scene2" aria-hidden="true"><div class="rays"></div>{pl('monstera','sway')}</div>
<h2 class="h">Let’s figure out what your plant needs</h2>
<p class="sub">Answer one quick question. No rush, no pressure.</p>
<div class="tipbox"><b>One thing to know</b><span>Many houseplants like to dry out a little between waterings. Check first.</span></div>
<p class="ask">How did this plant find you?</p>
<div class="chips3"><button class="chip3" type="button"><span class="ic">{ic('i-heart')}</span>I inherited it</button><button class="chip3" type="button"><span class="ic">{ic('i-box')}</span>I bought it</button><button class="chip3" type="button"><span class="ic">{ic('i-sprout')}</span>It was a gift</button></div>''',bar('Show me one thing','One tap at a time. Stop anytime.'))

beats=['Some plants hold a lot of memories.','Caring for one can feel big.','You don’t have to know it all.','So, how is your plant today?']
m2=f'''<div class="phone"><div class="scroll an" id="p2"><div class="in" id="an1">{top}<div class="scene2 big" aria-hidden="true"><div class="rays"></div>{pl('monstera','sway')}</div><div class="beats">'''+''.join(f'<p class="b">{b}</p>' for b in beats)+'''</div><div class="adots" aria-hidden="true"><i></i><i></i><i></i><i></i></div></div>
<div class="in" id="an2" hidden>'''+top+f'''<h2 class="h">What’s going on with your plant?</h2><div class="opts4"><button class="opt4" type="button"><span class="ic">{ic('i-up')}</span>It looks tall or leggy</button><button class="opt4" type="button"><span class="ic">{ic('i-droop')}</span>Leaves are yellow or droopy</button><button class="opt4" type="button"><span class="ic">{ic('i-q')}</span>I’m not sure what it needs</button><button class="opt4" type="button"><span class="ic">{ic('i-box')}</span>I just got it</button></div></div>
<div class="bar" id="anbar"></div></div></div>'''

m4=phone('p4',top+f'''<h2 class="h">Which plant are you caring for?</h2><p class="sub">Pick the closest one. We’ll start there.</p><p class="ask">How did this plant find you?</p>
<div class="tiles"><button class="tile" type="button"><span class="i">{ic('i-heart')}</span>I inherited a plant</button><button class="tile" type="button"><span class="i">{ic('i-box')}</span>I just bought one</button><button class="tile" type="button"><span class="i">{ic('i-sprout')}</span>Someone gave me one</button><button class="tile" type="button"><span class="i">{ic('i-house')}</span>I’ve had it a while</button></div>''',bar('Check on my plant','Pick one, then we’ll go slowly.'))

m5=phone('p5',top+f'''<h2 class="h">Here’s what a plant plan can look like</h2><p class="sub">Tell us about your plant and we’ll write steps like these.</p>
<div class="sample"><span class="ex">Example only. Yours will match your plant.</span>
<div class="s1"><b>Your first step</b><div class="row1"><span class="bx"></span>Check the soil with a finger, 2 inches down.</div></div>
<div class="s2"><b>Leave alone</b><div class="row1"><span class="x">×</span>Skip repotting and trimming for now after a move.</div></div>
<div class="s3"><b>Watch for</b><div class="row1"><span class="w">!</span>Watch for soil that stays wet for many days.</div></div></div>''',bar('See what it needs','Answer a few questions first.'))

ads={
1:[('Not sure what your plant needs?','Every plant is a little different. Take a quiet minute and answer a few questions about yours.','Learn more'),('Before you water, try this','Many houseplants like to dry out a bit between drinks. Here’s a simple way to check yours.','See more')],
2:[('A plant can hold a lot of memories','If a plant means something to you, let’s take care of it, gently.','Learn more'),('New plant, big questions?','Light, water, pots, pets. Answer a few quick questions and see where to begin.','See more')],
3:[('Six gentle things to know about houseplants','Soil checks, light, pots, and pets. A short, plain guide for anyone caring for a plant.','See more'),('Is your Monstera supposed to look like this?','Long, climbing vines are often normal. Read what to watch for and what can wait.','Learn more')],
4:[('Did you inherit a plant?','It can feel like a lot. Tell us a bit about it and we’ll help you know where to start.','Learn more'),('Which plant are you caring for?','Pick the closest match, then see simple first steps. Works for new plants, gifts, and old ones.','See more')],
5:[('See what plant care steps can look like','One thing to do first, one to leave alone, one to watch. Take a look at an example.','See more'),('Plant care, one step at a time','Get simple steps for your plant: what to do, what to wait on, and what to watch.','Learn more')]}
def adhtml(n):
    return '<details class="ads"><summary>Ad copy that leads here</summary>'+''.join(f'<div class="ad"><b>{h}</b><p>{p}</p><span>Button: {b}</span></div>' for h,p,b in ads[n])+'</details>'
def col(n,name,desc,body,extra=''):
    return f'<div class="col">{body}{extra}<div class="cap"><b>{n} · {name}</b><span>{desc}</span></div>{adhtml(n)}<button class="pick" data-k="{n}" type="button">Pick {n}</button></div>'
replay='<button class="rep" id="replay" type="button">Replay the animation</button>'
html=f'''<title>Landing Options</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Shrikhand&family=Figtree:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--pbg:#EEF3EF;--pfg:#183229;--pmuted:#52716A;--pcard:#fff;--pline:#CFE0D6;--pacc:#B83A62}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--pbg:#101C18;--pfg:#E6F2EC;--pmuted:#9DB8AB;--pcard:#17271F;--pline:#2A4538;--pacc:#F08AA6;color-scheme:dark}}}}
:root[data-theme="dark"]{{--pbg:#101C18;--pfg:#E6F2EC;--pmuted:#9DB8AB;--pcard:#17271F;--pline:#2A4538;--pacc:#F08AA6;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--pbg);color:var(--pfg);font-family:'Figtree',system-ui,sans-serif;font-size:16px;line-height:1.45;padding-inline:16px;padding-block:24px 70px}}
.wrap{{max-width:1260px;margin-inline:auto}}
h1{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(30px,7vw,42px);line-height:1.08;margin:0;text-wrap:balance}}
.lead{{color:var(--pmuted);margin:10px 0 0;max-width:62ch}}
.tog{{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}}
.tog button{{font:inherit;font-weight:700;padding:9px 16px;border-radius:99px;border:2px solid var(--pfg);background:transparent;color:var(--pfg);cursor:pointer}}
.tog button[aria-pressed="true"]{{background:var(--pfg);color:var(--pbg)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,370px),1fr));gap:34px 28px;margin-top:24px}}
.col{{min-width:0;display:flex;flex-direction:column;gap:12px;align-items:center}}
.cap{{align-self:stretch;display:flex;flex-direction:column;gap:2px}}
.cap b{{font-family:'Fraunces',serif;font-size:21px}}
.cap span{{color:var(--pmuted);font-size:15px}}
.pick{{align-self:stretch;font:inherit;font-weight:800;font-size:17px;padding:13px;border-radius:14px;border:2px solid var(--pfg);background:var(--pfg);color:var(--pbg);cursor:pointer}}
.pick[aria-pressed="true"]{{background:#F7D774;color:#183229;border-color:#F7D774}}
.rep{{align-self:stretch;font:inherit;font-weight:700;padding:10px;border-radius:12px;border:2px solid var(--pline);background:var(--pcard);color:var(--pfg);cursor:pointer}}
.ads{{align-self:stretch;border:2px solid var(--pline);border-radius:14px;background:var(--pcard);padding:0 14px}}
.ads summary{{cursor:pointer;font-weight:700;padding:11px 0}}
.ad{{border-top:1px dashed var(--pline);padding:10px 0;font-size:15px}}.ad b{{display:block}}.ad p{{margin:2px 0}}.ad span{{color:var(--pmuted);font-size:13.5px}}
:focus-visible{{outline:3px solid var(--pacc);outline-offset:3px}}
symbol{{overflow:visible}}
.note{{margin-top:18px;color:var(--pmuted)}}
.phone{{width:min(390px,100%);height:760px;border:9px solid #14201a;border-radius:42px;overflow:hidden;background:#000;box-shadow:0 14px 40px rgba(0,0,0,.2)}}
.grid .phone{{--bg:#F3F6F2;--ink:#274A3E;--card:#fff;--soft:#F9E4EA;--blob:#DCEBE4;--edge:#5F8F7B;--bw:1.5px;--sun:#F7D774;--g1:#3C7A5E;--g2:#6DB28B;--g3:#B9DFC7;--pot:#F2A9B8;--pot2:#E58AA0;--sky:#FDF1C9;--water:#A9D6EE;--pop:#B83A62;--popd:#7E2441;--muted:#58786B;--disp:'Fraunces',Georgia,serif;--dw:600;--osh:0 3px 10px rgba(39,74,62,.1);--cardbd:#5F8F7B}}
.grid.sd .phone{{--bg:#F3E2BF;--ink:#4A2B1A;--card:#FBF1D8;--soft:#F7C98B;--blob:#F2B25A;--edge:#4A2B1A;--bw:2.5px;--sun:#F6B01C;--g1:#2F5D3A;--g2:#6A9A3A;--g3:#B6C94F;--pot:#E2702D;--pot2:#B4471B;--sky:#FBE7A8;--water:#8CC6C9;--pop:#B9420F;--popd:#7A2A08;--muted:#7A5236;--disp:'Shrikhand',Georgia,serif;--dw:400;--osh:3px 3px 0 #4A2B1A}}
.scroll{{height:100%;overflow-y:auto;overflow-x:hidden;background:var(--bg);color:var(--ink);font-family:'Figtree',sans-serif;scrollbar-width:none;position:relative;display:flex;flex-direction:column}}
.scroll::-webkit-scrollbar{{display:none}}
.in{{padding:14px 18px 8px;display:flex;flex-direction:column;gap:12px;flex:1}}
.in[hidden]{{display:none}}
.top{{display:flex;justify-content:center}}
.logo{{display:flex;align-items:center;gap:8px;font-family:var(--disp);font-weight:var(--dw);font-size:16px}}
.logo svg{{width:26px;height:26px;color:var(--g2)}}
.h{{font-family:var(--disp);font-weight:var(--dw);font-size:29px;line-height:1.12;margin:0;text-wrap:balance}}
.grid.sd .h{{font-size:25px}}
.h3{{font-family:var(--disp);font-weight:var(--dw);font-size:22px;line-height:1.15;margin:0}}
.grid.sd .h3{{font-size:19px}}
.sub{{margin:0;font-size:17px}}
.ask{{font-weight:700;font-size:18px;margin:2px 0 0}}
.bar{{position:sticky;bottom:0;z-index:5;padding:12px 16px calc(12px + env(safe-area-inset-bottom,0px));background:var(--bg);border-top:var(--bw) solid var(--edge);box-shadow:0 -8px 22px rgba(0,0,0,.08)}}
.cta{{display:flex;width:100%;align-items:center;justify-content:center;gap:10px;font:inherit;font-family:var(--disp);font-weight:var(--dw);font-size:20px;min-height:58px;padding:12px 18px;border:var(--bw) solid var(--edge);border-radius:99px;background:var(--pop);color:#fff;box-shadow:0 4px 0 var(--popd);cursor:pointer}}
.cta.small{{min-height:50px;font-size:18px}}
.cta.ghost{{background:var(--card);color:var(--ink);box-shadow:var(--osh)}}
.tl{{text-align:center;font-size:14px;font-weight:600;margin-top:8px;color:var(--ink);opacity:.8}}
.scene2{{position:relative;border-radius:24px;background:var(--blob);overflow:hidden;display:flex;justify-content:center;align-items:flex-end;padding:8px 8px 0}}
.scene2 .rays{{position:absolute;inset:-25% -15%;background:linear-gradient(115deg,transparent 28%,rgba(255,255,255,.6) 40%,transparent 52%,rgba(255,255,255,.35) 64%,transparent 76%);animation:rays 9s ease-in-out infinite alternate;pointer-events:none}}
@keyframes rays{{from{{transform:translateX(-10%);opacity:.45}}to{{transform:translateX(10%);opacity:.9}}}}
.sway{{height:132px;width:auto;aspect-ratio:240/260;flex:none;overflow:visible;transform-origin:50% 100%;animation:sway 7s ease-in-out infinite}}
.scene2.big .sway{{height:230px}}
@keyframes sway{{0%,100%{{transform:rotate(-1.8deg)}}50%{{transform:rotate(1.8deg)}}}}
.tipbox{{display:flex;flex-direction:column;gap:2px;background:var(--card);border:var(--bw) solid var(--edge);border-radius:16px;padding:10px 12px;font-size:16px}}.tipbox b{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.chips3{{display:flex;flex-direction:column;gap:10px}}
.chip3,.opt4{{position:relative;display:flex;align-items:center;gap:14px;width:100%;min-height:62px;text-align:left;font:inherit;font-weight:700;font-size:18px;color:var(--ink);background:var(--card);border:var(--bw) solid var(--edge);border-radius:18px;padding:8px 40px 8px 12px;box-shadow:var(--osh);cursor:pointer}}
.chip3::after,.opt4::after{{content:"\\203a";position:absolute;right:16px;font-size:28px;opacity:.55}}
.ic{{flex:none;width:44px;height:44px;border:var(--bw) solid var(--edge);border-radius:13px;background:var(--bg);display:grid;place-items:center;color:var(--edge)}}.ic svg{{width:30px;height:30px}}
.opts4{{display:flex;flex-direction:column;gap:12px;margin-top:6px}}
.tiles{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.tile{{position:relative;display:flex;flex-direction:column;gap:8px;text-align:left;font:inherit;font-weight:700;font-size:17px;line-height:1.25;color:var(--ink);background:var(--card);border:var(--bw) solid var(--edge);border-radius:20px;padding:14px 12px;box-shadow:var(--osh);min-height:140px;cursor:pointer}}
.tile .i{{width:46px;height:46px;border-radius:14px;background:var(--bg);display:grid;place-items:center}}.tile .i svg{{width:32px;height:32px;color:var(--edge)}}
.tagp{{align-self:flex-start;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;background:var(--sun);color:var(--ink);border:var(--bw) solid var(--edge);border-radius:99px;padding:3px 10px}}
.by{{margin:-4px 0 0;font-size:14px;font-weight:600;color:var(--muted)}}
.hero3{{background:var(--blob);border-radius:22px;display:grid;place-items:center;padding:10px 10px 0}}.hp{{width:150px;height:auto}}
.as{{display:flex;flex-direction:column;gap:10px;margin-top:6px}}.as p{{margin:0;font-size:17px}}
figure.ph{{margin:0}}.ph .art{{background:var(--blob);border-radius:18px;border:var(--bw) solid var(--edge);padding:6px;overflow:hidden}}.ph svg{{width:100%;height:auto;display:block}}
figcaption{{font-size:13.5px;color:var(--muted);margin-top:6px}}
.pq{{margin:14px 0 6px;padding:14px 16px;border-left:5px solid var(--pop);background:var(--card);border-radius:0 16px 16px 0;font-family:var(--disp);font-weight:var(--dw);font-size:22px;line-height:1.2}}
.grid.sd .pq{{font-size:19px}}
.inl{{background:var(--soft);border:var(--bw) solid var(--edge);border-radius:18px;padding:14px;display:flex;flex-direction:column;gap:10px;margin-top:8px}}.inl p{{margin:0;font-weight:700}}
.fine{{font-size:13px;opacity:.75;text-align:center;margin:8px 0}}
.sample{{background:var(--card);border:var(--bw) solid var(--edge);border-radius:22px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px rgba(39,74,62,.12)}}
.ex{{align-self:flex-start;font-size:12.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;background:var(--sun);border-radius:99px;padding:4px 10px}}
.sample b{{font-family:var(--disp);font-weight:var(--dw);font-size:19px}}
.row1{{display:flex;gap:10px;align-items:center;margin-top:4px;font-size:16.5px}}
.bx{{flex:none;width:24px;height:24px;border:var(--bw) solid var(--edge);border-radius:7px}}
.x,.w{{flex:none;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-weight:800}}.x{{background:#FCE8DC;color:#B5501F}}.w{{background:var(--sun)}}
.s2,.s3{{border-top:1.5px dashed var(--edge);padding-top:10px}}
.beats{{position:relative;height:130px;margin-top:6px}}
.b{{position:absolute;inset:0;margin:0;display:grid;place-items:center;text-align:center;font-family:var(--disp);font-weight:var(--dw);font-size:27px;line-height:1.15;opacity:0;transform:translateY(8px);transition:opacity .7s,transform .7s}}
.grid.sd .b{{font-size:23px}}
.b.on{{opacity:1;transform:none}}
.adots{{display:flex;gap:8px;justify-content:center}}.adots i{{width:9px;height:9px;border-radius:50%;background:var(--edge);opacity:.25;transition:opacity .4s}}.adots i.on{{opacity:1}}
#an2{{animation:fadein .6s ease both}}@keyframes fadein{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{.scene2 .rays,.sway,#an2{{animation:none!important}}.b{{transition:none}}}}
</style>
{defs}
<div class="wrap">
  <h1>Five landing options</h1>
  <p class="lead">Every one keeps a clear button fixed at the bottom. Scroll inside each phone. Option 2 plays by itself and moves to its second page when it ends. Option 3 is the long article.</p>
  <div class="tog" role="group" aria-label="Look"><button type="button" id="sc" aria-pressed="true">Watercolor look</button><button type="button" id="sd" aria-pressed="false">Retro 70s look</button></div>
  <div class="grid sc" id="grid">
  {col(1,'Quiet Start','Calm. One idea, one question, one button.',m1)}
  {col(2,'Animated Opening','Four calm lines, then it moves on to the first question by itself.',m2,replay)}
  {col(3,'Long Read','A native, article-style guide with images. The button stays on screen.',m3)}
  {col(4,'Quiz First','The first question is the page.',m4)}
  {col(5,'Plan Preview','Shows what you get before you start.',m5)}
  </div>
  <p class="note" id="msg" role="status"></p>
</div>
<script>
(function(){{
document.querySelectorAll('.pick').forEach(function(b){{b.addEventListener('click',function(){{
  document.querySelectorAll('.pick').forEach(function(x){{x.setAttribute('aria-pressed','false');x.textContent='Pick '+x.dataset.k}});
  b.setAttribute('aria-pressed','true');b.textContent='Picked '+b.dataset.k;
  document.getElementById('msg').textContent='Tell me: '+b.dataset.k+'.';
}})}});
var g=document.getElementById('grid'),a=document.getElementById('sc'),d=document.getElementById('sd');
function look(k){{g.className='grid '+k;a.setAttribute('aria-pressed',String(k==='sc'));d.setAttribute('aria-pressed',String(k==='sd'))}}
a.onclick=function(){{look('sc')}};d.onclick=function(){{look('sd')}};
var timers=[];
function clr(){{timers.forEach(clearTimeout);timers=[]}}
function bar2(page){{
  var b=document.getElementById('anbar');
  b.innerHTML=page===1?'<button class="cta ghost" type="button" id="skip">Skip</button>':'<button class="cta" type="button">See what it needs <span aria-hidden="true">\\u2192</span></button><div class="tl">Just one question at a time.</div>';
  var s=document.getElementById('skip');if(s)s.onclick=function(){{clr();page2()}};
}}
function page2(){{document.getElementById('an1').hidden=true;var p=document.getElementById('an2');p.hidden=false;bar2(2);document.getElementById('p2').scrollTop=0}}
function run(){{
  clr();var an1=document.getElementById('an1');an1.hidden=false;document.getElementById('an2').hidden=true;bar2(1);
  var bs=an1.querySelectorAll('.b'),ds=an1.querySelectorAll('.adots i');
  bs.forEach(function(x){{x.classList.remove('on')}});ds.forEach(function(x){{x.classList.remove('on')}});
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches){{page2();return}}
  bs.forEach(function(x,i){{
    timers.push(setTimeout(function(){{bs.forEach(function(y){{y.classList.remove('on')}});x.classList.add('on');ds.forEach(function(y,j){{y.classList.toggle('on',j<=i)}})}},500+i*2800));
  }});
  timers.push(setTimeout(page2,500+bs.length*2800+400));
}}
document.getElementById('replay').onclick=run;run();
}})();
</script>
'''
open('landing6.html','w').write(html)
