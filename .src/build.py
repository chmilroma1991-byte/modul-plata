# Збирає index.html: python3 .src/build.py
import json,html,os
R=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(R,'site_tpl.html')).read()
raw=open(os.path.join(R,'pub.json')).read();d=json.loads(raw)
CAT={'wash':'Пральні машини','dry':'Сушильні машини','dish':'Посудомийні машини','motor':'Двигуни'}
out=[]
for c in ['wash','dry','dish','motor']:
    by={}
    for r in d:
        if r[0]==c: by.setdefault(r[1],[]).append(r[3])
    for b in sorted(by):
        out.append('<p><b>%s %s:</b> %s</p>'%(CAT[c],html.escape(b),html.escape(', '.join(by[b]))))
t=t.replace('__ALLCODES__','\n'.join(out)).replace('__DATA__',raw.replace('</','<\\/'))
open(os.path.join(R,'..','index.html'),'w').write(t)
print('ok',len(d))
