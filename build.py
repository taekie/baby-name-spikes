import json
d=json.load(open('series.json'))
head = '''<title>갑자기 많아진 이름</title>
<style>
:root{
  --surface:#ffffff; --panel:#f5f7fa; --ink:#151a21; --ink2:#5b6572; --ink3:#8a94a3;
  --hair:#e3e8ef; --accent:#3b82f6; --accent-soft:rgba(59,130,246,.14); --mark:#c9761f;
  --chip:#eef2f7;
  --male:#2563eb; --male-soft:rgba(37,99,235,.13); --male-chip:#e7effd;
  --female:#d6336c; --female-soft:rgba(214,51,108,.12); --female-chip:#fceaf1;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --surface:#11151b; --panel:#1a2029; --ink:#e7edf5; --ink2:#9aa5b4; --ink3:#6c7787;
  --hair:#28303b; --accent:#5b9cf8; --accent-soft:rgba(91,156,248,.18); --mark:#dca059;
  --chip:#222a35;
  --male:#4a90e8; --male-soft:rgba(74,144,232,.20); --male-chip:#1b2a3d;
  --female:#d4568f; --female-soft:rgba(212,86,143,.18); --female-chip:#341f2b;
}}
:root[data-theme="dark"]{
  --surface:#11151b; --panel:#1a2029; --ink:#e7edf5; --ink2:#9aa5b4; --ink3:#6c7787;
  --hair:#28303b; --accent:#5b9cf8; --accent-soft:rgba(91,156,248,.18); --mark:#dca059;
  --chip:#222a35;
  --male:#4a90e8; --male-soft:rgba(74,144,232,.20); --male-chip:#1b2a3d;
  --female:#d4568f; --female-soft:rgba(212,86,143,.18); --female-chip:#341f2b;
}
*{box-sizing:border-box}
body{
  background:var(--surface); color:var(--ink); margin:0;
  font-family:'KoddiUD OnGothic',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  font-size:15px; line-height:1.65; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1080px; margin:0 auto; padding-inline:20px; padding-block:56px 72px}
h1{font-size:clamp(28px,5vw,40px); line-height:1.15; margin:0 0 14px; letter-spacing:-.02em; text-wrap:balance; font-weight:800}
.lede{color:var(--ink2); max-width:62ch; margin:0 0 8px; font-size:16px}
.lede b{color:var(--ink)}
.meta{color:var(--ink3); font-size:13px; margin-top:18px; font-variant-numeric:tabular-nums}
.legend{display:flex; align-items:center; gap:7px; font-size:13px; color:var(--ink2); margin:20px 0 0}
.legend .sw{width:11px; height:11px; border-radius:2px; display:inline-block}
.legend .sw.m{background:var(--male)}
.legend .sw.f{background:var(--female); margin-left:12px}
.rule{height:1px; background:var(--hair); border:0; margin:44px 0 0}
h2{font-size:21px; margin:46px 0 6px; letter-spacing:-.01em; font-weight:800}
h2 .n{color:var(--accent); font-weight:800; margin-right:10px; font-size:15px; vertical-align:2px}
.sub{color:var(--ink2); max-width:66ch; margin:0 0 26px; font-size:14.5px}
.sub b{color:var(--ink)}
.grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(268px,1fr)); gap:28px 24px}
.card{display:flex; flex-direction:column; gap:7px}
.card .top{display:flex; align-items:baseline; gap:8px; flex-wrap:wrap}
.nm{font-size:19px; font-weight:800; letter-spacing:-.01em}
.chip{font-size:11px; color:var(--ink2); background:var(--chip); border-radius:3px; padding:2px 6px; letter-spacing:.04em; font-weight:700}
.chip.m{color:var(--male); background:var(--male-chip)}
.chip.f{color:var(--female); background:var(--female-chip)}
.mult{margin-left:auto; font-size:12.5px; color:var(--ink3); font-variant-numeric:tabular-nums}
.mult b{font-weight:800; font-size:13.5px}
.card[data-g="male"] .mult b{color:var(--male)}
.card[data-g="female"] .mult b{color:var(--female)}
figure{margin:0}
svg{display:block; width:100%; height:auto; max-width:100%; overflow:visible}
.cap{font-size:13px; color:var(--ink2); line-height:1.5}
.cap .work{color:var(--ink); font-weight:700}
.cap .yr{color:var(--mark); font-weight:700; font-variant-numeric:tabular-nums}
.tbox{overflow-x:auto}
table{width:100%; border-collapse:collapse; font-size:14px; min-width:520px}
th,td{text-align:left; padding:10px 12px 10px 0; border-bottom:1px solid var(--hair); vertical-align:middle}
th{font-size:11.5px; letter-spacing:.06em; color:var(--ink3); font-weight:700}
td.num{font-variant-numeric:tabular-nums; white-space:nowrap; color:var(--ink2)}
.note{background:var(--panel); border-radius:6px; padding:18px 20px; font-size:13.5px; color:var(--ink2); margin-top:30px; max-width:72ch}
.note b{color:var(--ink)}
#tip{position:fixed; pointer-events:none; opacity:0; transition:opacity .09s;
  background:var(--ink); color:var(--surface); font-size:12px; padding:6px 9px; border-radius:4px;
  font-variant-numeric:tabular-nums; z-index:9; white-space:nowrap; line-height:1.45}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
'''

