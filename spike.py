import pandas as pd, numpy as np
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
tot = df.groupby(['year','gender'])['count'].sum().rename('tot')
df = df.join(tot, on=['year','gender'])
df['share'] = df['count']/df['tot']*10000   # 1만명당

res=[]
for g, sub in df.groupby('gender'):
    p = sub.pivot_table(index='name', columns='year', values='share').fillna(0)
    c = sub.pivot_table(index='name', columns='year', values='count').fillna(0)
    yrs = sorted(p.columns)
    for i,y in enumerate(yrs):
        if i==0: continue
        prev = p[yrs[i-1]]
        cur  = p[y]
        nxt  = p[yrs[i+1]] if i+1<len(yrs) else pd.Series(np.nan, index=p.index)
        res.append(pd.DataFrame({
            'gender':g,'name':p.index,'year':y,
            'count':c[y],'cnt_prev':c[yrs[i-1]],
            'share':cur,'share_prev':prev,'share_next':nxt,
            'yoy': cur/(prev+0.05),           # 0.05 = 1만명당 스무딩
            'spike': cur/(np.maximum(prev,nxt.fillna(prev))+0.05),
        }))
r = pd.concat(res, ignore_index=True)
r = r[r['count']>=80]                          # 노이즈 컷
r.to_csv('spike_all.csv', index=False, encoding='utf-8-sig')

def show(d, title, n=25):
    print('\n=== '+title)
    for _,x in d.head(n).iterrows():
        print(f"{x['year']:.0f} {x['gender'][0]} {x['name']:<4} {x['cnt_prev']:>6.0f}→{x['count']:>6.0f}명  "
              f"({x['share_prev']:.1f}→{x['share']:.1f}/만)  x{x['yoy']:.1f}")

show(r.sort_values('yoy',ascending=False), '전년 대비 급등 (YoY)')
show(r.sort_values('spike',ascending=False), '단발성 급등 (전후 대비, 유행형)')
