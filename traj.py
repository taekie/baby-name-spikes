import pandas as pd, numpy as np, sys
df = pd.read_csv('koreanname_rank.csv', encoding='utf-8-sig')
tot = df.groupby(['year','gender'])['count'].sum().rename('tot')
df = df.join(tot, on=['year','gender'])
df['share'] = df['count']/df['tot']*10000
yrs = sorted(df['year'].unique())

def traj(name, g):
    p = df[(df['name']==name)&(df['gender']==g)].set_index('year')
    s = [p['share'].get(y,0) for y in yrs]
    c = [p['count'].get(y,0) for y in yrs]
    mx = max(s) or 1
    bar = ''.join(' ▁▂▃▄▅▆▇█'[min(8,int(round(v/mx*8)))] for v in s)
    print(f"{name:<4}{g[0]} |{bar}| 최고 {max(c):.0f}명({yrs[int(np.argmax(s))]})  " +
          ' '.join(f"{y%100:02d}:{v:.0f}" for y,v in zip(yrs,c)))

print('연도:', ' '.join(str(y%100) for y in yrs))
for line in sys.stdin.read().split():
    n,g = line.split(':')
    traj(n,g)