CASES = [
 ("주원","male",2011,"제빵왕 김탁구","KBS2 · 2010.6~9 · 최고 50.8% · 배우 주원"),
 ("훤","male",2012,"해를 품은 달","MBC · 2012.1~3 · 이훤"),
 ("연우","female",2012,"해를 품은 달","MBC · 2012.1~3 · 허연우"),
 ("우재","male",2013,"내 딸 서영이","KBS2 주말 · ~2013.3 · 평균 40.7% · 강우재"),
 ("예승","female",2013,"7번방의 선물","영화 · 2013.1 개봉 · 딸 예승"),
 ("시진","male",2016,"태양의 후예","KBS2 · 2016.2~4 · 유시진"),
 ("라온","female",2016,"구르미 그린 달빛","KBS2 · 2016.8~10 · 홍라온"),
 ("보검","male",2016,"배우 박보검","구르미 그린 달빛(2016)·남자친구(2018)"),
 ("지안","female",2018,"나의 아저씨","tvN · 2018.3~5 · 이지안"),
 ("해인","male",2018,"배우 정해인","밥 잘 사주는 예쁜 누나 · 2018.3~5"),
 ("이서","female",2020,"이태원 클라쓰","JTBC · 2020.1~3 · 조이서"),
 ("다미","female",2022,"배우 김다미","이태원 클라쓰(2020) 조이서 역"),
 ("이진","male",2022,"스물다섯 스물하나","tvN · 2022.2~4 · 백이진"),
 ("하리","female",2022,"사내 맞선","SBS · 2022.2~4 · 신하리"),
 ("태리","female",2022,"배우 김태리","아가씨(2016)~스물다섯 스물하나(2022)"),
 ("새벽","female",2022,"오징어 게임","넷플릭스 · 2021.9 · 강새벽"),
 ("도준","male",2023,"재벌집 막내아들","JTBC · 2022.11~12 · 진도준"),
 ("해이","female",2023,"일타 스캔들","tvN · 2023.1~3 · 남해이"),
 ("해인","female",2024,"눈물의 여왕","tvN · 2024.3~4 · 홍해인"),
 ("선재","male",2024,"선재 업고 튀어","tvN · 2024.4~5 · 류선재"),
]
PERSON_HIT = [
 ("연아","female",2009,"김연아","2009.3 세계선수권 최초 우승"),
 ("설현","female",2015,"AOA 설현","2015~16 광고 최다 모델"),
 ("제니","female",2018,"블랙핑크 제니","2016 데뷔, 2018년부터 상승"),
 ("해린","female",2023,"뉴진스 해린","2022.7 데뷔, 15년 정체 뒤 4배"),
]
PERSON_MISS = [
 ("흥민","male","손흥민","19년 통틀어 최대 10명"),
 ("상혁","male","페이커 이상혁","2008년 213명에서 계속 감소"),
 ("정후","male","이정후","MLB 진출 전후 변화 없음"),
 ("지성","male","박지성","2002·2010 월드컵 전후 변화 없음"),
 ("현진","male","류현진","2013 MLB 데뷔 해 ×1.08"),
 ("우진","male","김우진(양궁 3관왕)","2024년 ×1.1"),
]
Z12 = [
 ("호랑이","호·범","185,627명","2010 +31.4% · 2022 +15.3%","두 번 다 크게 증가",True),
 ("용","용·룡","13,029명","2012 +36.3% · 2024 +65.8%","두 번 다 크게 증가",True),
 ("양","양","8,544명","2015 +28.6%","730명 중 617명이 ‘태양’",False),
 ("돼지","해","1,449명","2019 −5.7%","동해·서해 등 바다 海",False),
 ("토끼","토","422명","2011 +4.2% · 2023 −28.1%","하루토·유우토 등 일본식 이름",False),
 ("말","마","418명","2014 +54.8% · 2026 +71.6%","연 20~38명, 유마·루마 등",False),
 ("소","소","274명","2009 −36.1% · 2021 −33.2%","연 7~21명",False),
 ("닭","계","109명","2017 +12.7%","연 5명",False),
 ("쥐 · 뱀 · 원숭이 · 개","—","0명","—","이름 글자로 쓰인 예 없음",False),
]
CONTROL = [
 ("호","+31.7%","+15.4%","+3.3%","170,479"),
 ("율","+23.8%","+2.6%","+0.5%","85,556"),
 ("윤","+16.1%","−7.0%","+5.6%","136,848"),
 ("준","+9.5%","−5.2%","+0.1%","358,867"),
 ("우","+5.7%","−0.7%","+1.7%","351,258"),
 ("후","+5.5%","+3.1%","−3.6%","83,860"),
 ("원","+1.3%","−2.7%","−1.6%","123,700"),
 ("빈","−3.9%","−6.0%","−0.3%","68,655"),
 ("훈","−4.6%","−0.7%","−7.8%","85,265"),
 ("현","−5.6%","+7.7%","−2.5%","192,572"),
 ("성","−8.1%","−2.6%","−3.8%","94,834"),
 ("진","−8.4%","+5.4%","+0.6%","104,681"),
 ("찬","−8.5%","+9.8%","−2.7%","89,232"),
 ("민","−10.1%","−17.4%","−4.9%","135,816"),
]
ZODIAC = [
 ("○호 합계|호끝","male",[2010,2022],"‘호’로 끝나는 남아 이름 전체","1만 명당 점유율. 두 호랑이해가 19년 중 1·2위"),
 ("범","male",[2010,2022],"호랑이의 순우리말","경인년과 임인년에 각각 반등"),
 ("백호","male",[2010,2022],"경인년 白虎","흰 호랑이는 60년에 한 번. 2022년에는 4명"),
 ("○용·○룡 합계|용룡끝","male",[2012,2024],"‘용·룡’으로 끝나는 남아 이름 전체","길게는 감소 추세인데 용의 해마다 반등한다"),
 ("미르","male",[2012,2024],"용의 순우리말","임진년과 갑진년에 각각 3배, 4배"),
 ("태호","male",[2010,2022],"돌림자의 전통형","2010년 +67%, 2022년 +19%로 반응이 약해졌다"),
]
UNKNOWN = [
 ("하율","male",2009),("대겸","male",2011),("나겸","female",2011),
 ("다겸","female",2014),("지온","female",2015),
 ("시안","male",2016),("보겸","male",2016),
]
FLAT = [
 ("영우","male","이상한 변호사 우영우","ENA · 2022 · 최고 17.5%","2022년 59→72명, 이후 다시 감소"),
 ("기훈","male","오징어 게임","넷플릭스 · 2021 · 전 세계 1위","2008년 128명에서 계속 감소, 반등 없음"),
 ("그래","male","미생","tvN · 2014 · 장그래","19년 통틀어 최대 3명"),
 ("새로이","male","이태원 클라쓰","JTBC · 2020 · 박새로이","최대 14명. 같은 작품 ‘이서’와 대조된다"),
 ("은탁","female","도깨비","tvN · 2016~17 · 지은탁","19년 통틀어 최대 2명"),
 ("동은","female","더 글로리","넷플릭스 · 2022~23 · 문동은","오히려 감소 추세"),
]

