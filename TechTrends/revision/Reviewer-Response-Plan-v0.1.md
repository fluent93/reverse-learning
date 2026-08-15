# TechTrends Major Revision — 리뷰어 대응 계획 (v0.1)

- 원고: "From AI-Generated Output to Learner Ownership: A Reverse Learning Framework for Generative AI-Mediated Education"
- 결정: Major Revision (Editor: Lucas Vasconcelos)
- 제출물: (1) 수정 원고(Word, 수정부분 하이라이트/색상 표시), (2) 2열 Response to Reviewers 표
- 상태 코드: ✅ 미착수 / 🟨 작성중 / ✅ 완료

---

## Editor 요구사항

| ID | 요구사항 | 대응 | 상태 |
|----|---------|------|------|
| E1 | 2열 표(리뷰어 지적 / 구체적 응답) 제출 | 본 문서를 기반으로 최종 Response Table 작성 | ✅ |
| E2 | 수정 부분 하이라이트 또는 색상 표시 | 수정 원고에 노란 하이라이트 적용 | ✅ |
| E3 | 편집 가능한 소스 파일만 제출 (PDF 불가) | Word(.docx)로 제출 | ✅ |

---

## Reviewer #1

### R1-1. 이론적 기여와 독창성 부족 (최우선)

**지적 요지:** 기존 개념(AI literacy, productive failure 등)과의 구별은 했지만, 프레임워크가 *무엇을 새롭게 설명하는지*를 확립하지 못함. 이론들(AI literacy, metacognition, ICAP, productive failure)이 어떻게 집합적으로 프레임워크를 뒷받침하고, 학습자가 AI 산출물에서 ownership으로 이동하는 *메커니즘*이 무엇인지 통합적 설명 필요. 명시할 것:
1. Reverse Learning이 도입하는 새로운 설명 메커니즘은 무엇인가?
2. 왜 기존 프레임워크로는 이 과정을 설명할 수 없는가?
3. Reverse Learning만이 포착하는 교육 현상은 무엇인가?

**원고 현재 상태:**
- §3 Theoretical Background가 이론을 병렬 나열 (3.1~3.6 각각 독립적)
- §6 + Table 2가 "무엇이 아닌지"는 다루지만 "무엇을 새롭게 설명하는지"는 미흡
- §2에서 "model-oriented conceptual contribution" (Jaakkola, 2020)으로 포지셔닝

**대응 방향:**
- §3 말미에 이론 통합 소절 신설 (예: "3.7 Toward an Integrated Account"):
  각 이론이 담당하는 단계를 명시하고(AI literacy→verification, metacognition→skepticism/prompting, ICAP→engagement 이동, productive failure→불완전 산출물의 교육적 가치), 이들이 결합해도 설명하지 못하는 공백 = **"artifact-first" 조건에서의 인식적 책임 이전(epistemic responsibility transfer) 메커니즘**을 논증
- 새 설명 메커니즘 후보(원고 기존 개념을 격상): "fluency-validity gap"의 발견이 productive struggle을 촉발하고, 이것이 재구성을 통해 ownership으로 전환되는 과정. 기존 이론은 (a) 학습자가 무(無)에서 시작하거나 (b) 인간 산출 자료를 다루는 것을 전제하므로, 완성형으로 보이는 기계 산출물에서 시작하는 학습을 설명하지 못함
- 고유하게 포착하는 현상: "understanding 이전에 polished artifact를 보유하는" 학습 상황 — §1, §3.1에 이미 서술되어 있으므로 이를 명시적 novelty claim으로 재구성
- R2-2와 연동해서 처리 (동일한 근본 지적)

**상태:** ✅

---

### R1-2. 학습자 준비도와 사전지식

**지적 요지:** 프레임워크는 학습자가 부정확성을 식별하고 검증·재구성할 수 있다고 가정하지만, 이 능력은 기존 학문 지식과 메타인지 기술에 의존. 추가 논의 필요: (a) 초보자 vs 전문가, (b) 형평성 함의, (c) 선수 역량, (d) 필요한 교수적 스캐폴드, (e) prompt literacy의 역할 (초기 프롬프트 품질이 산출물 품질을 좌우).

