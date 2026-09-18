# -*- coding: utf-8 -*-
import pandas as pd, numpy as np
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
yrs = sorted(df.year.unique())
TOT = df.groupby(['year','gender'])['count'].sum()
TIGER=[2010,2022]; DRAGON=[2012,2024]

def sh(mask, g='male'):
    s = df[(df.gender==g) & mask].groupby('year')['count'].sum().reindex(yrs).fillna(0)
    return s/TOT.xs(g,level=1).reindex(yrs)*10000, s

def chg(s):  # 전년 대비 증감률
    return [np.nan]+[(s.iloc[i]/s.iloc[i-1]-1) if s.iloc[i-1]>0 else np.nan for i in range(1,len(s))]

print('■ 남아 이름 중 ‘호’가 들어간 이름 전체 (합계 점유율)')
s,c = sh(df.name.str.contains('호',na=False)); g=chg(s)
for i,y in enumerate(yrs):
    d = '' if np.isnan(g[i]) else f'{g[i]:+.1%}'
    star = '  ★ 호랑이해' if y in TIGER else ''
    print(f"  {y}  {s.iloc[i]:6.1f}/만  {int(c.iloc[i]):>6}명  {d:>7}{star}")
ranked = sorted([(g[i],yrs[i]) for i in range(1,len(yrs))], reverse=True)
print(f"  → 19년 중 증가율 1위 {ranked[0][1]}년({ranked[0][0]:+.1%}), 2위 {ranked[1][1]}년({ranked[1][0]:+.1%}), 3위 {ranked[2][1]}년({ranked[2][0]:+.1%})")

print('\n■ 대조군: 다른 흔한 글자는 같은 해에 어땠나')
print(f"  {'글자':<4}{'2010년':>9}{'2022년':>9}   {'나머지 17년 중앙값':>10}")
for ch in list('호준우현민서진윤아은도하'):
    s2,_ = sh(df.name.str.contains(ch,na=False)); g2=chg(s2)
    i10,i22 = yrs.index(2010), yrs.index(2022)
    rest = [g2[i] for i in range(1,len(yrs)) if yrs[i] not in TIGER]
    mark = ' ←' if ch=='호' else ''
    print(f"  {ch:<4}{g2[i10]:>+8.1%}{g2[i22]:>+9.1%}   {np.median(rest):>+9.1%}{mark}")

print('\n■ ‘호’ 위치별')
for lab, mask in [('끝자리 (○호)', df.name.str.endswith('호',na=False)),
                  ('첫자리 (호○)', df.name.str.startswith('호',na=False))]:
    s3,c3 = sh(mask); g3=chg(s3)
    print(f"  {lab}: 2010 {g3[yrs.index(2010)]:+.1%} ({int(c3.iloc[yrs.index(2009)])}→{int(c3.iloc[yrs.index(2010)])}명)"
          f" · 2022 {g3[yrs.index(2022)]:+.1%}")

print('\n■ 2010년에 가장 많이 늘어난 ‘호’ 이름 (2009년 30명 이상)')
p = df[df.gender=='male'].pivot_table(index='name',columns='year',values='count').fillna(0)
p = p[p.index.str.contains('호')]
t = TOT.xs('male',level=1)
rows=[]
for n in p.index:
    a,b = p.loc[n,2009], p.loc[n,2010]
    if a>=30:
        rows.append((b/a-1, n, int(a), int(b), (b/t[2010])/(a/t[2009])-1))
rows.sort(reverse=True)
for r,n,a,b,adj in rows[:12]:
    print(f"  {n:<4}{a:>5} → {b:>5}명  {adj:+7.1%}")
print(f"  ... 30명 이상 ‘호’ 이름 {len(rows)}개 중 {sum(1 for r in rows if r[0]>0)}개가 증가")

print('\n■ 용의 해 검증 (2012 임진·2024 갑진)')
for lab, mask in [('‘용/룡’ 포함', df.name.str.contains('용|룡',na=False)),
                  ('미르', df.name=='미르')]:
    s4,c4 = sh(mask); g4=chg(s4)
    print(f"  {lab}: " + ' · '.join(f"{y} {g4[yrs.index(y)]:+.1%}" for y in DRAGON)
          + f"  (나머지 중앙값 {np.median([g4[i] for i in range(1,len(yrs)) if yrs[i] not in DRAGON]):+.1%})")

print('\n\n══ 2010 vs 2022, 왜 차이가 나나 ══')
print('\n■ 출생아 수 자체 (띠 출산 붐이 있었나)')
b = TOT.xs('male',level=1)+TOT.xs('female',level=1)
for y in [2008,2009,2010,2011,2012,2020,2021,2022,2023,2024]:
    d=(b[y]/b[y-1]-1) if y-1 in b else np.nan
    tag={2010:'  ★ 경인년(백호)',2022:'  ★ 임인년(흑호)',2012:'  ○ 임진년(흑룡)',2024:'  ○ 갑진년(청룡)'}.get(y,'')
    print(f"  {y}  {int(b[y]):>7}명  {'' if np.isnan(d) else f'{d:+.1%}':>7}{tag}")

print('\n■ ‘백호’ 한 이름을 빼면')
for y,prev in [(2010,2009),(2022,2021)]:
    for lab, extra in [('전체',None),('백호 제외','백호')]:
        m = df.name.str.contains('호',na=False)
        if extra: m = m & (df.name!=extra)
        s5,_ = sh(m); g5=chg(s5)
        print(f"  {y} {lab:<8}{g5[yrs.index(y)]:+.1%}")

print('\n■ 2022년에 늘어난 ‘호’ 이름 (2021년 30명 이상)')
t = TOT.xs('male',level=1)
rows=[]
for n in p.index:
    a,b2 = p.loc[n,2021], p.loc[n,2022]
    if a>=30: rows.append(((b2/t[2022])/(a/t[2021])-1, n, int(a), int(b2)))
rows.sort(reverse=True)
for r,n,a,b2 in rows[:10]: print(f"  {n:<4}{a:>5} → {b2:>5}명  {r:+7.1%}")
print(f"  ... 30명 이상 {len(rows)}개 중 {sum(1 for r in rows if r[0]>0)}개 증가")

print('\n■ 같은 이름의 두 호랑이해 반응 비교 (2009·2021 모두 30명 이상)')
print(f"  {'이름':<5}{'2010년':>9}{'2022년':>9}")
both=[]
for n in p.index:
    if p.loc[n,2009]>=30 and p.loc[n,2021]>=30:
        r10=(p.loc[n,2010]/t[2010])/(p.loc[n,2009]/t[2009])-1
        r22=(p.loc[n,2022]/t[2022])/(p.loc[n,2021]/t[2021])-1
        both.append((r10,r22,n))
both.sort(reverse=True)
for r10,r22,n in both[:10]: print(f"  {n:<5}{r10:>+8.1%}{r22:>+9.1%}")
print(f"  n={len(both)} · 중앙값 2010 {np.median([x[0] for x in both]):+.1%} / 2022 {np.median([x[1] for x in both]):+.1%}")
