import re
s=open('quiz.html').read()
# split style block
a=s.index('<style>')+7;b=s.index('</style>')
css=s[a:b]
css=css.replace('2px solid var(--edge)','var(--bw) solid var(--edge)')
css=css.replace('0 5px 0 var(--edge)','var(--sh)').replace('0 3px 0 var(--edge)','var(--osh)').replace('0 4px 0 var(--edge)','var(--bsh)').replace('0 0 0 var(--edge)','var(--ash)')
css=css.replace('font-weight:800','font-weight:var(--dw)')
css=css.replace('--display:','--bw:2px;--sh:0 5px 0 var(--edge);--osh:0 3px 0 var(--edge);--bsh:0 4px 0 var(--edge);--ash:0 0 0 var(--edge);--dw:800;\n  --display:',1)
def tok(d): return ';'.join(f'--{k}:{v}' for k,v in d.items())+';'
C_l={'bg':'#F3F6F2','card':'#FFFFFF','ink':'#274A3E','muted':'#58786B','line':'#CFE0D6','leaf':'#3C7A5E','on-leaf':'#FFFFFF','pop':'#B83A62','popd':'#7E2441','on-pop':'#FFFFFF','pop-soft':'#F9E4EA','sun':'#F7D774','on-sun':'#274A3E','good':'#2F7A55','good-soft':'#E0F1E7','bad':'#B5501F','bad-soft':'#FCE8DC','edge':'#5F8F7B','g1':'#3C7A5E','g2':'#6DB28B','g3':'#B9DFC7','pot':'#F2A9B8','pot2':'#E58AA0','blob':'#DCEBE4','sky':'#FDF1C9','water':'#A9D6EE','wash1':'rgba(185,223,199,.65)','wash2':'rgba(242,169,184,.30)','wash3':'rgba(169,214,238,.40)'}
C_x={'bw':'1.5px','sh':'0 10px 28px rgba(39,74,62,.14)','osh':'0 3px 10px rgba(39,74,62,.10)','bsh':'0 6px 16px rgba(39,74,62,.22)','ash':'none','dw':'600','display':"'Fraunces','Georgia',serif"}
C_d={'bg':'#101C18','card':'#17271F','ink':'#E6F2EC','muted':'#9DB8AB','line':'#2A4538','leaf':'#6DB28B','on-leaf':'#0B1E16','pop':'#F08AA6','popd':'#9A4A60','on-pop':'#2A0A14','pop-soft':'#3A1E29','sun':'#F7D774','on-sun':'#274A3E','good':'#6DD39A','good-soft':'#173626','bad':'#FFA67A','bad-soft':'#3A2518','edge':'#6F9E8A','g1':'#4E9A76','g2':'#7BC79B','g3':'#B9E6CB','pot':'#D98FA0','pot2':'#BE6F85','blob':'#1F3A2F','sky':'#3D3818','water':'#5BA9D6','wash1':'rgba(79,208,138,.12)','wash2':'rgba(240,138,166,.10)','wash3':'rgba(91,169,214,.14)'}
D_l={'bg':'#F3E2BF','card':'#FBF1D8','ink':'#4A2B1A','muted':'#7A5236','line':'#DDBE88','leaf':'#2F6B3A','on-leaf':'#FFF6DE','pop':'#B9420F','popd':'#7A2A08','on-pop':'#FFFFFF','pop-soft':'#F7C98B','sun':'#F6B01C','on-sun':'#4A2B1A','good':'#2F6B3A','good-soft':'#DDE8B8','bad':'#A8431A','bad-soft':'#F5CBA7','edge':'#4A2B1A','g1':'#2F5D3A','g2':'#6A9A3A','g3':'#B6C94F','pot':'#E2702D','pot2':'#B4471B','blob':'#F2B25A','sky':'#FBE7A8','water':'#8CC6C9','sun2':'#F6C46E'}
D_x={'bw':'2.5px','sh':'5px 5px 0 var(--edge)','osh':'3px 3px 0 var(--edge)','bsh':'4px 4px 0 var(--edge)','ash':'0 0 0 var(--edge)','dw':'400','display':"'Shrikhand','Georgia',serif"}
D_d={'bg':'#2A1A12','card':'#3A261B','ink':'#F6E7C8','muted':'#CBAE8A','line':'#5A3F2D','leaf':'#A5C85A','on-leaf':'#1F1408','pop':'#F08A4B','popd':'#8A4A22','on-pop':'#2A1208','pop-soft':'#5A3320','sun':'#F6B01C','on-sun':'#4A2B1A','good':'#A5C85A','good-soft':'#3A4220','bad':'#FF9A66','bad-soft':'#5A2E1B','edge':'#E8C98F','g1':'#6A9A3A','g2':'#A5C85A','g3':'#D3E07A','pot':'#E2702D','pot2':'#B4471B','blob':'#7A4A1F','sky':'#5A4A1E','water':'#6AAEB2','sun2':'#8A5A28'}