**원고 현재 상태:**
- §9 세 번째 objection에서 equity를 1개 문단으로만 언급 ("Learners with stronger prior knowledge may be better positioned...")
- 스캐폴드는 RQ3에서 연구 과제로만 제시
- prompt literacy는 명시적으로 다루지 않음

**대응 방향:**
- 신규 섹션 추가 (예: §7 앞 또는 §5 뒤에 "Learner Readiness, Prerequisites, and Scaffolding"):
  - 초보자/전문가 차이: 초보자에게는 verification 단계에서 외부 기준(소스 비교 템플릿, 체크리스트, 교수자 모델링) 제공 필요 — expertise reversal 관련 문헌 인용
  - 선수 역량 명시: 최소한의 도메인 지식, 소스 평가 능력, prompt literacy
  - 단계별 스캐폴드 표 또는 목록 제시 (기존 §7 assignments를 스캐폴드로 재연결)
  - prompt literacy: Stage 1(artifact 생성)과 Stage 4(iterative prompting)의 전제 조건으로 명시, 관련 문헌 인용
- §9 equity 문단을 이 신규 섹션과 상호 참조로 강화

**상태:** ✅

---

### R1-3. 분야별 적용성, 한계, 경계조건 + 최신 문헌

**지적 요지:** 검증과 재구성은 STEM/인문/사회과학 등 도메인마다 크게 다름. 구현 과제도 상이. 한계와 경계조건(boundary conditions) 논의 심화 필요. 최신 동료심사 문헌 보강: human-AI collaboration, cognitive offloading, prompt literacy, AI-supported learning.

**원고 현재 상태:**
- 분야별 차이 논의 없음 (§3.4에서 workplace 맥락만 간략 언급)
- Limitations 독립 섹션 없음 (§9 objections 형식으로 분산)
- 참고문헌이 2023~2024에 집중, cognitive offloading 문헌 없음

**대응 방향:**
- "Boundary Conditions and Disciplinary Variation" 소절 신설:
  - STEM: 코드 실행·계산 검증 등 객관적 검증 가능 ↔ 인문학: 해석적 타당성·전거 검증 중심 ↔ 사회과학: 근거의 맥락 의존성
  - 프레임워크가 잘 작동하는 조건 vs 한계 조건 (예: 정답이 없는 창작 과제, 검증 자원이 없는 환경)
- Limitations 명시 소절로 재구성
- 문헌 보강 (2024~2026 동료심사 논문):
  - cognitive offloading (예: Risko & Gilbert 및 GenAI 맥락 후속 연구)
  - human-AI collaboration / hybrid intelligence
  - prompt literacy 관련 실증 연구
  - AI-supported learning 최신 메타분석·리뷰
  - ※ 문헌 검색 후 목록 확정 필요

**상태:** ✅

---

### R1-4. 짧은 문단 통합

**지적 요지:** 1~2문장짜리 문단이 다수. 관련 아이디어를 통합해 흐름·일관성·학술적 완성도 개선.

**원고 현재 상태:** 확인됨 — 예: §4의 "The AI output is not the final answer. It is the starting point." (한 문장 문단), §4 sequence 제시부, 각 Stage 설명의 2문장 문단들, §10 결론부 다수.

**대응 방향:** 전체 원고를 훑으며 1~2문장 문단을 인접 문단과 병합. 수사적 효과를 위한 한 문장 문단은 최소한만 유지하거나 제거.

**상태:** ✅

---

### R1-5. Figure 1 재설계

**지적 요지:** 현재 그림이 선형(linear)인데 본문은 반복적(iterative) 과정을 기술. 더 강한 개념적 표현으로 발전시킬 것.

**원고 현재 상태:** Figure 1이 단순 화살표 나열 (A→B→...→G). 캡션에서만 "recursive"라고 서술.

**대응 방향:**
- 순환 루프(verification ↔ iterative prompting), 회귀 경로, 진입/이탈 조건을 시각화한 새 다이어그램 제작
- R2-2 대응(메커니즘 명시)과 일관되게: 그림에 단계 간 관계(전제·피드백 루프)를 표기
- 형식: Word 삽입 가능한 벡터/고해상도 이미지

**상태:** ✅

---

## Reviewer #2

### R2-1. 학습자 행위주체성(agency) 이론화 부재

