import subprocess,json,time,csv,sys
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
BASE='https://koreanname.me'

def get(path,tries=6):
    for i in range(tries):
        t=subprocess.run(['curl','-s','--max-time','60','-A',UA,
            '-H','Accept: application/json, text/plain, */*',
            '-H','Referer: https://koreanname.me/',BASE+path],
            capture_output=True,text=True).stdout
        try: return json.loads(t)
        except Exception: time.sleep(1+i)
    raise RuntimeError('fail '+path)

# page p -> offset (p-1)*100, limit p*100  =>  pages 1,2,4,8,... tile without overlap
def year_names(year):
    out={'male':[],'female':[]}
    p=1
    while True:
        d=get(f'/api/rank/{year}/{year}/{p}')
        got=0
        for g in ('male','female'):
            rows=d[g]
            if rows:
                assert len(out[g])==(p-1)*100, (year,g,p,len(out[g]))
                out[g].extend(rows); got+=len(rows)
        if not got: break
        p*=2
        time.sleep(0.2)
    return out

born=get('/api/born')
json.dump(born,open('born.json','w'),ensure_ascii=False)
years=[y['year'] for y in born['year']]
print('years:',years,flush=True)

w=csv.writer(open('koreanname_rank.csv','w',newline='',encoding='utf-8-sig'))
w.writerow(['year','gender','rank','name','count'])
for y in years:
    d=year_names(y)
    for g in ('male','female'):
        for r in d[g]:
            w.writerow([y,g,r['rank'],r['name'],r['count']])
    print(y,'male',len(d['male']),'female',len(d['female']),flush=True)