def js(o): return json.dumps(o,ensure_ascii=False)

body=['<div class="wrap">']
body.append('''<h1>갑자기 많아진 이름</h1>
<p class="lede">2008~2026년 출생신고 이름 36만 건을 연도별로 세어, 전년보다 갑자기 늘어난 이름을 찾았습니다. 상당수가 그해 방영하거나 개봉한 작품의 <b>등장인물</b> 이름이었습니다. 반면 아이돌이나 운동선수처럼 <b>실존 인물</b>의 이름은 거의 늘지 않았습니다.</p>
<p class="lede">출생아 수가 19년 사이 절반 아래로 줄었으므로 모든 그래프는 <b>출생아 1만 명당 비율</b>로 그렸습니다. 명수는 그래프 위에 커서를 올리면 나옵니다.</p>
<p class="meta">출처 koreanname.me(원자료: 대법원 전자가족관계등록시스템) · 2026년은 9월까지의 부분 집계 · 아래는 시점이 겹친다는 관찰이며 인과의 증명이 아닙니다</p>
<p class="legend"><span class="sw m"></span>남아<span class="sw f"></span>여아</p>
<hr class="rule">''')

def cards(lst):
    out=['<div class="grid">']
    for n,g,yr,work,det in lst:
        disp, _, raw = n.partition('|')
        key=f"{raw or disp}:{g}"
        n=disp
        yrs_ = yr if isinstance(yr,(list,tuple)) else [yr]
        marks = ','.join(str(v) for v in yrs_)
        ylab = ', '.join(str(v) for v in yrs_)
        out.append(f'''<div class="card" data-g="{g}">
  <div class="top"><span class="nm">{n}</span><span class="chip {"m" if g=="male" else "f"}">{"남아" if g=="male" else "여아"}</span><span class="mult" data-mult="{key}|{marks}"></span></div>
  <figure><svg data-k="{key}" data-mark="{marks}" viewBox="0 0 300 100" role="img" aria-label="{n} 연도별 추이"></svg></figure>
  <div class="cap"><span class="work">{work}</span> <span class="yr">{ylab}</span><br>{det}</div>
</div>''')
    out.append('</div>')
    return '\n'.join(out)

