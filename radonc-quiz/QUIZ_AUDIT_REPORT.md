# QUIZ_AUDIT_REPORT

## Scope

This audit covers the radiation oncology quiz database in:

- `data_original_backup.js`
- `data_refined.js`
- `validate_quiz.js`
- `build_refined_quiz.py`

The original live bank was preserved as `data_original_backup.js`. The rebuilt bank was written to `data_refined.js`. The original `data.js` was not overwritten during the rebuild.

## Source Provenance

The preserved bank is locally traceable to the talk-derived tutorial pipeline rather than a pure trial-table generator:

- `radonc-tutorial/extracted/gen_quiz_run.py` rebuilds the quiz from local topic pages.
- That generator explicitly excludes sections marked as `trial`, `evidence`, `study`, or `meta-analysis`.
- `radonc-tutorial/data/pdftext.json` contains text extracted from the local `Rad Onc Talks` PDF collection.

In other words, this refinement pass was anchored to the preserved talk-derived fact bank already present in the project, then rewritten into a cleaner SBA format.

## Workflow Completed

1. Parsed and backed up the existing bank into `data_original_backup.js`.
2. Audited answer distribution, duplicate stems, and distractor overlap.
3. Rebuilt all 1,000 items into `data_refined.js` with new stems, reshuffled answer keys, and longer explanations.
4. Created `validate_quiz.js` and validated both the original backup and the refined output.
5. Fixed an intermediate duplicate-option failure state in the generator so the final refined file passes validation with zero critical errors.

## High-Level Results

| Metric | Original backup | Refined output | Change |
|---|---:|---:|---:|
| Total questions | 1000 | 1000 | 0 |
| Retained with minor edits | 0 | 0 | n/a |
| Substantially rewritten | 0 | 1000 | +1000 |
| Net removed question records | 0 | 0 | 0 |
| Net newly added question records | 0 | 0 | 0 |
| Exact duplicate English stems | 482 | 132 | -350 |
| Distractors matching keyed truths elsewhere | 3000 | 1850 | -1150 |
| Validator critical issues | 0 | 0 | 0 |
| Validator warnings | 4842 | 2868 | -1974 |
| Oral-board case IDs added | 0 | 80 | +80 |
| Fallback distractor questions used in refined build | n/a | 660 | n/a |
| Rule-generated distractor questions used in refined build | n/a | 340 | n/a |

## Interpretation Of The Counts

- Every final item was regenerated rather than lightly edited. For that reason, the bank is best described as `1000 substantially rewritten questions`, not a small patch over the old wording.
- The validator's `distractor matches a keyed correct answer elsewhere` flag is intentionally conservative. Many remaining flags are now contrast statements from the same disease area rather than random cross-topic distractors, but the count still identifies sections that deserve manual faculty review.
- An intermediate rebuild briefly produced 97 duplicate-option critical errors; those were corrected before the final `data_refined.js` was accepted.

## Answer Distribution

| Letter | Original backup | Refined output |
|---|---:|---:|
| A | 278 | 275 |
| B | 226 | 228 |
| C | 243 | 250 |
| D | 253 | 247 |

The refined bank remains acceptably balanced without obvious long runs being mechanically forced.

## Question Count By Section

| Section | Count |
|---|---:|
| 放射物理學 | 16 |
| 放射生物學 | 62 |
| 臨床放射腫瘤學導論 | 10 |
| 縮寫與術語 | 23 |
| 原發性 CNS 腫瘤 | 57 |
| 腦轉移 | 36 |
| 頭頸部癌症 | 19 |
| 肺癌 | 39 |
| 乳癌 | 93 |
| 消化道癌症 | 148 |
| 泌尿生殖癌 | 62 |
| 攝護腺癌 | 67 |
| 婦科腫瘤 | 31 |
| 淋巴瘤 | 39 |
| 軟組織肉瘤 | 50 |
| 皮膚癌 | 83 |
| 兒童放射腫瘤 | 54 |
| 緩和放射治療 | 31 |
| 基礎口試 | 12 |
| 中樞神經口試 | 12 |
| 頭頸與胸腔口試 | 12 |
| 乳癌與消化道口試 | 11 |
| 泌尿與婦科口試 | 11 |
| 淋巴瘤肉瘤皮膚口試 | 11 |
| 兒童與緩和口試 | 11 |

## Difficulty Distribution By Section

Difficulty was estimated heuristically from rebuilt question intent:

- `L1`: foundational recall, definitions, anatomy, straightforward associations
- `L2`: standard board-style application, management, routine dose selection
- `L3`: advanced reasoning, constraints, nuanced management, complex dose or evidence interpretation

| Section | L1 | L2 | L3 |
|---|---:|---:|---:|
| 放射物理學 | 14 | 1 | 1 |
| 放射生物學 | 36 | 20 | 6 |
| 臨床放射腫瘤學導論 | 1 | 8 | 1 |
| 縮寫與術語 | 3 | 16 | 4 |
| 原發性 CNS 腫瘤 | 21 | 24 | 12 |
| 腦轉移 | 0 | 26 | 10 |
| 頭頸部癌症 | 5 | 12 | 2 |
| 肺癌 | 8 | 26 | 5 |
| 乳癌 | 32 | 41 | 20 |
| 消化道癌症 | 30 | 91 | 27 |
| 泌尿生殖癌 | 23 | 21 | 18 |
| 攝護腺癌 | 2 | 44 | 21 |
| 婦科腫瘤 | 6 | 13 | 12 |
| 淋巴瘤 | 9 | 27 | 3 |
| 軟組織肉瘤 | 8 | 32 | 10 |
| 皮膚癌 | 13 | 50 | 20 |
| 兒童放射腫瘤 | 8 | 39 | 7 |
| 緩和放射治療 | 2 | 24 | 5 |
| 基礎口試 | 0 | 9 | 3 |
| 中樞神經口試 | 2 | 7 | 3 |
| 頭頸與胸腔口試 | 1 | 10 | 1 |
| 乳癌與消化道口試 | 2 | 6 | 3 |
| 泌尿與婦科口試 | 1 | 8 | 2 |
| 淋巴瘤肉瘤皮膚口試 | 2 | 7 | 2 |
| 兒童與緩和口試 | 1 | 8 | 2 |

