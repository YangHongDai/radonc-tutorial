# Radiation Oncology Interactive Tutorial

Bilingual (English / 繁體中文) interactive tutorial for radiation oncology, built on the scrna-interactive-tutorial template.

## 中文簡介

放射腫瘤學互動式教學。涵蓋 18 個臨床、物理、放射生物學主題，整合 1,037 篇 Estes 2025 關鍵試驗重點與 1,000 道雙語互動考題。直接開啟 `index.html` 即可使用，無需伺服器。

## English Description

A bilingual interactive Rad Onc tutorial covering 18 clinical / physics / radbio topic areas, integrated highlights from 1,037 Estes 2025 key studies, and a 1,000-question bilingual quiz. Open `index.html` in any modern browser.

## Contents

- **`index.html`** — hub landing page with all topics
- **Foundations**: `intro-clinical.html`, `physics.html`, `radbio.html`, `lingo.html`
- **Disease sites**: `cns.html`, `brain-mets.html`, `headneck.html`, `lung.html`, `breast.html`, `gi.html`, `gu.html`, `prostate.html`, `gyn.html`, `lymphoma.html`, `sarcoma.html`, `skin.html`, `peds.html`, `palliative.html`
- **`radonc-quiz/`** — 1,000-question bilingual quiz UI (single/multi/true-false)
- **`data/trials.json`** — extracted trial data used to generate integrated key-trial sections
- **`data/pdftext.json`** — raw PDF text for reference
- **`extracted/`** — generator scripts (Python)

## Source materials

- `Rad Onc Talks` — 70+ PDFs across 18 topic folders
- `Rad Onc Tables - Key Studies Estes 2025.xlsx` — Estes 2025 Key Studies tables

## Language toggle

Every page includes a floating **中文 / EN** toggle button (top right). Language preference is stored in `localStorage` under `radonc_lang`. All headings, cards, and quiz questions/answers/explanations are bilingual.

## Quiz

The 1,000-question bank comprises:

- **142 hand-authored core clinical questions** across physics, radbio, clinical intro, lingo, and every disease site (single / multi-select / true-false)
- **858 trial-templated questions** auto-generated from the Estes 2025 tables (per-trial interpretation and population questions), organized by disease site

The quiz supports practice mode (per-question feedback + explanations), exam mode (submit at end), random practice, wrong-answer review, marked-question review, per-user progress, and JSON import/export — inherited from the template UI.

## GitHub publish helper

This project includes Windows-friendly helper scripts in `scripts/` for publishing to GitHub.

First-time publish:

```powershell
cd C:\Users\ydai\Desktop\RT2\radonc-tutorial
.\scripts\publish-to-github.ps1 -RepoName radonc-tutorial -OpenCreatePage
```

That initializes Git locally, stages/commits the project, opens the GitHub repo creation page under `YangHongDai`, and prepares the `origin` remote. After creating the empty GitHub repo in your browser, rerun:

```powershell
.\scripts\publish-to-github.ps1 -RepoName radonc-tutorial
```

If you want the script to create the repo automatically through the GitHub API, set a token first:

```powershell
$env:GITHUB_TOKEN = "YOUR_TOKEN"
.\scripts\publish-to-github.ps1 -RepoName radonc-tutorial -CreateRepo
```

For later updates:

```powershell
.\scripts\push-update.ps1 -CommitMessage "Refine quiz translations"
```