body.append('<h2><span class="n">01</span>등장인물의 이름</h2>')
body.append('<p class="sub">점선은 이름이 늘어난 해입니다. 출생신고는 태어난 지 한 달 안에 하므로 방영 중이거나 직후에 태어난 아기에게 곧바로 반영됩니다. 연말에 방영한 <b>재벌집 막내아들</b>의 ‘도준’이 이듬해에 늘어난 것이 그 시차를 보여줍니다. 한 작품에서 <b>여러 인물이 함께</b> 늘기도 합니다. 해를 품은 달은 남녀 주인공 ‘훤’과 ‘연우’가 같은 해에 올랐고, 내 딸 서영이는 ‘우재’와 함께 ‘성재’(155→223명), ‘호정’(46→61명)이 올랐습니다.</p>')
body.append(cards(CASES))

body.append('<h2><span class="n">02</span>실존 인물의 이름은 잘 안 쓴다</h2>')
body.append('<p class="sub">아이돌 75명의 이름을 데뷔 연도 기준으로 같이 훑었습니다. 대부분 움직이지 않았습니다. 절반 이상이 1.2배 안팎으로, 사실상 변화가 없습니다. 배수가 커 보이는 항목은 대개 규모가 없습니다. 세븐틴 승관은 0명에서 4명, 트와이스 사나는 2명에서 11명입니다. 등장인물의 이름은 빌려 쓸 수 있지만, <b>실존 인물의 이름은 그 사람이 곧바로 떠올라</b> 아이에게 붙이기 어려운 듯합니다.</p>')
body.append('<p class="sub" style="margin-bottom:22px">규모까지 움직인 예외는 넷입니다. 아이돌 셋과, 운동선수 중 유일한 사례인 김연아입니다. 뉴진스 해린은 15년간 100~160명대에 묶여 있다가 데뷔 이후 4배가 됐고, 아직 오르는 중입니다.</p>')
body.append(cards(PERSON_HIT))
body.append('<p class="sub" style="margin-top:30px">운동선수는 위상과 무관하게 거의 통하지 않았습니다. 김연아만 예외입니다.</p>')
rows=['<div class="tbox"><table style="min-width:440px"><thead><tr><th>이름</th><th>인물</th><th>결과</th></tr></thead><tbody>']
for n,g,who,res in PERSON_MISS:
    rows.append(f'<tr><td><b>{n}</b> <span class="chip {"m" if g=="male" else "f"}">{"남" if g=="male" else "여"}</span></td>'
                f'<td style="color:var(--ink2)">{who}</td><td style="color:var(--ink2)">{res}</td></tr>')