**지적 요지:** 프레임워크가 학습자 행동(skepticism, verification, iterative prompting)을 나열하지만 *어떤 조건에서 실제로 그 행동이 일어나는지* 이론화하지 않음. 비판적으로 동기화된 학습자를 암묵적으로 가정하나 실제 학생 다수는 효율성 목적으로 GenAI 사용. Zimmerman SRL 모델이나 expectancy-value theory를 활용해 다음에 답할 것:
- 무엇이 학습자로 하여금 AI 산출물을 수용하지 않고 의심하게 만드는가?
- 어떤 기질적(dispositional)·맥락적(contextual)·과제 수준(task-level) 조건이 전체 과정의 전개 가능성을 높이거나 낮추는가?

**원고 현재 상태:** 동기·자기조절 이론 전무. Flavell 메타인지만 인용. "failure mode"로 수동적 수용을 기술하지만 왜 발생하는지 설명 없음.

**대응 방향:**
- 신규 이론 소절 추가 (예: "3.x Learner Agency and the Activation of Skepticism"):
  - Zimmerman SRL(forethought–performance–self-reflection)로 각 단계의 자기조절 요구 매핑
  - Expectancy-value theory로 참여 조건 설명: 과제 가치 인식(utility/attainment value)과 성공 기대가 낮으면 효율성 지향 사용으로 회귀
  - Skepticism 촉발 요인(trigger) 명시: (a) 기질적 — epistemic curiosity, need for cognition, AI에 대한 사전 신뢰 수준, (b) 맥락적 — 평가 설계(oral defense 예고 등), 교실 규범, 교수자 모델링, (c) 과제 수준 — 개인 관련성, 검증 가능성, 결과의 이해관계(stakes)
- 설계 함의로 연결: 프레임워크는 자연 발생을 기대하는 게 아니라 **평가 설계로 조건을 조성**한다는 논리 (§7과 연결) — 기존 원고의 assessment 설계가 사실상 이 "activation condition"임을 명시하면 자연스러움
- R1-2(준비도)와 상호 참조

**상태:** ✅

---

### R2-2. 개념적 프레임워크가 아니라 프로세스 모델로 읽힘

**지적 요지:** 7개 구성요소가 선형 순서로만 제시되고 요소 간 *관계와 메커니즘*이 이론화되지 않음. 개념적 프레임워크라면 구성개념이 무엇인지뿐 아니라 *어떻게, 왜* 연결되는지 명시해야 함. 선택지: (a) 프로세스 모델로 솔직히 재포지셔닝, 또는 (b) 구성요소 연결 메커니즘을 실질적으로 보강. 구체 질문:
- Verification은 iterative prompting의 전제인가, 동시 발생 가능한가?
- 학습자가 단계를 건너뛰거나 회귀할 수 있는가?
- 구성요소 간 잠재적 관계는 무엇인가?

**원고 현재 상태:**
- §5 도입부와 Figure 1 캡션에서 "not always strictly linear", "recursive"라고 서술하지만 관계를 체계적으로 명시하지 않음
- §2에서 Jaakkola (2020) model-oriented paper로 자기 정의 — "proposes relationships among constructs"라고 했으나 실제 본문이 이를 이행하지 못함 (리뷰어 지적의 근거)

**대응 방향 (옵션 b 권장 — R1-1과 동시 해결):**
- §5에 "Relationships Among Components" 소절 신설. 명시할 것:
  - 필수 선행 관계: Artifact와 Skepticism은 진입 조건, Explainable Ownership은 종결 조건
  - 동시/순환 관계: Verification ↔ Iterative Prompting은 상호 촉진 (검증 실패→재프롬프팅, 프롬프팅→새 검증 대상). 동시 발생 가능함을 명시
  - 건너뛰기/회귀: Contextual Integration에서 재검증으로 회귀 가능. 단, Skepticism 없이 Verification 없음(수동적 수용), Reconstruction 없이 Ownership 없음(표면 편집) — 이런 부정 경로를 failure mode와 연결해 메커니즘화
  - 관계 유형을 표 또는 명제(proposition) 형식으로 제시 (P1, P2... 형식이면 conceptual framework 관례에 부합)
- 새 Figure 1(R1-5)에 이 관계를 반영
- §2의 자기 포지셔닝 문구를 이행 내용과 일치하도록 미세 수정

**상태:** ✅

