import pandas as pd, numpy as np, sys
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
tot = df.groupby(['year','gender'])['count'].sum().rename('tot')
df = df.join(tot, on=['year','gender'])
df['share'] = df['count']/df['tot']*10000
yrs = sorted(df['year'].unique())
piv = {g: df[df.gender==g].pivot_table(index='name',columns='year',values='share').fillna(0) for g in ('male','female')}
cnt = {g: df[df.gender==g].pivot_table(index='name',columns='year',values='count').fillna(0) for g in ('male','female')}

def best(name, g):
    if name not in piv[g].index: return None
    s = piv[g].loc[name].values; c = cnt[g].loc[name].values
    r = [(s[i]/(s[i-1]+0.05), i) for i in range(1,len(yrs)) if c[i]>=60]
    if not r: return None
    x,i = max(r)
    return dict(name=name,g=g,year=yrs[i],x=round(x,1),prev=int(c[i-1]),cur=int(c[i]),peak=int(c.max()))

NAMES = """정국 지민 태형 남준 석진 윤기 호석 백현 찬열 세훈 경수 종대 준면 민석
다현 채영 지효 나연 정연 미나 사나 해린 혜인 민지 채원 윤진 원영 유진 예나 유리
정한 원우 민규 도겸 승관 재현 도영 해찬 재민 정우 현진 승민 선우 정원 성훈
아린 소연 미연 유나 채령 류진 예지 은석 원빈 승한 지용 지코 태양
흥민 연아 지성 강인 정후 하성 상혁 페이커 류현 세리 도영 준호 태현 시우 리우
주원 라온 하늘 이나 시연 예린 은하 유주 신비 엄지 슬기 예리 조이 윤아 수영 태연
서현 유나 지수 제니 리사 채원 은채 민정 지원 하윤 다온 아린 서진 유담 제이
우재 근호 기태 강호 훤 백호 미르 범 하율 지온 시안 보겸 대겸 나겸 다겸""".split()
seen=set(); rows=[]
for n in NAMES:
    if n in seen: continue
    seen.add(n)
    for g in ('male','female'):
        b = best(n,g)
        if b and b['x']>=1.5: rows.append(b)
rows.sort(key=lambda r:-r['x'])
print(f"{'이름':<5}{'성':<3}{'해':<6}{'배수':<7}{'전년→그해':<16}최고")
for r in rows[:40]:
    print(f"{r['name']:<6}{'남' if r['g']=='male' else '여':<3}{r['year']:<6}×{r['x']:<6}{r['prev']:>5}→{r['cur']:>5}명    {r['peak']}명")
