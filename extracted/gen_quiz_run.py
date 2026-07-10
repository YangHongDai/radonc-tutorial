# -*- coding: utf-8 -*-
"""Build the Rad Onc quiz from talk-derived tutorial pages.

This version intentionally removes the old trial-only bank and rebuilds the
question set from the tutorial's talk-topic pages, with a separate oral-boards
section made from high-yield management facts.
"""

from __future__ import annotations

import html
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "radonc-quiz" / "data.js"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TARGET_MAIN = 920
TARGET_ORAL = 80
TARGET_TOTAL = TARGET_MAIN + TARGET_ORAL
PAGE_CAP = 90

RNG = random.Random(42)
LETTERS = "ABCD"

PAGE_CONFIG = [
    {
        "file": "physics.html",
        "top_zh": "基礎入門",
        "top_en": "Foundations",
        "sub_zh": "放射物理學",
        "sub_en": "Radiation Physics",
    },
    {
        "file": "radbio.html",
        "top_zh": "基礎入門",
        "top_en": "Foundations",
        "sub_zh": "放射生物學",
        "sub_en": "Radiation Biology",
    },
    {
        "file": "intro-clinical.html",
        "top_zh": "基礎入門",
        "top_en": "Foundations",
        "sub_zh": "臨床放射腫瘤學導論",
        "sub_en": "Clinical Rad Onc",
    },
    {
        "file": "lingo.html",
        "top_zh": "基礎入門",
        "top_en": "Foundations",
        "sub_zh": "縮寫與術語",
        "sub_en": "Acronyms & Lingo",
    },
    {
        "file": "cns.html",
        "top_zh": "中樞神經系統",
        "top_en": "Central Nervous System",
        "sub_zh": "原發性 CNS 腫瘤",
        "sub_en": "Adult Primary CNS",
    },
    {
        "file": "brain-mets.html",
        "top_zh": "中樞神經系統",
        "top_en": "Central Nervous System",
        "sub_zh": "腦轉移",
        "sub_en": "Brain Metastases",
    },
    {
        "file": "headneck.html",
        "top_zh": "頭頸與胸腔",
        "top_en": "Head, Neck & Thorax",
        "sub_zh": "頭頸部癌症",
        "sub_en": "Head & Neck",
    },
    {
        "file": "lung.html",
        "top_zh": "頭頸與胸腔",
        "top_en": "Head, Neck & Thorax",
        "sub_zh": "肺癌",
        "sub_en": "Lung Cancer",
    },
    {
        "file": "breast.html",
        "top_zh": "乳癌與消化道",
        "top_en": "Breast & GI",
        "sub_zh": "乳癌",
        "sub_en": "Breast Cancer",
    },
    {
        "file": "gi.html",
        "top_zh": "乳癌與消化道",
        "top_en": "Breast & GI",
        "sub_zh": "消化道癌症",
        "sub_en": "Gastrointestinal",
    },
    {
        "file": "gu.html",
        "top_zh": "泌尿與婦科",
        "top_en": "GU & Gyn",
        "sub_zh": "泌尿生殖癌",
        "sub_en": "Genitourinary",
    },
    {
        "file": "prostate.html",
        "top_zh": "泌尿與婦科",
        "top_en": "GU & Gyn",
        "sub_zh": "攝護腺癌",
        "sub_en": "Prostate Cancer",
    },
    {
        "file": "gyn.html",
        "top_zh": "泌尿與婦科",
        "top_en": "GU & Gyn",
        "sub_zh": "婦科腫瘤",
        "sub_en": "Gynecologic",
    },
    {
        "file": "lymphoma.html",
        "top_zh": "淋巴瘤、肉瘤與皮膚",
        "top_en": "Lymphoma, Sarcoma & Skin",
        "sub_zh": "淋巴瘤",
        "sub_en": "Lymphoma",
    },
    {
        "file": "sarcoma.html",
        "top_zh": "淋巴瘤、肉瘤與皮膚",
        "top_en": "Lymphoma, Sarcoma & Skin",
        "sub_zh": "軟組織肉瘤",
        "sub_en": "Sarcoma",
    },
    {
        "file": "skin.html",
        "top_zh": "淋巴瘤、肉瘤與皮膚",
        "top_en": "Lymphoma, Sarcoma & Skin",
        "sub_zh": "皮膚癌",
        "sub_en": "Skin Cancer",
    },
    {
        "file": "peds.html",
        "top_zh": "兒童與緩和",
        "top_en": "Pediatrics & Palliative",
        "sub_zh": "兒童放射腫瘤",
        "sub_en": "Pediatrics",
    },
    {
        "file": "palliative.html",
        "top_zh": "兒童與緩和",
        "top_en": "Pediatrics & Palliative",
        "sub_zh": "緩和放射治療",
        "sub_en": "Palliative RT",
    },
]

