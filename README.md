# 갑자기 많아진 이름

2008~2026년 출생신고 이름 36만 건에서 특정 해에 갑자기 늘어난 이름을 찾아, 그해 방영·개봉한 작품과 대조한 분석입니다.

**https://taekie.github.io/baby-name-spikes/**

## 데이터

- `koreanname_rank.csv` (360,453행) — `year, gender, rank, name, count`. 2008~2026년 연도·성별 전체 이름.
- `born.json` — 연도별 출생아 수(성별·지역 포함).

출처는 [koreanname.me](https://koreanname.me)이고 원자료는 대법원 전자가족관계등록시스템입니다. 출생 시점이 아니라 **출생신고 기준**이며, 2026년은 9월까지의 부분 집계입니다.

검증: 연도·성별 `count` 합계가 같은 출처의 출생아 수와 19개 연도 모두 일치합니다.

## 스크립트

| 파일 | 하는 일 |
|---|---|
| `fetch.py` | koreanname.me API에서 전 연도 수집 → `koreanname_rank.csv`, `born.json` |
| `spike.py` | 출생아 1만 명당 비율로 정규화해 전년 대비 급등 탐지 |
| `check.py` | 특정 이름 목록의 최대 급등 연도 확인 |
| `traj.py` | 이름 하나의 19년 궤적을 터미널 스파크라인으로 출력 |
| `export.py` | 페이지에 쓸 시계열만 `series.json`으로 추출 |
| `build.py` | `series.json` + 본문 → `spike.html`(아티팩트용), `docs/index.html`(Pages용) |

```bash
python3 fetch.py     # 수집 (약 5분)
python3 export.py    # 시계열 추출
python3 build.py     # 페이지 생성
```

## 주의

시점의 일치를 보여줄 뿐 인과관계의 증명은 아닙니다. 작품이 이름을 유행시켰는지, 작가가 이미 유행하던 이름을 등장인물에 붙였는지는 이 데이터만으로 가릴 수 없습니다.
