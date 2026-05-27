# RLF 콘텐츠 파이프라인 — 단계별 수행 가이드

**버전:** v1.0  
**작성:** Changhan Ryu  
**목적:** Reverse Learning Framework 산출물을 멀티에이전트 방식으로 제작할 때, 각 단계에서 무엇을 어디서 어떻게 수행하고 state.json을 어떻게 업데이트하는지 기록한다.

---

## 전제

| 항목 | 내용 |
|------|------|
| **에이전트** | API 없음. 모든 LLM은 대화형 인터페이스로 사용 |
| **Drafter / Reviser / Verifier** | 폰 ChatGPT 앱 (GPT 계열) |
| **Critic / Finalist / Publisher** | Cursor Web 또는 Cursor Desktop (Claude Opus 계열) |
| **파일 커밋** | 폰 GitHub 앱 또는 Cursor Web |
| **Release / Publisher** | PC 또는 Mac Cursor Desktop |
| **상태 추적** | 레포 루트의 `state.json` (매 단계 후 수동 업데이트) |

---

## 파일 명명 규칙

| 파일 | 경로 예시 |
|------|----------|
| 브리프 | `briefs/<slug>.md` |
| 초안 | `drafts/v1.md`, `drafts/v2.md`, … |
| 리뷰 (JSON) | `reviews/v1-review.json` |
| 리뷰 (MD) | `reviews/v1-review.md` |
| 최종본 | `final/v1.0.md` |
| 검증 리포트 | `verification/v1.0-check.md` |
| 브런치 초안 | `posts/brunch_v1.0_ko.md` |
| LinkedIn 초안 | `posts/linkedin_v1.0_en.md` |
| 상태 파일 | `state.json` (레포 루트) |

---

## state.json 기본 구조

```json
{
  "schema_version": "1.0",
  "pipeline_id": "<slug>",
  "artifact_type": "<paper|checklist|rubric|guide|one_pager|blog_source|education>",
  "current_stage": "<kickoff|drafting|critiquing|revising|finalizing|verifying|awaiting_human_approval|publishing|done>",
  "target_version": "v1.0",
  "iteration": 0,
  "iteration_max": 3,
  "score_threshold": 90,
  "latest_draft": null,
  "latest_review": null,
  "latest_final": null,
  "latest_verification": null,
  "latest_total_score": null,
  "escalation_reason": null,
  "failure_log": [],
  "history": [],
  "human_gates": {
    "pr_url": "",
    "approved": false,
    "approved_at_utc": null,
    "approved_by": null,
    "publish_authorized": false
  },
  "config": {
    "drafter_model_intent": "gpt-5",
    "critic_model_intent": "claude-opus-4.7",
    "reviser_model_intent": "gpt-5",
    "finalist_model_intent": "claude-opus-4.7",
    "verifier_model_intent": "gpt-5",
    "publisher_model_intent": "claude-opus-4.7"
  }
}
```

---

## Critic ↔ Reviser 루프 판단 기준

```
Critic 점수 ≥ 90점  →  바로 Step 8 (Finalist)
Critic 점수 < 90점  →  Step 7 (Reviser)로 한 번 더
최대 3회 반복        →  3회 후에는 점수 무관 Step 8 (Finalist)로
```

---

## 전체 흐름 요약

```
Step 1  아이템 선정
Step 2  브랜치 생성
Step 3  브리프 작성
Step 4  Drafter (GPT)       →  drafts/v1.md
Step 5  커밋
Step 6  Critic (Claude)     →  reviews/v1-review.*      ← 루프 시작
Step 7  Reviser (GPT)       →  drafts/v2.md             ← 점수 < 90일 때
         Step 6으로 돌아가기  (최대 3회)
Step 8  Finalist (Claude)   →  final/v1.0.md
Step 9  Verifier (GPT)      →  verification/v1.0-check.md
Step 10 사람 확인 및 Merge
Step 11 Publisher (Claude)  →  posts/brunch_*.md + posts/linkedin_*.md
Step 12 게시 및 Release
```

---

## 단계별 상세 수행 내용

---

### Step 1. 프로젝트 아이템 선정

**수행 위치:** 어디서든 (메모, 구두 결정)