---

### R2-3. "Explainable Ownership" 구성개념 미발달

**지적 요지:** 가장 독창적이고 중요한 기여인데 이론적 발전이 가장 부족. ownership이 무엇을 의미하는지 불분명:
- authorship ("내가 만들었다")
- epistemic ownership ("내가 이해한다")
- identity-level ownership ("이것이 내 사고를 반영한다")
세 가지는 이론적 함의와 측정 방법이 다른 별개 구성개념. 프레임워크는 어떤 ownership을 지칭하는가? 모든 과제에 세 유형이 모두 필요한가, 왜/왜 아닌가?

**원고 현재 상태:** §3.1에서 "intellectual responsibility"로 정의, Stage 7에서 "explain, defend, revise without AI"로 조작화. 세 층위 구분 없음.

**대응 방향:**
- Stage 7 확장 또는 독립 소절 신설 ("Unpacking Explainable Ownership"):
  - 세 층위 정의 + 각각의 이론적 계보 연결 (authorship→academic integrity/authorship 문헌(WAME, Eaton), epistemic→epistemic cognition/responsibility, identity→psychological ownership / writer identity 문헌)
  - 프레임워크의 핵심 주장: Reverse Learning의 목표는 **epistemic ownership이 필수 코어**이고, authorship은 재정의됨(도구 사용을 배제하지 않는 책임 개념 — 기존 §3.1 서술 활용), identity-level은 과제 유형에 따라 가변적(성찰적·창작적 과제에서 중요, 기술적 검증 과제에서는 부차적)
  - 과제 유형별 필요 ownership 층위를 간단한 표로 제시 가능
  - 측정 함의: 층위별 평가 방법 매핑 (oral defense→epistemic, ownership statement→authorship, reflective memo→identity) — 기존 Table 3과 연결
- Abstract와 §4 정의에도 세분화된 정의 반영

**상태:** ✅

---

### R2-4. APA 7판 형식 (표, 참고문헌)

**지적 요지:** 표는 가로선만 사용(세로선·내부 테두리 제거). 참고문헌에서 저널명과 권 번호 이탤릭 처리. 두 섹션 전체를 APA 7판 기준으로 재검토.

**원고 현재 상태:** Word 파일에서 표 테두리·참고문헌 이탤릭 상태 직접 확인 필요 (텍스트 추출로는 서식 미확인). Table 1~4 존재.

**대응 방향:**
- Table 1~4: 상단·헤더 하단·하단 가로선만 남기고 세로선/내부선 제거
- References: 저널명·권수 이탤릭 전수 확인. 추가 점검 사항:
  - Mollick & Mollick (2023) arXiv 표기 형식
  - WAME, Anthropic, Flipped Learning Network 등 웹 자료의 APA 7 형식
  - Chi (2009), Lave & Wenger (1991), Papert (1980) 등 본문 인용 여부 확인 (미인용 시 삭제 — APA는 인용-참고문헌 일치 요구)

**상태:** ✅

---

## 작업 순서 제안

1. **이론 코어 (R1-1 + R2-2 통합 작업)** — 통합 이론 소절 + 구성요소 관계(명제) 명시. 가장 크고 다른 수정의 기반
2. **R2-1 (agency/동기)** — 신규 이론 소절, SRL·expectancy-value 문헌 확보
3. **R2-3 (explainable ownership 3층위)** — 독립 소절 + Table 3 연결
4. **R1-2 (준비도·스캐폴드·prompt literacy)** — 신규 섹션
5. **R1-3 (경계조건·분야별 차이·문헌 보강)** — 신규 소절 + 문헌 검색
6. **R1-5 (Figure 1 재설계)** — 1번 작업의 관계 명세를 시각화
7. **R1-4 (문단 통합)** — 내용 수정 완료 후 전체 윤문 단계에서 수행
8. **R2-4 (APA)** — 최종 단계
9. **E1 Response Table 작성 + E2 하이라이트 확인 → 제출**

## 유의사항

- 모든 신규 문헌은 실제 존재 여부 검증 후 인용 (AI 환각 인용 금지 — 원고 주제 특성상 치명적)
- 수정 원고는 Word로 유지, 수정부 하이라이트
- Response Table의 각 응답에는 수정 위치(섹션/페이지) 명시
