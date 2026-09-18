# -*- coding: utf-8 -*-
import pandas as pd, numpy as np
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
yrs=sorted(df.year.unique())
TOT=df.groupby(['year','gender'])['count'].sum()
T=TOT.xs('male',level=1); F=TOT.xs('female',level=1)
M=df[df.gender=='male']

# 2008 무자(쥐) ~ 2026 병오(말)
ANIMALS=['쥐','소','호랑이','토끼','용','뱀','말','양','원숭이','닭','개','돼지']
STEMS={y: ANIMALS[(y-2008)%12] for y in yrs}
# 띠 동물을 가리키는, 실제로 이름에 쓰이는 글자 (끝자리 기준)
CHARS={
 '쥐':[], '소':['소'], '호랑이':['호','범'], '토끼':['토'], '용':['용','룡'],
 '뱀':[], '말':['마'], '양':['양'], '원숭이':[], '닭':['계'], '개':[], '돼지':['해'],
}
# 지지(地支) 한자
BRANCH={'쥐':'자','소':'축','호랑이':'인','토끼':'묘','용':'진','뱀':'사',
        '말':'오','양':'미','원숭이':'신','닭':'유','개':'술','돼지':'해'}

def series(chars, g='male'):
    sub = df[df.gender==g]
    if not chars: return None
    m = sub.name.str.endswith(tuple(chars))
    c = sub[m].groupby('year')['count'].sum().reindex(yrs).fillna(0)
    t = (T if g=='male' else F).reindex(yrs)
    return c/t*10000, c
def chg(s): return {yrs[i]: (s.iloc[i]/s.iloc[i-1]-1) if s.iloc[i-1]>0 else np.nan for i in range(1,len(s))}

print('■ 12지 전체: 띠 해에 그 동물 글자가 늘었나 (남아, 끝자리)')
print(f"  {'띠':<5}{'글자':<8}{'해당 띠해 증감':<22}{'그 외 중앙값':>10}   19년 누적")
for a in ANIMALS:
    ch=CHARS[a]
    yrs_a=[y for y in yrs if STEMS[y]==a and y>yrs[0]]
    if not ch:
        print(f"  {a:<5}{'—':<8}이름에 쓰이지 않음")
        continue
    s,c=series(ch); g=chg(s)
    vals=' · '.join(f"{y} {g[y]:+.1%}" for y in yrs_a)
    rest=[g[y] for y in g if STEMS[y]!=a]
    tot=int(c.sum())
    flag=' ★' if all(g[y]>0.12 for y in yrs_a) else ''
    print(f"  {a:<5}{'/'.join(ch):<8}{vals:<22}{np.median(rest):>+10.1%}   {tot:>8,}명{flag}")

print('\n■ 지지 한자로 끝나는 이름 (자축인묘진사오미신유술해)')
print(f"  {'띠':<5}{'글자':<4}{'해당 띠해':<22}{'그 외 중앙값':>10}   누적")
for a in ANIMALS:
    ch=[BRANCH[a]]
    yrs_a=[y for y in yrs if STEMS[y]==a and y>yrs[0]]
    s,c=series(ch)
    if c.sum()<3000: 
        print(f"  {a:<5}{ch[0]:<4}(누적 {int(c.sum()):,}명, 표본 부족)")
        continue
    g=chg(s); rest=[g[y] for y in g if STEMS[y]!=a]
    vals=' · '.join(f"{y} {g[y]:+.1%}" for y in yrs_a)
    print(f"  {a:<5}{ch[0]:<4}{vals:<22}{np.median(rest):>+10.1%}   {int(c.sum()):>8,}명")

print('\n■ 출생아 수 자체는 띠를 타나')
b=T+F
for y in yrs[1:]:
    d=b[y]/b[y-1]-1
    print(f"  {y} {STEMS[y]:<4}{int(b[y]):>7}명  {d:+6.1%}" + ('  ★' if d>0 else ''))