**할 일:**
- 이번에 만들 산출물 하나를 결정한다.
- `artifact_type`을 정한다: `paper` / `checklist` / `rubric` / `guide` / `one_pager` / `blog_source` / `education`
- 슬러그(slug)를 정한다: 소문자, 하이픈 구분. 예: `rlf-log-verification-v1`

**state.json 업데이트:** 없음 (브리프 작성 전)

---

### Step 2. 브랜치 생성

**수행 위치:** PC 브라우저 GitHub 또는 폰 GitHub 앱

**할 일:**
1. `main` 브랜치 선택
2. 브랜치 이름 입력: `feature/<slug>` 예: `feature/rlf-log-verification-v1`
3. Create branch

**주의:** `Compare & pull request` 버튼은 Step 10 전까지 누르지 않는다.

**state.json 업데이트:** 없음 (아직 파일 없음)

---

### Step 3. 브리프 작성

**수행 위치:** PC 브라우저 GitHub 또는 Cursor

**할 일:**
1. `briefs/_template.md` 내용을 전체 복사
2. 새 파일 `briefs/<slug>.md` 생성 (같은 `feature/<slug>` 브랜치에)
3. 아래 필드를 채운다:
   - Slug, Artifact type, Target version, Primary language
   - Audience (1차 사용자 / 2차 독자)
   - Purpose (한 문장)
   - Scope — 포함 / 제외 항목
   - Voice and tone
   - Acceptance criteria (Critic ≥ 90 기준)
4. 커밋 메시지 예: `chore: add brief for <slug>`

**state.json 업데이트:**
```json
{
  "pipeline_id": "<slug>",
  "artifact_type": "<선택한 타입>",
  "current_stage": "kickoff",
  "target_version": "v1.0"
}
```
`state.json.template`을 복사해서 `state.json`으로 저장 후 위 필드 수정. 같은 브랜치에 커밋.

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": null,
  "to_stage": "kickoff",
  "reason": "브리프 작성 완료. 파이프라인 시작.",
  "actor": "human",
  "rule_applied": null
}
```

---

### Step 4. Drafter — 초안 작성

**수행 위치:** 폰 ChatGPT 앱

**할 일:**
1. ChatGPT 새 대화 시작
2. **첫 번째 메시지:** `agents/01_drafter.md` 파일 안 `## System prompt` 섹션의 코드 블록(``` ``` ```) 전체를 복사해서 붙여넣기
3. **두 번째 메시지:** 아래 형식으로 전송

```
아래 브리프를 바탕으로 drafts/v1.md 파일 내용을 작성해줘.
YAML frontmatter 포함해서 전체 마크다운 파일로 출력해줘.

--- BRIEF ---
[briefs/<slug>.md 전체 내용 붙여넣기]
--- END ---
```

4. GPT가 출력한 마크다운 전체 복사

**Drafter Notes 섹션 확인:**
- GPT가 브리프에서 캐논(RLF 7단계 등)과 충돌하는 부분을 발견했으면 여기에 표시함
- 충돌이 있으면 Step 5 커밋 전에 사람이 판단

**state.json 업데이트 (Step 5 커밋과 함께):**
```json
{
  "current_stage": "critiquing",
  "latest_draft": "drafts/v1.md"
}
```

---

### Step 5. 초안 커밋

**수행 위치:** 폰 GitHub 앱

**할 일:**
1. 레포 → `feature/<slug>` 브랜치 확인
2. **Add file → Create new file**
3. 파일 경로: `drafts/v1.md`
4. Step 4에서 복사한 내용 붙여넣기
5. 커밋 메시지: `feat(draft): v1 by Drafter (gpt) for <slug>`
6. **Commit to `feature/<slug>`** 선택 (main이 아님)
7. `state.json` 열어서 `current_stage`, `latest_draft` 업데이트 후 커밋

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "kickoff",
  "to_stage": "critiquing",
  "reason": "Drafter 완료. drafts/v1.md 커밋.",
  "actor": "human",
  "rule_applied": 1
}
```

---

### Step 6. Critic — 평가

**수행 위치:** 폰 또는 PC 브라우저 Cursor Web

**할 일:**
1. Cursor Web에서 `fluent93/reverse-learning` 레포, `feature/<slug>` 브랜치 열기
2. **첫 번째 메시지:** `agents/02_critic.md`의 `## System prompt` 블록 붙여넣기
3. **두 번째 메시지:**