ORAL_CONFIG = [
    {
        "source_top_zh": "基礎入門",
        "sub_zh": "基礎口試",
        "sub_en": "Foundations Oral Boards",
        "quota": 12,
    },
    {
        "source_top_zh": "中樞神經系統",
        "sub_zh": "中樞神經口試",
        "sub_en": "CNS Oral Boards",
        "quota": 12,
    },
    {
        "source_top_zh": "頭頸與胸腔",
        "sub_zh": "頭頸與胸腔口試",
        "sub_en": "Head, Neck & Thorax Oral Boards",
        "quota": 12,
    },
    {
        "source_top_zh": "乳癌與消化道",
        "sub_zh": "乳癌與消化道口試",
        "sub_en": "Breast & GI Oral Boards",
        "quota": 11,
    },
    {
        "source_top_zh": "泌尿與婦科",
        "sub_zh": "泌尿與婦科口試",
        "sub_en": "GU & Gyn Oral Boards",
        "quota": 11,
    },
    {
        "source_top_zh": "淋巴瘤、肉瘤與皮膚",
        "sub_zh": "淋巴瘤肉瘤皮膚口試",
        "sub_en": "Lymphoma, Sarcoma & Skin Oral Boards",
        "quota": 11,
    },
    {
        "source_top_zh": "兒童與緩和",
        "sub_zh": "兒童與緩和口試",
        "sub_en": "Pediatrics & Palliative Oral Boards",
        "quota": 11,
    },
]

TRIAL_MARKERS = [
    "trial",
    "meta-analysis",
    "meta analysis",
    "phase ii",
    "phase iii",
    "phase iv",
    "randomized",
    "randomised",
    "prospective",
    "retrospective",
    "study",
    "studies",
    "evidence",
    "nejm",
    "jco",
    "lancet",
    "rtog",
    "nrg",
    "eortc",
    "nsabp",
    "calgb",
    "gog",
    "trog",
    "swog",
    "ghsg",
    "ebctcg",
    "acosog",
    "amaros",
    "cross",
    "pacific",
    "rapido",
    "portec",
    "stamede",
    "stampede",
    "prodige",
    "convert",
    "pace-b",
    "checkmate",
    "stupp",
    "noa-04",
    "catnon",
    "esopec",
    "classen",
    "lowry",
    "fort",
    "uk fast",
    "opera",
    "prospect",
    "opra",
    "janus",
    "stellar",
    "strass",
    "hyport-sts",
    "caspian",
    "adriatic",
    "hypo-rt-pc",
    "fast forward",
    "cre st",
    "crest",
    "quartz",
]

ORAL_KEYWORDS = [
    "standard",
    "preferred",
    "requires",
    "obtain",
    "workup",
    "dose",
    "doses",
    "gy",
    "fraction",
    "fractions",
    "boost",
    "imaging",
    "mri",
    "ct",
    "pet",
    "biopsy",
    "surgery",
    "resection",
    "radiotherapy",
    "chemotherapy",
    "brachytherapy",
    "sb rt",
    "sbrt",
    "srs",
    "observe",
    "concurrent",
    "adjuvant",
    "salvage",
    "staging",
    "constraint",
    "contraindication",
    "indicated",
    "management",
    "nodes",
    "screening",
    "follow-up",
    "follow up",
    "symptoms",
    "risk factor",
    "recommended",
]