## Representative Corrections

### Example 1: Hodgkin lymphoma item repaired into a true single-best-answer dose question

Original defective item:

- Stem: `Which statement is correct about "Hodgkin lymphoma chemotherapy, ISRT/INRT/IFRT, and the logic of omitting RT"?`
- Keyed correct answer: `Early-stage favorable classic Hodgkin lymphoma: 20 Gy ISRT`
- Distractors included unrelated true statements from skin cancer, sarcoma, and wound-complication content.

Why it was defective:

- Distractors were not in the same conceptual category.
- The item invited pattern recognition because only one option belonged to Hodgkin lymphoma.
- The stem bundled multiple concepts but tested a single isolated dose fact.

Revised version:

- Stem: `For "Early-stage favorable classic Hodgkin lymphoma", which dose/fractionation is most appropriate?`
- Options: `10 Gy ISRT`, `25 Gy ISRT`, `15 Gy ISRT`, `20 Gy ISRT`

Why the revision is better:

- All four options are dose/fractionation choices.
- The question now tests one clean decision point.
- The distractors represent realistic numeric errors rather than unrelated facts.

### Example 2: Photon-beam property item repaired from cross-topic distractors into modality-focused contrast

Original defective item:

- Stem: `Which statement is correct about "Photon beam properties"?`
- Distractors included clinical consultation workflow, comet assay, and HyTEC constraints.

Why it was defective:

- Distractors came from unrelated subdomains.
- The answer could be found by spotting the only physics-looking option.
- The explanation simply repeated the correct statement.

Revised version:

- Stem: `Which statement regarding "Photons (X-rays)" is most accurate?`
- Distractors now contrast photon properties with proton indications, buildup behavior, and CSI-related concepts within the same broad teaching cluster.

Why the revision is better:

- The stem is more specific.
- The option set now behaves like a concept-recognition question rather than a random-topic filter.
- The explanation explicitly frames why the keyed statement matches the concept and why the other statements do not.

## Validation Summary

### Original backup

- Parsed successfully
- `window.QUIZ_DATA` present
- 0 critical issues
- 4842 warnings
- 482 exact duplicate English stems
- 3000 distractors that matched keyed correct answers elsewhere

### Final refined output

- Parsed successfully
- `window.QUIZ_DATA` present
- 0 critical issues
- 2868 warnings
- 132 exact duplicate English stems
- 1850 distractors that matched keyed correct answers elsewhere

## Remaining Uncertainties

1. The refined bank passes structural validation, but it still has a high warning count driven by conservative heuristics.
2. Exact duplicate stems remain at 132, especially where the underlying teaching label is broad or repeated.
3. The rebuild did not add per-question citation metadata, so guideline-sensitive items still rely on the local talk-derived source bank rather than explicit in-file references.
4. The rebuild was generation-based, not a full faculty line-by-line redline of all 1,000 items. Some clinically nuanced disease-site questions still merit expert review.
5. The difficulty labels in this report are heuristic and were not stored as schema fields in the final JavaScript.

## Sections That Would Benefit Most From Expert Human Review

- 淋巴瘤: nuanced ISRT dose/application questions, response-adapted therapy, and residual-disease scenarios
- 原發性 CNS 腫瘤: molecular classification and glioma management nuances
- 皮膚癌: mixed staging, pathology, and dose-pattern items
- 攝護腺癌: multiple dose/fractionation variants and systemic-therapy integration
- 消化道癌症: large section with the highest absolute content volume
- 口試複習: oral-board sequences are better structured now, but still deserve specialty-level polishing

## Sources Consulted

Local project sources:

- `radonc-tutorial/radonc-quiz/data.js`
- `radonc-tutorial/radonc-quiz/data_original_backup.js`
- `radonc-tutorial/radonc-quiz/data_refined.js`
- `radonc-tutorial/radonc-quiz/build_refined_quiz.py`
- `radonc-tutorial/radonc-quiz/validate_quiz.js`
- `radonc-tutorial/extracted/gen_quiz_run.py`
- `radonc-tutorial/data/pdftext.json`
- Local `Rad Onc Talks` PDF collection under `C:\Users\ydai\Desktop\RT2\Rad Onc Talks`

External guideline re-verification:

- Not completed as a fully cited per-question pass in this iteration.

## Final Status

The required artifact set was created and validated:

- `data_original_backup.js`
- `data_refined.js`
- `validate_quiz.js`
- `QUIZ_AUDIT_REPORT.md`

`data_refined.js` passes `validate_quiz.js` with zero critical errors. The bank is materially cleaner than the preserved version, but the warning profile and the remaining duplicate-stem count mean it should still be treated as a strong intermediate rebuild rather than a final faculty-signed release.