```
drafts/v1.md를 agents/rubrics/rlf-core-rubric.md의 루브릭으로 평가해줘.

아래 두 파일을 작성해줘:
1) reviews/v1-review.json (agents/schema/review.schema.json 스키마 준수)
2) reviews/v1-review.md (사람이 읽는 평가 서술)

JSON에 반드시 포함: total_score, recommendation (FINALIZE 또는 REVISE), dimensions, top_issues
```

4. Cursor Web 에이전트가 두 파일을 레포에 직접 커밋하거나, 결과를 복사해서 GitHub 앱으로 수동 커밋
5. 커밋 메시지: `feat(review): v1 critic — <점수>/100 — <FINALIZE|REVISE>`

**점수 확인:**
- `reviews/v1-review.json` 열어서 `total_score` 확인
- **≥ 90:** Step 8 (Finalist)로 이동
- **< 90:** Step 7 (Reviser)로 이동

**state.json 업데이트:**
```json
{
  "current_stage": "revising",
  "latest_review": "reviews/v1-review.json",
  "latest_total_score": <점수>
}
```
(점수 ≥ 90이면 `"current_stage": "finalizing"`)

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "critiquing",
  "to_stage": "revising",
  "reason": "Critic v1 완료. 점수 <N>/100. REVISE 권고.",
  "actor": "human",
  "rule_applied": 2
}
```

---

### Step 7. Reviser — 수정 (점수 < 90일 때만)

**수행 위치:** 폰 ChatGPT 앱

**할 일:**
1. ChatGPT 새 대화 시작
2. **첫 번째 메시지:** `agents/03_reviser.md`의 `## System prompt` 블록 붙여넣기
3. **두 번째 메시지:**

```
아래 초안과 리뷰를 바탕으로 drafts/v<n+1>.md를 작성해줘.
Reviser Changelog 섹션 반드시 포함.
전체 마크다운 파일로 출력해줘.

--- DRAFT v<n> ---
[drafts/v<n>.md 전체 내용]
--- END ---

--- REVIEW JSON ---
[reviews/v<n>-review.json 전체 내용]
--- END ---

--- REVIEW MD ---
[reviews/v<n>-review.md 전체 내용]
--- END ---
```

4. 결과 복사 → GitHub 앱 → `drafts/v<n+1>.md` 커밋
5. 커밋 메시지: `feat(draft): v<n+1> by Reviser — <N>개 이슈 반영`

**루프 판단:**
- `iteration` 값 확인
- iteration < 3이면 → Step 6 (Critic)으로 돌아가기
- iteration = 3이면 → Step 8 (Finalist)로 강제 이동

**state.json 업데이트:**
```json
{
  "current_stage": "critiquing",
  "latest_draft": "drafts/v<n+1>.md",
  "iteration": <이전값 + 1>
}
```

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "revising",
  "to_stage": "critiquing",
  "reason": "Reviser v<n+1> 완료. iteration <N>.",
  "actor": "human",
  "rule_applied": 3
}
```

---

### Step 8. Finalist — 최종본 작성

**수행 위치:** Cursor Web (Claude Opus)

**조건:** Critic 점수 ≥ 90 도달 OR iteration = 3 도달

**할 일:**
1. Cursor Web에서 `feature/<slug>` 브랜치 열기
2. **첫 번째 메시지:** `agents/04_finalist.md`의 `## System prompt` 블록 붙여넣기
3. **두 번째 메시지:**

```
최신 draft와 모든 review를 바탕으로 final/v1.0.md를 작성해줘.

반드시 포함:
- YAML frontmatter (모든 필수 필드)
- 본문 전체
- Ownership Statement 섹션
- Open Items for Verifier 섹션
- Changelog from Last Public Version (해당되는 경우)

state escalation_reason: <none 또는 iter_max>
```

4. 결과를 `final/v1.0.md`로 커밋
5. 커밋 메시지: `feat(final): v1.0 by Finalist — verifier 대기 중`

