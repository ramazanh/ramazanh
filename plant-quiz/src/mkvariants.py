import json,subprocess,re
subprocess.run(['python3','mkstyle.py'],check=True)
src=open('mk_land6.py').read()
a=src.index('# ---- illustrations');b=src.index('m3=phone(')
ns={}
exec("def ic(n):return ''\ndef pl(n,cls=''):return '<svg class=\"'+cls+'\" viewBox=\"0 0 240 260\" aria-hidden=\"true\"><use href=\"#plant-'+n+'\"/></svg>'\n"+src[a:b],ns)
secs=ns['secs'];fig=ns['fig']
art=''
for n,(h,body,cap,svg) in enumerate(secs,1):
    art+='<section class="as"><h3>'+h+'</h3>'+fig(svg,cap)+'<p>'+body+'</p></section>'
    if n==3: art+='<div class="inl"><p>Want help with your own plant?</p><button class="btn" id="lrcta" type="button">See what it needs <span aria-hidden="true">→</span></button></div>'
    if n==4: art+='<blockquote class="pq">Waiting a little is often the kindest thing you can do.</blockquote>'
long_html=('<article class="lr"><span class="tagp">Plant guide</span><h1>A gentle guide to caring for a plant you love</h1><p class="by">Plant care guide</p>'
 '<p class="lead">Plants can be easier than they look. These six ideas fit most houseplants, big or small.</p>'
 '<div class="hero3"><svg viewBox="0 0 240 260" aria-hidden="true"><use href="#plant-monstera"/></svg></div>'+art+
 '<div class="as"><p>You don’t need to fix everything today. Start with one small check, like the soil. Your plant will show you more over time. If you’d like help with your own plant, answer a few questions.</p></div>'
 '<p class="fineprint">General plant-care tips. Not a substitute for a local nursery.</p></article>')
def build(base,lv,title,out):
    s=open(base).read()
    s=s.replace("var LV='qf';","var LV='"+lv+"';",1)
    if lv=='long': s=s.replace("var LONG_HTML='';","var LONG_HTML="+json.dumps(long_html)+";",1)
    s=re.sub(r'<title>.*?</title>','<title>'+title+'</title>',s,1)
    open(out,'w').write(s)
build('quiz_c.html','qf','Green Thumb Quiz First','v_c_qf.html')
build('quiz_c.html','long','Green Thumb Long Read','v_c_long.html')
build('quiz_c.html','plan','Green Thumb Plan Preview','v_c_plan.html')
build('quiz_c.html','grow','Green Thumb Growing Plant','v_c_grow.html')
build('quiz_d.html','long','Green Thumb Retro Long Read','v_d_long.html')
build('quiz_g.html','game','Green Thumb Game','v_g_game.html')
print('built')