MAIN_STEMS_ZH = [
    "關於「{section_zh}」，下列何者正確？",
    "下列哪一項符合「{section_zh}」的重點？",
    "在「{section_zh}」中，哪一項敘述正確？",
]

MAIN_STEMS_EN = [
    'Which statement is correct about "{section_en}"?',
    'Which point best matches "{section_en}"?',
    'In "{section_en}", which statement is correct?',
]

ORAL_STEMS_ZH = [
    "口試情境：關於「{section_zh}」，下列哪一項最符合標準回答？",
    "口試複習：針對「{section_zh}」，哪一項回答最恰當？",
    "口試重點：在「{section_zh}」中，哪一項敘述最應優先回答？",
]

ORAL_STEMS_EN = [
    'Oral boards: which statement is the best standard answer for "{section_en}"?',
    'Oral boards review: for "{section_en}", which answer is most appropriate?',
    'High-yield oral boards point: which statement fits "{section_en}"?',
]

SUMMARY_SECTION_MARKERS = [
    "summary",
    "take-home",
    "take home",
    "high-yield summary",
    "high yield summary",
    "clinical decision",
    "decision table",
    "memory aid",
    "one-sentence memory",
    "最終高分整理",
    "最重要",
    "總表",
    "一句話",
    "臨床決策總表",
    "高分重點",
    "take-home messages",
]


def normalize_text(text: str) -> str:
    text = html.unescape(text or "")
    replacements = {
        "\u00a0": " ",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\ufeff": "",
        "•": "-",
        "�": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"(?<=[A-Za-z0-9\u4e00-\u9fff])\?(?=[A-Za-z0-9\u4e00-\u9fff])", ": ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", " / ", fragment, flags=re.I)
    fragment = re.sub(r"</(p|li|td|th)>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return normalize_text(fragment)


def looks_trialy(text: str) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in TRIAL_MARKERS)


def looks_summary_section(text: str) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in SUMMARY_SECTION_MARKERS)


def is_good_fact(zh_text: str, en_text: str) -> bool:
    zh_text = normalize_text(zh_text)
    en_text = normalize_text(en_text)
    if not zh_text or not en_text:
        return False
    if len(zh_text) < 12 or len(en_text) < 12:
        return False
    if len(zh_text) > 320 or len(en_text) > 320:
        return False
    if zh_text.endswith(":") or en_text.endswith(":"):
        return False
    if looks_trialy(zh_text) or looks_trialy(en_text):
        return False
    bad_prefixes = (
        "objectives",
        "outline",
        "summary",
        "overview",
        "figure",
        "table",
        "part ",
        "most important",
        "high-yield",
        "high yield",
        "final high-yield",
        "final summary",
        "teaching point",
    )
    if any(en_text.lower().startswith(prefix) for prefix in bad_prefixes):
        return False
    return True


def row_to_text(row_html: str) -> str:
    cells = [strip_tags(cell) for cell in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row_html, flags=re.S)]
    cells = [cell for cell in cells if cell]
    if len(cells) < 2:
        return ""
    head, rest = cells[0], cells[1:]
    return normalize_text(f"{head}: {'; '.join(rest)}")