**state.json 업데이트:**
```json
{
  "current_stage": "verifying",
  "latest_final": "final/v1.0.md"
}
```

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "finalizing",
  "to_stage": "verifying",
  "reason": "Finalist 완료. final/v1.0.md 커밋.",
  "actor": "human",
  "rule_applied": 4
}
```

---

### Step 9. Verifier — 최종본 검증

**수행 위치:** 폰 ChatGPT 앱

**할 일:**
1. ChatGPT 새 대화 시작
2. **첫 번째 메시지:** `agents/05_verifier.md`의 `## System prompt` 블록 붙여넣기
3. **두 번째 메시지:**

```
아래 최종본을 검증하고 verification/v1.0-check.md를 작성해줘.
체크 항목 A1~F3 전부 포함. **Verdict:** PASS / PASS_WITH_FLAGS / FAIL 명시.

--- FINAL ---
[final/v1.0.md 전체 내용]
--- END ---

--- ONE-PAGER ---
[Reverse Learning Framework One-Pager.md 전체 내용]
--- END ---

--- CHECKLIST ---
[RLF-Checklist-AIOutputReview-v1.0.md 전체 내용]
--- END ---
```

4. 결과를 `verification/v1.0-check.md`로 커밋
5. 커밋 메시지: `feat(verify): v1.0 verifier — <PASS|PASS_WITH_FLAGS|FAIL>`

**판단:**
- **PASS / PASS_WITH_FLAGS:** Step 10으로 이동
- **FAIL:** Step 7 (Reviser)로 돌아가서 Verifier가 지적한 사항 수정 → 새 Critic → Finalist → Verifier 재실행

**state.json 업데이트:**
```json
{
  "current_stage": "awaiting_human_approval",
  "latest_verification": "verification/v1.0-check.md"
}
```
(FAIL인 경우 `"current_stage": "remediation"`)

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "verifying",
  "to_stage": "awaiting_human_approval",
  "reason": "Verifier PASS. 사람 승인 대기.",
  "actor": "human",
  "rule_applied": 5
}
```

---

### Step 10. 사람 확인 및 Merge

**수행 위치:** 폰 GitHub 앱 또는 PC 브라우저

**할 일:**
1. `verification/v1.0-check.md` 읽기
   - "Items the human must personally verify" 항목 직접 확인
2. `final/v1.0.md` 읽기
   - Ownership Statement가 내 실제 작업을 정확하게 반영하는지 확인
   - Known Quality Risks 섹션이 있으면 수용 여부 판단
3. 문제 없으면 → `feature/<slug>` → `main` PR 생성
4. PR 제목: `RLF Release — <artifact 제목> v1.0`
5. **Merge pull request**

**state.json 업데이트 (merge 전 마지막 커밋):**
```json
{
  "human_gates": {
    "approved": true,
    "approved_at_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "approved_by": "Changhan Ryu",
    "publish_authorized": false
  }
}
```

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "awaiting_human_approval",
  "to_stage": "publishing",
  "reason": "사람 승인 완료. Merge.",
  "actor": "human",
  "rule_applied": null
}
```

---

### Step 11. Publisher — 브런치 + LinkedIn 초안

**수행 위치:** PC 또는 Mac Cursor Desktop (대화형)

**할 일:**
1. `git checkout main && git pull` 로 merge된 최신 상태 받기
2. `publish/<slug>-v1.0` 브랜치 생성
3. Cursor Desktop 채팅 열기
4. **첫 번째 메시지:** `agents/06_publisher.md`의 `## System prompt` 블록 붙여넣기
5. **두 번째 메시지:**

```
final/v1.0.md와 verification/v1.0-check.md를 바탕으로 아래 두 파일을 작성해줘.

1) posts/brunch_v1.0_ko.md — 브런치 국문 (1,500~2,500자 본문 + 영문 요약)
2) posts/linkedin_v1.0_en.md — LinkedIn 영문 (150~300단어 + 국문 요약)

각 채널에 맞게 네이티브로 작성. 자동 번역 금지.
```

6. 두 초안을 검토하고 **개인 경험·톤** 수정
7. 특히 브런치 도입 단락은 직접 수정 권장
8. 커밋 메시지: `feat(posts): brunch + linkedin drafts for v1.0`

