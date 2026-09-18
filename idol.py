import pandas as pd, numpy as np
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
tot = df.groupby(['year','gender'])['count'].sum().rename('tot')
df = df.join(tot, on=['year','gender'])
df['share'] = df['count']/df['tot']*10000
yrs = sorted(df['year'].unique())
piv = {g: df[df.gender==g].pivot_table(index='name',columns='year',values='share').fillna(0) for g in ('male','female')}
cnt = {g: df[df.gender==g].pivot_table(index='name',columns='year',values='count').fillna(0) for g in ('male','female')}

def rows(name,g,debut):
    if name not in piv[g].index: return None
    s=piv[g].loc[name].values; c=cnt[g].loc[name].values
    # 데뷔/전성기 연도 ±1 구간에서 최대 YoY
    best=(0,None)
    for y in range(debut, min(debut+3, yrs[-1])+1):
        i=yrs.index(y)
        if i==0: continue
        x=s[i]/(s[i-1]+0.05)
        if x>best[0]: best=(x,i)
    x,i=best
    if i is None: return None
    return dict(n=name,g=g,y=yrs[i],x=round(x,2),prev=int(c[i-1]),cur=int(c[i]),peak=int(c.max()),pky=yrs[int(np.argmax(c))])

# (이름, 성별, 기준연도, 설명)  — 데뷔/전성기
IDOL = [
 ("정국","male",2013,"BTS 데뷔"),("지민","male",2013,"BTS 데뷔"),("태형","male",2013,"BTS"),
 ("석진","male",2013,"BTS"),("윤기","male",2013,"BTS"),("호석","male",2013,"BTS"),("남준","male",2013,"BTS"),
 ("백현","male",2012,"EXO 데뷔"),("찬열","male",2012,"EXO"),("세훈","male",2012,"EXO"),("경수","male",2012,"EXO"),
 ("민석","male",2012,"EXO"),("종인","male",2012,"EXO"),
 ("제니","female",2016,"블랙핑크 데뷔"),("지수","female",2016,"블랙핑크"),("채영","female",2015,"트와이스"),
 ("다현","female",2015,"트와이스 데뷔"),("나연","female",2015,"트와이스"),("사나","female",2015,"트와이스"),
 ("정연","female",2015,"트와이스"),("지효","female",2015,"트와이스"),("미나","female",2015,"트와이스"),
 ("민지","female",2022,"뉴진스 데뷔"),("해린","female",2022,"뉴진스"),("혜인","female",2022,"뉴진스"),
 ("다니엘","female",2022,"뉴진스"),
 ("윈터","female",2020,"에스파"),("카리나","female",2020,"에스파"),("닝닝","female",2020,"에스파"),
 ("원영","female",2018,"아이즈원/아이브"),("유진","female",2018,"아이즈원/아이브"),("가을","female",2021,"아이브"),
 ("채원","female",2021,"르세라핌"),("사쿠라","female",2021,"르세라핌"),("은채","female",2021,"르세라핌"),
 ("정한","male",2015,"세븐틴"),("원우","male",2015,"세븐틴"),("민규","male",2015,"세븐틴"),
 ("도겸","male",2015,"세븐틴"),("승관","male",2015,"세븐틴"),("호시","male",2015,"세븐틴"),
 ("재현","male",2016,"NCT"),("도영","male",2016,"NCT"),("해찬","male",2016,"NCT"),("재민","male",2016,"NCT"),
 ("지성","male",2016,"NCT"),("현진","male",2018,"스키즈"),("승민","male",2018,"스키즈"),("필릭스","male",2018,"스키즈"),
 ("지용","male",2012,"지드래곤 전성기"),("태양","male",2012,"빅뱅"),("승리","male",2012,"빅뱅"),
 ("설현","female",2015,"AOA"),("수지","female",2011,"미쓰에이"),("아이유","female",2011,"아이유"),
 ("지은","female",2011,"아이유 본명"),("태연","female",2009,"소녀시대"),("윤아","female",2009,"소녀시대"),
 ("수영","female",2009,"소녀시대"),("서현","female",2009,"소녀시대"),("효연","female",2009,"소녀시대"),
 ("유리","female",2009,"소녀시대"),("티파니","female",2009,"소녀시대"),
 ("아린","female",2016,"오마이걸"),("유아","female",2016,"오마이걸"),("승희","female",2016,"오마이걸"),
 ("소연","female",2018,"아이들"),("미연","female",2018,"아이들"),("우기","female",2018,"아이들"),
 ("예지","female",2019,"있지"),("류진","female",2019,"있지"),("채령","female",2019,"있지"),("유나","female",2019,"있지"),
 ("은하","female",2015,"여자친구"),("예린","female",2015,"여자친구"),("신비","female",2015,"여자친구"),
 ("슬기","female",2014,"레드벨벳"),("예리","female",2015,"레드벨벳"),("아이린","female",2014,"레드벨벳"),
]
SPORT_ACTOR = [
 ("연아","female",2009,"김연아 세계선수권 우승"),
 ("주원","male",2011,"배우 주원(제빵왕 김탁구 2010)"),
 ("흥민","male",2018,"손흥민"),("지성","male",2010,"박지성"),("현진","male",2013,"류현진 MLB"),
 ("정후","male",2023,"이정후 MLB"),("하성","male",2021,"김하성 MLB"),("상혁","male",2016,"페이커 이상혁"),
 ("우진","male",2021,"안산·김우진 양궁"),("세리","female",2008,"박세리"),
 ("우빈","male",2013,"배우 김우빈"),("종석","male",2016,"이종석"),("수현","male",2014,"김수현"),
 ("시우","male",2016,"배우/이름 트렌드"),("민호","male",2010,"이민호"),("보영","female",2012,"이보영"),
 ("상윤","male",2013,"이상윤"),("우재","male",2013,"내 딸 서영이 강우재"),
]

def show(title, lst):
    print('\n=== '+title)
    print(f"{'이름':<5}{'성':<3}{'배수':<7}{'전년→그해':<16}{'설명'}")
    out=[]
    for n,g,y,d in lst:
        r=rows(n,g,y)
        if r: out.append((r,d))
    out.sort(key=lambda t:-t[0]['x'])
    for r,d in out[:22]:
        flag='★' if r['x']>=2 else (' ' if r['x']>=1.4 else '·')
        print(f"{flag}{r['n']:<5}{'남' if r['g']=='male' else '여':<3}×{r['x']:<6}{r['prev']:>5}→{r['cur']:>5}명 ({r['y']})  {d}")
    xs=[r['x'] for r,_ in out]
    print(f"  → 총 {len(xs)}개 중 ×2 이상 {sum(1 for x in xs if x>=2)}개, ×1.4 이상 {sum(1 for x in xs if x>=1.4)}개, 중앙값 ×{np.median(xs):.2f}")

show('아이돌 멤버 이름 (데뷔~+2년 최대 YoY)', IDOL)
show('배우·스포츠 스타 이름', SPORT_ACTOR)
