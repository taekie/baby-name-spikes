import pandas as pd, json
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
tot = df.groupby(['year','gender'])['count'].sum().rename('tot')
df = df.join(tot, on=['year','gender'])
df['share'] = df['count']/df['tot']*10000
yrs = sorted(df['year'].unique())
want = """훤:male 연우:female 시진:male 예승:female 라온:female 지안:female 해인:male 보검:male 이서:female
다미:female 이진:male 하리:female 도준:male 해이:female 해인:female 선재:male 태리:female 새벽:female
백호:male 범:male 미르:male 태호:male 강호:male
대겸:male 나겸:female 다겸:female 우재:male 시안:male 지온:female 하율:male 보겸:male
주원:male 연아:female 설현:female 수지:female 해린:female 제니:female 흥민:male 상혁:male 지용:male 성재:male 호정:female 영우:male 기훈:male 그래:male 새로이:male 은탁:female 동은:female 택:male""".split()
out={}
for w in want:
    n,g = w.split(':')
    p = df[(df['name']==n)&(df['gender']==g)].set_index('year')
    out[w] = [int(p['count'].get(y,0)) for y in yrs]
json.dump({'years':[int(y) for y in yrs],'series':out}, open('series.json','w'), ensure_ascii=False)
print(len(out),'series')

# share 버전도 같이
out2={}
for w in want:
    n,g = w.split(':')
    p = df[(df['name']==n)&(df['gender']==g)].set_index('year')
    out2[w] = [round(float(p['share'].get(y,0)),2) for y in yrs]
json.dump({'years':[int(y) for y in yrs],'count':out,'share':out2,
           'births':{str(int(y)):{g:int(df[(df.year==y)&(df.gender==g)]['count'].sum()) for g in ('male','female')} for y in yrs}},
          open('series.json','w'), ensure_ascii=False)
print('ok')