rows.append('</tbody></table></div>')
body.append('\n'.join(rows))

body.append('<h2><span class="n">03</span>호랑이해와 용의 해</h2>')
body.append('<p class="sub">가장 크게 늘어난 이름은 작품과 무관했습니다. 띠에 맞춰 짓는 관습이 12년 주기로 돌아옵니다. 개별 이름이 아니라 <b>‘호’로 끝나는 남아 이름 전체</b>(2010년 162개)를 합산해도 두 호랑이해가 19년 중 증가율 1위와 2위입니다. 돌림자는 보통 끝 글자에 오므로 끝자리만 셌습니다. 점선 두 개가 같은 띠의 두 해입니다.</p>')
body.append(cards(ZODIAC))

body.append('<p class="sub" style="margin-top:34px">남아 이름의 끝 글자로 흔한 14개를 같은 방식으로 계산했습니다. <b>두 호랑이해 모두 ‘호’가 1위</b>입니다. 나머지 글자는 호랑이해에도 평소와 비슷합니다.</p>')
rows=['<div class="tbox"><table style="min-width:460px"><thead><tr><th>끝 글자</th><th>2010년 경인년</th><th>2022년 임인년</th><th>나머지 17년 중앙값</th><th>19년 누적</th></tr></thead><tbody>']
for ch, a, b_, med, n in CONTROL:
    em=' style="font-weight:800;color:var(--male)"' if ch=='호' else ''
    rows.append(f'<tr><td{em}>○{ch}</td><td class="num"{em}>{a}</td><td class="num"{em}>{b_}</td><td class="num">{med}</td><td class="num">{n}명</td></tr>')
rows.append('</tbody></table></div>')
body.append('\n'.join(rows))

body.append('''<div class="note"><b>2022년은 왜 2010년의 절반인가.</b> 세 가지가 겹칩니다. 첫째, 2010년에는 띠에 맞춘 출산 자체가 있었습니다. 출생아 수가 2009년 −3.1%에서 2010년 +5.3%로 돌아섰고, 그 뒤로 이만큼 늘어난 해는 없습니다. 둘째, ‘○호’의 전통형이 2020년대에는 이미 사양세였습니다. 2009년과 2021년에 각각 30명을 넘긴 이름 23개를 같은 기준으로 보면 중앙값이 2010년 +35.6%, 2022년 +11.9%인데, 태호(+67%→+19%)나 수호(+39%→+0.2%), 찬호(−7%→−49%)처럼 한자 느낌이 강한 이름일수록 반응이 사라졌습니다. 셋째, 흰 호랑이는 60년에 한 번이라 2010년에만 따로 홍보됐습니다. ‘백호’라는 이름 자체가 2010년에 22배가 됐다가 2022년에는 4명에 그쳤습니다. 다만 이것이 주된 이유는 아닙니다. ‘백호’를 빼고 계산해도 2010년 증가율은 +30.3%로 거의 그대로입니다.</div>''')
body.append('<p class="sub" style="margin-top:30px">띠 작명 자체가 약해진 것은 아닙니다. 용의 해는 오히려 최근이 더 셉니다. ‘용·룡’으로 끝나는 이름 전체가 2012년 +36.3%, 2024년 +65.8%로 늘었습니다. 이 이름들은 19년간 63/만에서 27/만으로 줄어드는 중인데도, 두 용의 해에만 증가율 1위와 2위를 기록했습니다(나머지 해 중앙값 −10.4%). ‘미르’는 2012년 3배, 2024년 4배가 됐습니다. 2022년에도 은호(690→911명), 리호(121→196명)처럼 요즘 작명 취향에 맞는 이름은 그대로 반응했습니다.</p>')