**state.json 업데이트:**
```json
{
  "current_stage": "publishing",
  "human_gates": {
    "publish_authorized": true
  }
}
```

---

### Step 12. 게시 및 GitHub Release

**수행 위치:** PC 또는 Mac

**할 일:**

**게시:**
1. 브런치 앱에서 `posts/brunch_v1.0_ko.md` 내용으로 포스팅
2. LinkedIn에서 `posts/linkedin_v1.0_en.md` 내용으로 포스팅
3. 각 파일 frontmatter 업데이트:
   - `status: published`
   - `canonical_url: <게시된 URL>`
4. 커밋 메시지: `docs(posts): mark v1.0 published`

**GitHub Release:**
1. 레포 → Releases → Draft a new release
2. Tag: `v1.0` (또는 `<artifact-slug>-v1.0`)
3. Target: `main`
4. Release title: `RLF-Log-Verification-v1.0` (산출물명으로)
5. 설명: final의 Purpose + 주요 특징 요약
6. Publish release

**README 업데이트:**
- `## Released Tools` 섹션에 새 항목 추가
- 커밋 메시지: `docs(readme): add <artifact> to released tools`

**state.json 업데이트:**
```json
{
  "current_stage": "done"
}
```

**history에 추가:**
```json
{
  "at_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "from_stage": "publishing",
  "to_stage": "done",
  "reason": "브런치 + LinkedIn 게시 완료. GitHub Release 생성.",
  "actor": "human",
  "rule_applied": null
}
```

---

## 전체 state.json 변화 흐름

| 단계 완료 후 | current_stage | 주요 변경 필드 |
|---|---|---|
| Step 3 (브리프) | `kickoff` | `pipeline_id`, `artifact_type` |
| Step 5 (초안 커밋) | `critiquing` | `latest_draft: "drafts/v1.md"` |
| Step 6 (Critic, REVISE) | `revising` | `latest_review`, `latest_total_score` |
| Step 6 (Critic, FINALIZE) | `finalizing` | 동일 |
| Step 7 (Reviser) | `critiquing` | `latest_draft: "drafts/v2.md"`, `iteration: 1` |
| Step 8 (Finalist) | `verifying` | `latest_final: "final/v1.0.md"` |
| Step 9 (Verifier, PASS) | `awaiting_human_approval` | `latest_verification` |
| Step 10 (Merge) | `publishing` | `human_gates.approved: true` |
| Step 11 (Publisher) | `publishing` | `human_gates.publish_authorized: true` |
| Step 12 (게시) | `done` | — |

---

## 참고 에이전트 파일

| 에이전트 | 파일 | 모델 |
|---------|------|------|
| Drafter | `agents/01_drafter.md` | ChatGPT (GPT 계열) |
| Critic | `agents/02_critic.md` | Cursor Web (Claude Opus) |
| Reviser | `agents/03_reviser.md` | ChatGPT (GPT 계열) |
| Finalist | `agents/04_finalist.md` | Cursor Web (Claude Opus) |
| Verifier | `agents/05_verifier.md` | ChatGPT (GPT 계열) |
| Publisher | `agents/06_publisher.md` | Cursor Desktop (Claude) |

---

## 자주 발생하는 문제

| 상황 | 대처 |
|------|------|
| Critic이 JSON 없이 텍스트만 줬다 | "결과를 ```json 코드 블록으로 다시 출력해줘" 요청 |
| Reviser가 주요 이슈를 Changelog에 안 적었다 | 해당 이슈 번호 언급하며 "이 이슈는 왜 빠졌는지 DISAGREEMENT로 명시해줘" 재요청 |
| Verifier가 FAIL을 줬다 | `state.json` `current_stage: "remediation"`, Reviser부터 재시작 |
| 실수로 main에 커밋했다 | feature 브랜치로 돌아가서 계속 진행. main 오커밋은 다음 PR 때 무시됨 |
| 어느 단계까지 했는지 잊어버렸다 | `state.json`의 `current_stage`와 `history` 마지막 항목 확인 |
| 브랜치를 바꿨는데 파일 목록이 같아 보인다 | 정상. feature 브랜치는 main 파일을 모두 포함하고 추가 파일만 더 보임 |