def extract_bilingual_sections(page_path: Path) -> list[dict]:
    page_html = page_path.read_text(encoding="utf-8")
    out = []
    for sec_html in re.findall(r'<section class="section">(.*?)</section>', page_html, flags=re.S):
        title_match = re.search(r'<h2[^>]*data-zh="([^"]*)"[^>]*data-en="([^"]*)"', sec_html, flags=re.S)
        if not title_match:
            continue

        section_zh = normalize_text(title_match.group(1))
        section_en = normalize_text(title_match.group(2))
        title_lower = f"{section_zh} {section_en}".lower()
        if any(marker in title_lower for marker in ("trial", "evidence", "study", "meta-analysis", "meta analysis")):
            continue
        zh_match = re.search(r'<div data-lang="zh">(.*?)</div>', sec_html, flags=re.S)
        en_match = re.search(r'<div data-lang="en">(.*?)</div>', sec_html, flags=re.S)
        if not zh_match or not en_match:
            continue

        zh_block = zh_match.group(1)
        en_block = en_match.group(1)
        facts = []
        seen = set()

        zh_paras = [strip_tags(item) for item in re.findall(r"<p[^>]*>(.*?)</p>", zh_block, flags=re.S)]
        en_paras = [strip_tags(item) for item in re.findall(r"<p[^>]*>(.*?)</p>", en_block, flags=re.S)]
        for zh_text, en_text in zip(zh_paras, en_paras):
            if is_good_fact(zh_text, en_text):
                key = en_text.lower()
                if key not in seen:
                    facts.append((zh_text, en_text))
                    seen.add(key)

        zh_items = [strip_tags(item) for item in re.findall(r"<li[^>]*>(.*?)</li>", zh_block, flags=re.S)]
        en_items = [strip_tags(item) for item in re.findall(r"<li[^>]*>(.*?)</li>", en_block, flags=re.S)]
        for zh_text, en_text in zip(zh_items, en_items):
            if is_good_fact(zh_text, en_text):
                key = en_text.lower()
                if key not in seen:
                    facts.append((zh_text, en_text))
                    seen.add(key)

        zh_bodies = re.findall(r"<tbody>(.*?)</tbody>", zh_block, flags=re.S)
        en_bodies = re.findall(r"<tbody>(.*?)</tbody>", en_block, flags=re.S)
        for zh_body, en_body in zip(zh_bodies, en_bodies):
            zh_rows = re.findall(r"<tr>(.*?)</tr>", zh_body, flags=re.S)
            en_rows = re.findall(r"<tr>(.*?)</tr>", en_body, flags=re.S)
            for zh_row, en_row in zip(zh_rows, en_rows):
                zh_text = row_to_text(zh_row)
                en_text = row_to_text(en_row)
                if is_good_fact(zh_text, en_text):
                    key = en_text.lower()
                    if key not in seen:
                        facts.append((zh_text, en_text))
                        seen.add(key)

        if facts:
            out.append(
                {
                    "section_zh": section_zh,
                    "section_en": section_en,
                    "facts": facts,
                }
            )
    return out


def build_candidates() -> tuple[dict, list[dict]]:
    page_map = {}
    all_candidates = []
    next_id = 0

    for cfg in PAGE_CONFIG:
        sections = extract_bilingual_sections(ROOT / cfg["file"])
        page_candidates = []
        for section in sections:
            for fact_zh, fact_en in section["facts"]:
                page_candidates.append(
                    {
                        "id": next_id,
                        "page": cfg["file"],
                        "top_zh": cfg["top_zh"],
                        "top_en": cfg["top_en"],
                        "sub_zh": cfg["sub_zh"],
                        "sub_en": cfg["sub_en"],
                        "section_zh": section["section_zh"],
                        "section_en": section["section_en"],
                        "fact_zh": fact_zh,
                        "fact_en": fact_en,
                    }
                )
                next_id += 1
        page_map[cfg["file"]] = {"config": cfg, "candidates": page_candidates}
        all_candidates.extend(page_candidates)

    return page_map, all_candidates


def pick_evenly(items: list, n: int) -> list:
    if n <= 0:
        return []
    if n >= len(items):
        return list(items)

    chosen = []
    used = set()
    span = len(items) / n
    for i in range(n):
        idx = min(len(items) - 1, int(i * span + span / 2))
        while idx in used and idx < len(items) - 1:
            idx += 1
        while idx in used and idx > 0:
            idx -= 1
        used.add(idx)
        chosen.append(items[idx])
    return chosen


