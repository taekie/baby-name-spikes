# -*- coding: utf-8 -*-
import pandas as pd, numpy as np
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
yrs = sorted(df.year.unique())
TOT = df.groupby(['year','gender'])['count'].sum()
T = TOT.xs('male',level=1)
TIGER=[2010,2022]; DRAGON=[2012,2024]
M = df[df.gender=='male']

def sh(mask):
    c = M[mask].groupby('year')['count'].sum().reindex(yrs).fillna(0)
    return c/T.reindex(yrs)*10000, c
def chg(s):
    return [np.nan]+[(s.iloc[i]/s.iloc[i-1]-1) if s.iloc[i-1]>0 else np.nan for i in range(1,len(s))]

print('■ 끝자리가 ‘호’인 남아 이름만 (○호)')
s,c = sh(M.name.str.endswith('호')); g=chg(s)
for i,y in enumerate(yrs):
    d='' if np.isnan(g[i]) else f'{g[i]:+.1%}'
    star='  ★' if y in TIGER else ''
    print(f"  {y}  {s.iloc[i]:6.1f}/만 {int(c.iloc[i]):>6}명 {d:>7}{star}")
r=sorted([(g[i],yrs[i]) for i in range(1,len(yrs))],reverse=True)
print(f"  → 1위 {r[0][1]}({r[0][0]:+.1%}) · 2위 {r[1][1]}({r[1][0]:+.1%}) · 3위 {r[2][1]}({r[2][0]:+.1%})")
rest=[g[i] for i in range(1,len(yrs)) if yrs[i] not in TIGER]
print(f"  → 나머지 17년 중앙값 {np.median(rest):+.1%}")
print(f"  → 고유 이름 수 2009 {M[(M.year==2009)&M.name.str.endswith('호')].name.nunique()}개 → 2010 {M[(M.year==2010)&M.name.str.endswith('호')].name.nunique()}개")

print('\n■ 백호 제외')
s2,_=sh(M.name.str.endswith('호') & (M.name!='백호')); g2=chg(s2)
print(f"  2010 {g2[yrs.index(2010)]:+.1%} · 2022 {g2[yrs.index(2022)]:+.1%}")

print('\n■ 끝자리가 ‘용·룡’인 남아 이름만')
s3,c3 = sh(M.name.str.endswith(('용','룡'))); g3=chg(s3)
for y in DRAGON:
    i=yrs.index(y); print(f"  {y}  {s3.iloc[i]:5.1f}/만 {int(c3.iloc[i]):>5}명  {g3[i]:+.1%}")
rest3=[g3[i] for i in range(1,len(yrs)) if yrs[i] not in DRAGON]
r3=sorted([(g3[i],yrs[i]) for i in range(1,len(yrs))],reverse=True)
print(f"  → 나머지 17년 중앙값 {np.median(rest3):+.1%} · 증가율 1위 {r3[0][1]}({r3[0][0]:+.1%}), 2위 {r3[1][1]}({r3[1][0]:+.1%})")

print('\n■ 대조군: 남아 이름 끝자리로 흔한 글자 (2008~2026 누적 기준 상위)')
last = M.assign(ch=M.name.str[-1]).groupby('ch')['count'].sum().sort_values(ascending=False)
print(f"  {'끝자':<4}{'2010':>9}{'2022':>9}{'나머지 중앙값':>13}   누적")
i10,i22 = yrs.index(2010), yrs.index(2022)
out=[]
for ch in last.head(14).index:
    s4,_=sh(M.name.str.endswith(ch)); g4=chg(s4)
    rest4=[g4[i] for i in range(1,len(yrs)) if yrs[i] not in TIGER]
    out.append((ch, g4[i10], g4[i22], np.median(rest4), int(last[ch])))
for ch,a,b,m,n in out:
    mark=' ←' if ch=='호' else ''
    print(f"  {ch:<4}{a:>+8.1%}{b:>+9.1%}{m:>+12.1%}   {n:>7,}명{mark}")
rank10=sorted(out,key=lambda x:-x[1]); rank22=sorted(out,key=lambda x:-x[2])
print(f"  → 2010년 1위 ‘{rank10[0][0]}’, 2022년 1위 ‘{rank22[0][0]}’")