body.append('<p class="sub" style="margin-top:34px">나머지 열 개 띠는 어떨까요. 같은 계산을 12지 전체에 돌리면 <b>호랑이와 용에서만</b> 효과가 나옵니다. 나머지는 그 동물을 가리키는 글자가 이름에 아예 쓰이지 않거나, 같은 글자가 전혀 다른 뜻으로 쓰입니다.</p>')
rows=['<div class="tbox"><table style="min-width:600px"><thead><tr><th>띠</th><th>끝 글자</th><th>19년 누적</th><th>해당 띠해 증감</th><th>판정</th></tr></thead><tbody>']
for a, ch, n, val, verdict, hit in Z12:
    em=' style="font-weight:800;color:var(--male)"' if hit else ''
    rows.append(f'<tr><td{em}>{a}</td><td class="num">{ch}</td><td class="num">{n}</td>'
                f'<td class="num"{em}>{val}</td><td style="color:var(--ink2)">{verdict}</td></tr>')
rows.append('</tbody></table></div>')
body.append('\n'.join(rows))
body.append('<p class="sub" style="margin-top:22px">쥐, 뱀, 원숭이, 개는 이름 글자로 쓰인 예가 없습니다. 소, 말, 토끼, 닭은 19년을 통틀어 100~400명대라 증감률이 의미를 갖지 못합니다. 양띠해인 2015년에 ‘양’으로 끝나는 이름이 28.6% 늘긴 했지만, 730명 중 617명이 ‘태양’이었습니다. 결국 이름에 올릴 만한 상서로운 동물이 호랑이와 용뿐이었던 셈입니다.</p>')

body.append('<h2><span class="n">04</span>원인을 못 찾은 이름</h2>')
body.append('<p class="sub">같은 기준에 걸렸지만 맞아떨어지는 작품을 찾지 못한 이름입니다. ‘겸’ 돌림(대겸, 나겸, 다겸, 보겸)은 2010년대 내내 유행했는데, 특정 연도에만 몰린 이유는 확인하지 못했습니다.</p>')
rows=['<div class="tbox"><table><thead><tr><th>이름</th><th>늘어난 해</th><th>전년 → 그해</th><th>배수</th><th>19년 추이</th></tr></thead><tbody>']
for n,g,yr in UNKNOWN:
    key=f"{n}:{g}"
    rows.append(f'<tr><td><b>{n}</b> <span class="chip {"m" if g=="male" else "f"}">{"남" if g=="male" else "여"}</span></td>'
                f'<td class="num">{yr}</td><td class="num" data-delta="{key}|{yr}"></td>'
                f'<td class="num" data-multp="{key}|{yr}"></td>'
                f'<td style="width:160px"><svg data-k="{key}" data-mark="{yr}" data-mini="1" viewBox="0 0 150 34"></svg></td></tr>')
rows.append('</tbody></table></div>')
body.append('\n'.join(rows))

body.append('<h2><span class="n">05</span>흥행해도 안 쓰는 이름</h2>')
body.append('<p class="sub">시청률이나 화제성만으로는 이름이 늘지 않습니다. 이름 자체가 요즘 작명 취향에 맞아야 합니다. 같은 <b>이태원 클라쓰</b>에서도 ‘조이서’는 크게 늘었지만 ‘박새로이’는 최대 14명에 그쳤습니다.</p>')
rows=['<div class="tbox"><table style="min-width:440px"><thead><tr><th>이름</th><th>작품</th><th>결과</th></tr></thead><tbody>']
for n,g,work,det,res in FLAT:
    rows.append(f'<tr><td><b>{n}</b> <span class="chip {"m" if g=="male" else "f"}">{"남" if g=="male" else "여"}</span></td>'
                f'<td><b>{work}</b><br><span style="color:var(--ink3);font-size:12.5px">{det}</span></td>'
                f'<td style="color:var(--ink2)">{res}</td></tr>')