def is_oral_candidate(candidate: dict) -> bool:
    text = candidate["fact_en"].lower()
    return any(keyword in text for keyword in ORAL_KEYWORDS)


def choose_oral_candidates(all_candidates: list[dict]) -> tuple[dict[str, list[dict]], set[int]]:
    chosen_ids = set()
    oral_by_subsection = {}

    for cfg in ORAL_CONFIG:
        pool = [
            cand
            for cand in all_candidates
            if cand["top_zh"] == cfg["source_top_zh"] and is_oral_candidate(cand)
        ]
        if len(pool) < cfg["quota"]:
            pool = [cand for cand in all_candidates if cand["top_zh"] == cfg["source_top_zh"]]

        selected = pick_evenly(pool, cfg["quota"])
        oral_by_subsection[cfg["sub_zh"]] = []
        for cand in selected:
            oral_cand = dict(cand)
            oral_cand["oral_sub_zh"] = cfg["sub_zh"]
            oral_cand["oral_sub_en"] = cfg["sub_en"]
            oral_by_subsection[cfg["sub_zh"]].append(oral_cand)
            chosen_ids.add(cand["id"])

    return oral_by_subsection, chosen_ids


def display_titles(candidate: dict) -> tuple[str, str]:
    return candidate["section_zh"], candidate["section_en"]


def compute_main_quotas(page_map: dict) -> dict[str, int]:
    quotas = {
        page_name: min(len(info["candidates"]), PAGE_CAP)
        for page_name, info in page_map.items()
    }
    total = sum(quotas.values())

    while total > TARGET_MAIN:
        progressed = False
        order = sorted(
            page_map.keys(),
            key=lambda name: (quotas[name], len(page_map[name]["candidates"])),
            reverse=True,
        )
        for page_name in order:
            floor = 5 if len(page_map[page_name]["candidates"]) >= 5 else len(page_map[page_name]["candidates"])
            if quotas[page_name] > floor:
                quotas[page_name] -= 1
                total -= 1
                progressed = True
                if total == TARGET_MAIN:
                    break
        if not progressed:
            break

    while total < TARGET_MAIN:
        progressed = False
        order = sorted(
            page_map.keys(),
            key=lambda name: (len(page_map[name]["candidates"]) - quotas[name], len(page_map[name]["candidates"])),
            reverse=True,
        )
        for page_name in order:
            if quotas[page_name] < len(page_map[page_name]["candidates"]):
                quotas[page_name] += 1
                total += 1
                progressed = True
                if total == TARGET_MAIN:
                    break
        if not progressed:
            break

    if total != TARGET_MAIN:
        raise RuntimeError(f"Unable to allocate {TARGET_MAIN} main questions; got {total}.")

    return quotas


def select_main_candidates(page_candidates: list[dict], quota: int) -> list[dict]:
    by_section = defaultdict(list)
    section_order = []
    for cand in page_candidates:
        if cand["section_zh"] not in by_section:
            section_order.append(cand["section_zh"])
        by_section[cand["section_zh"]].append(cand)

    section_quota = {section: 0 for section in section_order}
    total = 0
    while total < quota:
        progressed = False
        for section in section_order:
            if section_quota[section] < len(by_section[section]):
                section_quota[section] += 1
                total += 1
                progressed = True
                if total == quota:
                    break
        if not progressed:
            break

    selected = []
    for section in section_order:
        selected.extend(pick_evenly(by_section[section], section_quota[section]))
    return selected


