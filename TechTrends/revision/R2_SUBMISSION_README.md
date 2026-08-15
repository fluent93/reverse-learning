# R2 Submission Package

## 제출 권장 파일

1. `Main_Manuscript_Reverse_Learning_Framework_R2.docx`
2. `Response_to_Reviewers_R2.docx`
3. 노란 표시 필드 보완을 완료한 `Title_Page_Reverse_Learning_Framework_R2.docx`
4. 포털이 별도 figure 업로드를 요구할 때만 `Figure1_Reverse_Learning_Framework_R2.png`

PDF는 제출하지 않는다.

## 편집 가능한 원천 및 재생성

- 전체 수정 이력 보존 원천(제출용 아님): `Manuscript_R2_improved.md`
- 선택적 하이라이트 제출 원천: `Manuscript_R2_marked.md`
- 하이라이트 없는 참고 원천: `Manuscript_R2_clean.md`
- 두 원천 생성: `.venv/bin/python TechTrends/revision/prepare_highlight_variants.py`
- 답변서 원천: `Response_to_Reviewers_R2.md`
- 평가 리포트: `Self_Evaluation_Report_KO.md` / `.docx`
- Title Page 생성: `.venv/bin/python TechTrends/revision/build_title_page_r2.py`
- 제출용 원고 생성:
  - `.venv/bin/python TechTrends/revision/build_docx.py --src TechTrends/revision/Manuscript_R2_marked.md --out TechTrends/revision/Main_Manuscript_Reverse_Learning_Framework_R2.docx --fig TechTrends/revision/Figure1_Reverse_Learning_Framework_R2.png`
- clean 참고 원고 생성:
  - `.venv/bin/python TechTrends/revision/build_docx.py --src TechTrends/revision/Manuscript_R2_clean.md --out TechTrends/revision/Main_Manuscript_Reverse_Learning_Framework_R2_Clean.docx --fig TechTrends/revision/Figure1_Reverse_Learning_Framework_R2.png`
- 답변서 생성:
  - `.venv/bin/python TechTrends/revision/build_response_docx.py --src TechTrends/revision/Response_to_Reviewers_R2.md --out TechTrends/revision/Response_to_Reviewers_R2.docx`

## 제출 전 필수 수동 확인

- R2 Title Page의 이메일, 전화번호, 주소, ORCID와 author bio가 모두 입력되어 있다.
- Microsoft Word에서 전체 선택 후 필드를 업데이트하여 페이지 번호를 확정한다.
- 표 행, Figure 1 가독성, 노란 하이라이트, References 새 페이지 시작을 육안 확인한다.
- Editorial Manager의 파일 designation과 저자 익명성 설정을 확인한다.
- 포털에는 선택적 하이라이트가 적용된 R2 원고를 제출한다. clean 원고는 별도 clean-copy 항목이 있거나 편집자가 요청한 경우에만 제출한다.

## 최종 개념 정합성

- Reverse Learning은 ML 알고리즘이나 computational path reversal을 뜻하지 않는다.
- 본 원고에서의 reversal은 생성형 AI가 완성도 높아 보이는 산출물을 이해보다 먼저 제공하면서 생기는 **교육학적 학습 순서의 역전**이다.
- 최종 R2에서는 ML, reversal learning, reverse engineering 비교를 삭제하고 flipped learning 및 backward design과의 교육학적 경계만 남겼다.