rows.append('</tbody></table></div>')
body.append('\n'.join(rows))

body.append('''<div class="note"><b>읽을 때 주의할 점.</b> 이 페이지가 보여주는 것은 시점의 일치입니다. 작품이 이름을 유행시켰는지, 아니면 작가가 이미 유행하던 이름을 등장인물에 붙였는지는 이 데이터만으로 가릴 수 없습니다. ‘이서’, ‘하리’, ‘지안’처럼 이미 완만히 오르던 이름이 방영 연도에 기울기를 바꾼 경우가 특히 그렇습니다. 반대로 ‘훤’, ‘우재’, ‘예승’, ‘해이’처럼 직전까지 연 10명 안팎이던 이름이 한 해에 100명대가 된 경우는 작품 쪽 설명이 훨씬 자연스럽습니다.</div>''')
body.append('<p class="meta">전체 36만 453행 · 연도·성별 합계가 같은 출처의 출생아 수와 19개 연도 모두 일치함을 확인</p>')
body.append('</div><div id="tip"></div>')

script = '''<script>
const D = __DATA__;
const YRS = D.years, N = YRS.length;
const tip = document.getElementById('tip');
const NS='http://www.w3.org/2000/svg';
const el=(t,a)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;};

function draw(svg){
  const key=svg.dataset.k, marks=svg.dataset.mark.split(',').map(Number), mini=svg.dataset.mini==='1';
  const s=D.share[key], c=D.count[key];
  if(!s||!c) return;
  const male=key.split(':')[1]==='male';
  const LINE=male?'var(--male)':'var(--female)', FILL=male?'var(--male-soft)':'var(--female-soft)';
  const W=mini?150:300, H=mini?34:100;
  const PL=mini?2:4, PR=mini?2:4, PT=mini?4:16, PB=mini?4:18;
  const max=Math.max.apply(null,s)*1.14 || 1;
  const X=i=>PL+i*(W-PL-PR)/(N-1);
  const Y=v=>H-PB-(v/max)*(H-PT-PB);
  const MI=marks.map(m=>YRS.indexOf(m)).filter(i=>i>=0);

  if(!mini) MI.forEach(mi=>
    svg.appendChild(el('line',{x1:X(mi),x2:X(mi),y1:PT-8,y2:H-PB,stroke:'var(--mark)','stroke-width':1,'stroke-dasharray':'2 3',opacity:.9})));
  svg.appendChild(el('line',{x1:PL,x2:W-PR,y1:H-PB,y2:H-PB,stroke:'var(--hair)','stroke-width':1}));

  const pts=s.map((v,i)=>X(i)+','+Y(v)).join(' ');
  svg.appendChild(el('polygon',{points:PL+','+(H-PB)+' '+pts+' '+(W-PR)+','+(H-PB),fill:FILL,stroke:'none'}));
  svg.appendChild(el('polyline',{points:pts,fill:'none',stroke:LINE,'stroke-width':mini?1.4:2,'stroke-linejoin':'round','stroke-linecap':'round'}));

  MI.forEach(mi=>{
    svg.appendChild(el('circle',{cx:X(mi),cy:Y(s[mi]),r:mini?2.4:4,fill:LINE,stroke:'var(--surface)','stroke-width':2}));
    if(!mini){
      const t=el('text',{x:X(mi),y:Y(s[mi])-10,'text-anchor':mi>N-4?'end':(mi<3?'start':'middle'),
        fill:'var(--ink)','font-size':11,'font-weight':700,
        stroke:'var(--surface)','stroke-width':3.5,'stroke-linejoin':'round','paint-order':'stroke'});
      t.textContent=(key.endsWith('끝:male')? s[mi].toFixed(0)+'/만' : c[mi].toLocaleString()+'명'); svg.appendChild(t);
    }
  });
  if(!mini){
    [0,N-1].forEach((i,k)=>{
      const t=el('text',{x:X(i),y:H-5,'text-anchor':k?'end':'start',fill:'var(--ink3)','font-size':10});
      t.textContent=YRS[i]; svg.appendChild(t);
    });
    svg.appendChild(el('rect',{x:0,y:0,width:W,height:H,fill:'transparent'}));
    svg.addEventListener('pointermove',ev=>{
      const r=svg.getBoundingClientRect();
      const i=Math.max(0,Math.min(N-1,Math.round(((ev.clientX-r.left)/r.width*W-PL)/((W-PL-PR)/(N-1)))));
      tip.textContent=YRS[i]+'년 · '+c[i].toLocaleString()+'명 · 1만명당 '+s[i];
      tip.style.left=Math.min(innerWidth-tip.offsetWidth-8,ev.clientX+12)+'px';
      tip.style.top=(ev.clientY-38)+'px'; tip.style.opacity=1;
    });
    svg.addEventListener('pointerleave',()=>{tip.style.opacity=0;});
  }
}
document.querySelectorAll('svg[data-k]').forEach(draw);

function ratio(key,yr){const c=D.count[key]; if(!c) return {prev:0,cur:0,x:null};
  const b=key.endsWith('끝:male')?D.share[key]:c;   // 집계는 점유율 기준
  const i=YRS.indexOf(yr), p=c[i-1]||0;
  return {prev:p,cur:c[i],x:b[i-1]?(b[i]/b[i-1]):null};}
document.querySelectorAll('[data-mult]').forEach(e=>{
  const a=e.dataset.mult.split('|'), ys=a[1].split(',').map(Number);
  const parts=ys.map(y=>{const r=ratio(a[0],y);
    const v=(r.x && r.cur>=20)?('<b>×'+r.x.toFixed(1)+'</b>'):('<b>'+r.cur.toLocaleString()+'명</b>');
    return ys.length>1 ? (y+' '+v) : ('전년 '+v);});
  e.innerHTML=parts.join(' · ');
});
document.querySelectorAll('[data-delta]').forEach(e=>{
  const a=e.dataset.delta.split('|'), r=ratio(a[0],+a[1]);
  e.textContent=r.prev.toLocaleString()+' → '+r.cur.toLocaleString()+'명';
});
document.querySelectorAll('[data-multp]').forEach(e=>{
  const a=e.dataset.multp.split('|'), r=ratio(a[0],+a[1]);
  e.textContent=r.x?('×'+r.x.toFixed(1)):'신규';
});
</script>'''.replace('__DATA__', js(d))

page = head+'\n'.join(body)+script
open('spike.html','w',encoding='utf-8').write(page)

# GitHub Pages용 독립 문서
DESC='2008~2026년 신생아 이름 36만 건에서 특정 해에 갑자기 늘어난 이름을 찾아 드라마·영화 방영 시점과 대조했습니다.'
import os
os.makedirs('docs', exist_ok=True)
open('docs/index.html','w',encoding='utf-8').write(
'<!doctype html>\n<html lang="ko">\n<head>\n'
'<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width,initial-scale=1">\n'
f'<meta name="description" content="{DESC}">\n'
'<meta property="og:type" content="article">\n'
'<meta property="og:title" content="갑자기 많아진 이름">\n'
f'<meta property="og:description" content="{DESC}">\n'
'<meta name="twitter:card" content="summary">\n'
'<link rel="icon" href="data:image/svg+xml,'
'<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>'
'<text y=%22.9em%22 font-size=%2290%22>📈</text></svg>">\n'
'<style>*{box-sizing:border-box}html{color-scheme:light dark}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
+ page[:page.index('</style>')+8] + '\n</head>\n<body>\n'
+ page[page.index('</style>')+8:] + '\n</body>\n</html>\n')
print('ok: spike.html + docs/index.html')