def dedupe_candidates(candidates: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for cand in candidates:
        key = cand["fact_en"].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(cand)
    return out


def choose_distractors(
    candidate: dict,
    pool_top: dict,
    pool_global: list[dict],
    *,
    oral: bool,
) -> list[dict]:
    used_ids = {candidate["id"]}
    target_len = len(candidate["fact_en"])

    def filtered(pool: list[dict], allow_same_top: bool) -> list[dict]:
        out = []
        for cand in pool:
            if cand["id"] in used_ids:
                continue
            if cand["page"] == candidate["page"]:
                continue
            if cand["section_zh"] == candidate["section_zh"]:
                continue
            if not allow_same_top and cand["top_zh"] == candidate["top_zh"]:
                continue
            out.append(cand)
        out = dedupe_candidates(out)
        out.sort(key=lambda cand: (abs(len(cand["fact_en"]) - target_len), cand["fact_en"]))
        return out

    distractors = []
    if oral:
        pool_plan = (
            (pool_global, False),
            (pool_global, True),
        )
    else:
        pool_plan = (
            (pool_top[candidate["top_zh"]], True),
            (pool_global, False),
            (pool_global, True),
        )

    for pool, allow_same_top in pool_plan:
        if len(distractors) >= 3:
            break
        candidates = filtered(pool, allow_same_top)
        shortlist = candidates[: max(12, 3 * (3 - len(distractors)))]
        local_rng = random.Random(candidate["id"] * 1009 + len(distractors))
        local_rng.shuffle(shortlist)
        for cand in shortlist:
            if cand["id"] in used_ids:
                continue
            distractors.append(cand)
            used_ids.add(cand["id"])
            if len(distractors) == 3:
                break

    if len(distractors) < 3:
        raise RuntimeError(f"Not enough distractors for candidate {candidate['id']} / {candidate['section_en']}")

    return distractors


def build_question(candidate: dict, distractors: list[dict], oral: bool) -> dict:
    local_rng = random.Random(candidate["id"] * 7919 + (1 if oral else 0))
    option_pairs = [(candidate["fact_zh"], candidate["fact_en"])] + [
        (cand["fact_zh"], cand["fact_en"]) for cand in distractors
    ]
    local_rng.shuffle(option_pairs)
    answer_index = option_pairs.index((candidate["fact_zh"], candidate["fact_en"]))

    stem_idx = candidate["id"] % len(MAIN_STEMS_ZH)
    section_zh, section_en = display_titles(candidate)
    if oral:
        stem_zh = ORAL_STEMS_ZH[stem_idx].format(
            section_zh=section_zh,
            section_en=section_en,
        )
        stem_en = ORAL_STEMS_EN[stem_idx].format(
            section_zh=section_zh,
            section_en=section_en,
        )
        exp_zh = f"口試要點：{candidate['fact_zh']}"
        exp_en = f"Oral boards pearl: {candidate['fact_en']}"
    else:
        stem_zh = MAIN_STEMS_ZH[stem_idx].format(
            section_zh=section_zh,
            section_en=section_en,
        )
        stem_en = MAIN_STEMS_EN[stem_idx].format(
            section_zh=section_zh,
            section_en=section_en,
        )
        exp_zh = f"重點：{candidate['fact_zh']}"
        exp_en = f"Key point: {candidate['fact_en']}"

    question = {
        "type": "single",
        "stem": stem_zh,
        "stem_en": stem_en,
        "ans": LETTERS[answer_index],
        "exp": exp_zh,
        "exp_en": exp_en,
    }

    for idx, (opt_zh, opt_en) in enumerate(option_pairs):
        letter = LETTERS[idx]
        question[letter] = opt_zh
        question[f"{letter}_en"] = opt_en

    return question


def count_subjects(subjects: dict) -> int:
    total = 0
    for subsections in subjects.values():
        for questions in subsections.values():
            total += len(questions)
    return total


def main() -> None:
    page_map, all_candidates = build_candidates()

    oral_candidates, oral_ids = choose_oral_candidates(all_candidates)

    for page_name, info in page_map.items():
        info["candidates"] = [cand for cand in info["candidates"] if cand["id"] not in oral_ids]

    main_quotas = compute_main_quotas(page_map)

    selected_main = {}
    for page_name, info in page_map.items():
        selected_main[page_name] = select_main_candidates(info["candidates"], main_quotas[page_name])

    pool_page = {}
    pool_top = defaultdict(list)
    pool_global = []
    for page_name, selected in selected_main.items():
        pool_page[page_name] = selected
        pool_global.extend(selected)
        for cand in selected:
            pool_top[cand["top_zh"]].append(cand)

    oral_pool_by_top = defaultdict(list)
    oral_pool_page = defaultdict(list)
    oral_pool_global = []
    for subsection_candidates in oral_candidates.values():
        for cand in subsection_candidates:
            oral_pool_by_top[cand["top_zh"]].append(cand)
            oral_pool_page[cand["page"]].append(cand)
            oral_pool_global.append(cand)

    subjects = {
        "基礎入門": {},
        "中樞神經系統": {},
        "頭頸與胸腔": {},
        "乳癌與消化道": {},
        "泌尿與婦科": {},
        "淋巴瘤、肉瘤與皮膚": {},
        "兒童與緩和": {},
        "口試複習": {},
    }

    labels_en = {
        "基礎入門": "Foundations",
        "中樞神經系統": "Central Nervous System",
        "頭頸與胸腔": "Head, Neck & Thorax",
        "乳癌與消化道": "Breast & GI",
        "泌尿與婦科": "GU & Gyn",
        "淋巴瘤、肉瘤與皮膚": "Lymphoma, Sarcoma & Skin",
        "兒童與緩和": "Pediatrics & Palliative",
        "口試複習": "Oral Boards Review",
    }

    for cfg in PAGE_CONFIG:
        labels_en[cfg["sub_zh"]] = cfg["sub_en"]
        page_questions = []
        for cand in selected_main[cfg["file"]]:
            distractors = choose_distractors(cand, pool_top, pool_global, oral=False)
            page_questions.append(build_question(cand, distractors, oral=False))
        subjects[cfg["top_zh"]][cfg["sub_zh"]] = page_questions

    for cfg in ORAL_CONFIG:
        labels_en[cfg["sub_zh"]] = cfg["sub_en"]
        oral_questions = []
        for cand in oral_candidates[cfg["sub_zh"]]:
            distractors = choose_distractors(cand, oral_pool_by_top, oral_pool_global, oral=True)
            oral_questions.append(build_question(cand, distractors, oral=True))
        subjects["口試複習"][cfg["sub_zh"]] = oral_questions

    total_main = sum(
        len(qs)
        for top, subs in subjects.items()
        if top != "口試複習"
        for qs in subs.values()
    )
    total_oral = sum(len(qs) for qs in subjects["口試複習"].values())
    total_all = count_subjects(subjects)

    if total_main != TARGET_MAIN:
        raise RuntimeError(f"Expected {TARGET_MAIN} main questions, got {total_main}.")
    if total_oral != TARGET_ORAL:
        raise RuntimeError(f"Expected {TARGET_ORAL} oral questions, got {total_oral}.")
    if total_all != TARGET_TOTAL:
        raise RuntimeError(f"Expected {TARGET_TOTAL} total questions, got {total_all}.")

    data = {
        "radonc": {
            "label": "☢️ 放射腫瘤學互動考題",
            "label_en": "☢️ Rad Onc Interactive Quiz",
            "labels_en": labels_en,
            "subjects": subjects,
        }
    }

    OUT_PATH.write_text(
        "/* Rad Onc Interactive Quiz - bilingual question bank (talk-derived).\n"
        " * Source: tutorial topic pages built from Rad Onc Talks; old trial-only bank removed.\n"
        ' * Schema per question: type="single"|"multi"|"tf"; ans letter or list; stem/A/B/C/D/exp bilingual.\n'
        " */\nwindow.QUIZ_DATA = "
        + json.dumps(data, ensure_ascii=False, indent=1)
        + ";\n",
        encoding="utf-8",
    )

    print(f"Main questions: {total_main}")
    print(f"Oral questions: {total_oral}")
    print(f"Total questions: {total_all}")
    for top_zh, subsections in subjects.items():
        top_total = sum(len(qs) for qs in subsections.values())
        print(f"  {top_zh}: {top_total} questions across {len(subsections)} subsections")


if __name__ == "__main__":
    main()