G_l={'bg':'#3A8EF0','card':'#FFFFFF','ink':'#1B2B6B','muted':'#4B5FA8','line':'#B7C6F5','leaf':'#2FBF4A','on-leaf':'#FFFFFF','pop':'#FF8A00','popd':'#8A3B00','on-pop':'#FFFFFF','pop-soft':'#FFE9C2','sun':'#FFD23F','on-sun':'#5A3A00','good':'#1A8F3E','good-soft':'#D9F8DF','bad':'#C2353A','bad-soft':'#FFE0E0','edge':'#1B2B6B','g1':'#1E8E3E','g2':'#3BC45B','g3':'#9BEA9B','pot':'#FF9B3D','pot2':'#E5731A','blob':'#BFE6FF','sky':'#FFF4B8','water':'#6EC6FF'}
G_x={'bw':'3px','sh':'0 8px 0 #101C4A','osh':'0 5px 0 #101C4A','bsh':'0 6px 0 #8A3B00','ash':'0 0 0 #101C4A','dw':'400','display':"'Lilita One','Fredoka',system-ui,sans-serif"}
def block(k,l,x,d):
    return f'''
:root[data-style="{k}"]{{{tok(l)}{tok(x)}}}
@media (prefers-color-scheme:dark){{:root[data-style="{k}"]:not([data-theme="light"]){{{tok(d)}color-scheme:dark}}}}
:root[data-style="{k}"][data-theme="dark"]{{{tok(d)}color-scheme:dark}}
'''
extra=block('c',C_l,C_x,C_d)+block('d',D_l,D_x,D_d)+block('g',G_l,G_x,G_l)+'''
[data-style="c"] .scene,[data-style="c"] .fig svg,[data-style="c"] .pc svg,[data-style="c"] .mini{filter:url(#wc)}
[data-style="c"] .fig{background:radial-gradient(120% 90% at 30% 20%,var(--blob),var(--card))}
[data-style="d"] .fig{background:repeating-conic-gradient(from 0deg at 50% 100%,var(--blob) 0 10deg,var(--sun2) 10deg 20deg)}
[data-style="d"] .q{font-size:clamp(23px,5.8vw,29px);line-height:1.15}
[data-style="d"] .landing h1{font-size:clamp(25px,6.6vw,34px)}
[data-style="d"] .res h1{font-size:clamp(28px,7.4vw,38px)}
[data-style="d"] .btn{font-size:18px}
[data-style="d"] .opt{font-weight:700}
[data-style="d"] .hero h1 em{color:var(--pop)}

[data-style="c"] body,[data-style="c"] body.lp{background:radial-gradient(70% 38% at 8% 0%,var(--wash1),transparent 72%),radial-gradient(55% 34% at 100% 26%,var(--wash2),transparent 72%),radial-gradient(70% 40% at 0% 100%,var(--wash3),transparent 72%),var(--bg)}
[data-style="c"] body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.09;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2' seed='3'/><feColorMatrix values='0 0 0 0 .25 0 0 0 0 .35 0 0 0 0 .3 0 0 0 .7 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")}
[data-style="c"] .card,[data-style="c"] .sample{border-radius:28px 32px 26px 30px/30px 26px 32px 28px}
[data-style="c"] .opt,[data-style="c"] .chip3,[data-style="c"] .tipnote,[data-style="c"] .reply{border-radius:20px 24px 18px 22px/22px 18px 24px 20px}
[data-style="c"] .deco{opacity:.2;filter:blur(.8px)}
[data-style="c"] .fig,[data-style="c"] .scene2,[data-style="c"] .growscene,[data-style="c"] .hero3,[data-style="c"] .tipart{border-radius:30px 26px 32px 24px/26px 32px 24px 30px}
[data-style="c"] .top{background:transparent}

[data-style="g"] body,[data-style="g"] body.lp{background:radial-gradient(120% 55% at 50% 0%,#9BE0FF 0%,transparent 62%),linear-gradient(180deg,#4FB3FF 0%,#3A8EF0 48%,#2A5BD7 100%);background-attachment:fixed;color:#fff;font-family:'Fredoka','Nunito',system-ui,sans-serif;font-weight:500}
[data-style="g"] h1,[data-style="g"] h2,[data-style="g"] h3{font-weight:400;letter-spacing:.01em}
[data-style="g"] .qf h1,[data-style="g"] .lr h1,[data-style="g"] .open h1{color:#fff;text-shadow:0 3px 0 #1B2B6B,0 0 12px rgba(27,43,107,.5);-webkit-text-stroke:1px #1B2B6B;paint-order:stroke fill}
[data-style="g"] .qf .lead,[data-style="g"] .open .lead,[data-style="g"] .pickmsg{color:#fff;text-shadow:0 2px 0 #1B2B6B;font-weight:600}
[data-style="g"] .pickmsg{color:#FFE27A}
[data-style="g"] .card,[data-style="g"] .sample{background:linear-gradient(#FFFFFF,#E9F1FF);border:3px solid #1B2B6B;border-radius:28px;box-shadow:0 8px 0 #101C4A,inset 0 3px 0 #fff;color:#1B2B6B}
[data-style="g"] .card .sub{color:#4B5FA8}
[data-style="g"] .card h2.q{color:#1B2B6B}
[data-style="g"] .kicker{background:linear-gradient(#FFE27A,#FFC21A);color:#5A3A00;border:3px solid #1B2B6B;border-radius:12px;box-shadow:0 3px 0 #1B2B6B;font-family:'Lilita One',sans-serif;font-weight:400}
[data-style="g"] .btn{background:linear-gradient(#FFD65A 0%,#FFA51F 52%,#FF8A00 100%);color:#fff;border:3px solid #8A3B00;border-radius:20px;box-shadow:0 6px 0 #8A3B00,inset 0 3px 0 rgba(255,255,255,.6);text-shadow:0 2px 0 rgba(120,50,0,.55);font-size:23px;letter-spacing:.02em;position:relative}
[data-style="g"] .btn::before{content:"";position:absolute;left:12px;right:12px;top:5px;height:30%;border-radius:12px;background:linear-gradient(rgba(255,255,255,.55),rgba(255,255,255,0));pointer-events:none}
[data-style="g"] .btn:active{transform:translateY(5px);box-shadow:0 1px 0 #8A3B00,inset 0 3px 0 rgba(255,255,255,.5)}
[data-style="g"] .btn.ghost,[data-style="g"] .btn.ghost.cta{background:linear-gradient(#8FD0FF,#4FA3F5);border-color:#1B3A9A;box-shadow:0 6px 0 #1B3A9A,inset 0 3px 0 rgba(255,255,255,.55);color:#fff;text-shadow:0 2px 0 rgba(10,40,120,.6)}
[data-style="g"] .btn.cta:disabled{background:linear-gradient(#C9D4F0,#9FB0D8);border-color:#5C6FA8;box-shadow:0 5px 0 #5C6FA8;color:#fff;text-shadow:0 2px 0 rgba(40,60,120,.5);border-style:solid}
[data-style="g"] .opt,[data-style="g"] .chip3,[data-style="g"] .try{background:linear-gradient(#FFFFFF,#DCE8FF);color:#1B2B6B;border:3px solid #1B2B6B;border-radius:20px;box-shadow:0 5px 0 #1B2B6B,inset 0 2px 0 #fff;font-family:'Fredoka',sans-serif;font-weight:600}
[data-style="g"] .opt:hover:not(:disabled){background:linear-gradient(#FFFFFF,#CFE0FF)}
[data-style="g"] .opt.picked,[data-style="g"] .chip3.sel{background:linear-gradient(#B8F5A8,#4CCB5A);color:#0B4A1B;border-color:#1B5E2B;box-shadow:0 5px 0 #1B5E2B,inset 0 2px 0 rgba(255,255,255,.7)}
[data-style="g"] .opt.right{background:linear-gradient(#B8F5A8,#4CCB5A);border-color:#1B5E2B;box-shadow:0 5px 0 #1B5E2B}
[data-style="g"] .opt.wrong{background:linear-gradient(#FFC2C2,#FF7B7B);border-color:#9A2A2A;box-shadow:0 5px 0 #9A2A2A}
[data-style="g"] .opt .ic,[data-style="g"] .chip3 .ic{background:#fff;border:3px solid #1B2B6B;border-radius:14px;color:#1B2B6B}
[data-style="g"] .reply{background:linear-gradient(#FFF6D0,#FFE59A);border:3px solid #1B2B6B;border-radius:22px;box-shadow:0 5px 0 #1B2B6B;color:#1B2B6B}
[data-style="g"] .reply.ok{background:linear-gradient(#D9F8DF,#A9EDB6)}[data-style="g"] .reply.no{background:linear-gradient(#FFE0E0,#FFB9B9)}
[data-style="g"] .reply .tag{font-family:'Lilita One',sans-serif;font-weight:400;font-size:21px}
[data-style="g"] .tipnote{background:linear-gradient(#FFF6D0,#FFE59A);border:3px solid #1B2B6B;border-radius:18px;box-shadow:0 4px 0 #1B2B6B;color:#1B2B6B}
[data-style="g"] .tipnote b{color:#7A4A00}
[data-style="g"] .stickybar{background:linear-gradient(to top,#2A5BD7 72%,rgba(42,91,215,0));border:0;box-shadow:none}
[data-style="g"] .stickybar .trust{color:#fff;text-shadow:0 2px 0 #1B2B6B;opacity:1}
[data-style="g"] .fig,[data-style="g"] .scene2,[data-style="g"] .growscene,[data-style="g"] .tipart,[data-style="g"] .hero3{background:linear-gradient(#DDF3FF,#BFE6FF);border:3px solid #1B2B6B;border-radius:24px;box-shadow:inset 0 3px 0 #fff}
[data-style="g"] .top{background:transparent}
[data-style="g"] .brand{color:#fff;text-shadow:0 2px 0 #1B2B6B;font-size:20px}
[data-style="g"] .bar{height:20px;border:3px solid #1B2B6B;background:#16307E;box-shadow:inset 0 3px 0 rgba(0,0,0,.35)}
[data-style="g"] .bar i{background:linear-gradient(#FFE27A,#FFB300);border-radius:99px;box-shadow:inset 0 3px 0 rgba(255,255,255,.55)}
[data-style="g"] .steps{color:#fff;text-shadow:0 2px 0 #1B2B6B;font-weight:700;font-size:15px}
[data-style="g"] .link{color:#fff;text-shadow:0 2px 0 #1B2B6B;text-decoration:none}
[data-style="g"] .fineprint,[data-style="g"] .welcome p{color:#EAF4FF;text-shadow:0 1px 0 #1B2B6B}
[data-style="g"] .welcome{background:rgba(255,255,255,.2);border:3px solid #fff}
[data-style="g"] .deco{display:none}
[data-style="g"] .gate li,[data-style="g"] .items b{color:#1B2B6B}
.mascotrow{display:flex;justify-content:center;margin-top:6px;margin-bottom:-18px;position:relative;z-index:3}
.mascot{width:86px;height:93px;animation:bob 2.4s ease-in-out infinite;transform-origin:50% 100%;filter:drop-shadow(0 6px 0 rgba(16,28,74,.35))}
@keyframes bob{0%,100%{transform:translateY(0) scaleY(1)}45%{transform:translateY(-8px) scaleY(1.04)}70%{transform:translateY(0) scaleY(.96)}}
.tight .mascot{width:60px;height:65px}.tight .mascotrow{margin-bottom:-12px}.tighter .mascotrow{display:none}
.lvlc{display:flex;flex-direction:column;align-items:center;gap:2px;margin-top:10px;font-family:'Lilita One',sans-serif;font-size:34px;color:#fff;text-shadow:0 4px 0 #1B2B6B;-webkit-text-stroke:1.5px #1B2B6B;paint-order:stroke fill}
.stars{font-size:44px;color:#FFD23F;letter-spacing:6px;text-shadow:0 4px 0 #8A5B00;-webkit-text-stroke:2px #8A5B00;animation:pop 0.6s ease both}
.cf{position:fixed;width:9px;height:14px;border-radius:2px;pointer-events:none;z-index:60;animation:cf .9s ease-out forwards}
@keyframes cf{from{transform:translate(0,0) rotate(0);opacity:1}to{transform:translate(var(--dx),var(--dy)) rotate(var(--r));opacity:0}}
@media (prefers-reduced-motion:reduce){.mascot,.stars{animation:none!important}}
'''
css=css+extra
s=s[:a]+css+s[b:]
s=s.replace('<link href="https://fonts.googleapis.com/css2?family=Bricolage','<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Lilita+One&family=Fredoka:wght@500;600&family=Shrikhand&family=Bricolage',1)
# watercolor filter def
s=s.replace('<svg class="deco"','<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="wc" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6"/></filter></svg>\n<svg class="deco"',1)
for k,t in (('c','Green Thumb Watercolor'),('d','Green Thumb Retro'),('g','Green Thumb Game')):
    o=s.replace('<title>Green Thumb Check-In</title>',f'<title>{t}</title>\n<script>document.documentElement.setAttribute("data-style","{k}")</script>',1)
    open(f'quiz_{k}.html','w').write(o)
print('ok')
