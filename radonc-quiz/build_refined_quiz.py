from __future__ import annotations

import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC_PATH = ROOT / "data_original_backup.js"
OUT_PATH = ROOT / "data_refined.js"
STATS_PATH = ROOT / "refinement_stats.json"
LETTERS = "ABCD"
RNG = random.Random(20260710)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ORAL_ABBR = {
    "基礎口試": "FDN",
    "中樞神經口試": "CNS",
    "頭頸與胸腔口試": "HNT",
    "乳癌與消化道口試": "BGI",
    "泌尿與婦科口試": "GUG",
    "淋巴瘤肉瘤皮膚口試": "LSS",
    "兒童與緩和口試": "PAP",
}

GENERIC_LABELS_EN = {
    "results",
    "interpretation",
    "methods",
    "randomization",
    "summary",
    "take-home messages",
    "clinical decision summary table",
    "final high-yield summary",
    "most important take-home messages",
}

GENERIC_LABELS_ZH = {
    "結果",
    "解讀",
    "方法",
    "隨機分派",
    "總結",
    "最終高分整理",
    "臨床決策總表",
    "最重要 take-home messages",
}

TOKEN_GROUPS = [
    ([r"\bipsilateral\b", r"\b同側\b"], [("contralateral", "對側"), ("bilateral", "雙側")], "laterality mismatch"),
    ([r"\bcontralateral\b", r"\b對側\b"], [("ipsilateral", "同側"), ("bilateral", "雙側")], "laterality mismatch"),
    ([r"\bperipheral\b", r"\b周邊\b"], [("central", "中央"), ("ultracentral", "超中央")], "tumor location mismatch"),
    ([r"\bcentral\b", r"\b中央\b"], [("peripheral", "周邊"), ("ultracentral", "超中央")], "tumor location mismatch"),
    ([r"\bultracentral\b", r"\b超中央\b"], [("central", "中央"), ("peripheral", "周邊")], "tumor location mismatch"),
    ([r"\bpositive\b", r"\b陽性\b"], [("negative", "陰性")], "biomarker polarity mismatch"),
    ([r"\bnegative\b", r"\b陰性\b"], [("positive", "陽性")], "biomarker polarity mismatch"),
    ([r"\bmethylated\b", r"\b甲基化\b"], [("unmethylated", "未甲基化")], "molecular marker mismatch"),
    ([r"\bunmethylated\b", r"\b未甲基化\b"], [("methylated", "甲基化")], "molecular marker mismatch"),
    ([r"\bIDH-mut\b", r"\bIDH 突變\b"], [("IDH-wildtype", "IDH 野生型")], "molecular subtype mismatch"),
    ([r"\bIDH-wildtype\b", r"\bIDH 野生型\b"], [("IDH-mut", "IDH 突變")], "molecular subtype mismatch"),
    ([r"\bhigh-risk\b", r"\b高風險\b"], [("low-risk", "低風險"), ("intermediate-risk", "中風險")], "risk-group mismatch"),
    ([r"\blow-risk\b", r"\b低風險\b"], [("high-risk", "高風險"), ("intermediate-risk", "中風險")], "risk-group mismatch"),
    ([r"\bintermediate-risk\b", r"\b中風險\b"], [("high-risk", "高風險"), ("low-risk", "低風險")], "risk-group mismatch"),
    ([r"\bfavorable\b"], [("unfavorable", "unfavorable")], "risk-group mismatch"),
    ([r"\bunfavorable\b"], [("favorable", "favorable")], "risk-group mismatch"),
    ([r"\blimited-stage\b"], [("extensive-stage", "extensive-stage")], "stage-category mismatch"),
    ([r"\bextensive-stage\b"], [("limited-stage", "limited-stage")], "stage-category mismatch"),
    ([r"\bcomplete response\b", r"\b完全緩解\b", r"\bCR\b"], [("partial response", "部分緩解"), ("stable disease", "疾病穩定")], "response-category mismatch"),
    ([r"\bpartial response\b", r"\b部分緩解\b", r"\bPR\b"], [("complete response", "完全緩解"), ("progressive disease", "疾病進展")], "response-category mismatch"),
    ([r"\badjuvant\b", r"\b輔助\b"], [("neoadjuvant", "新輔助"), ("salvage", "挽救性")], "treatment-setting mismatch"),
    ([r"\bneoadjuvant\b", r"\b新輔助\b"], [("adjuvant", "輔助"), ("definitive", "根治性")], "treatment-setting mismatch"),
    ([r"\bdefinitive\b", r"\b根治性\b"], [("adjuvant", "輔助"), ("palliative", "緩和")], "treatment-setting mismatch"),
    ([r"\bsalvage\b", r"\b挽救性\b"], [("adjuvant", "輔助"), ("palliative", "緩和")], "treatment-setting mismatch"),
    ([r"\bpalliative\b", r"\b緩和\b"], [("definitive", "根治性"), ("adjuvant", "輔助")], "treatment-intent mismatch"),
    ([r"\bpreferred\b"], [("not routinely preferred", "不建議作為常規首選"), ("reserved for selected patients", "僅保留給特定病人")], "recommendation mismatch"),
    ([r"\brecommended\b"], [("not routinely recommended", "不建議常規使用"), ("reserved for relapse", "通常保留於復發時")], "recommendation mismatch"),
    ([r"\brequires\b"], [("does not require", "不需要"), ("should avoid", "應避免")], "requirement mismatch"),
    ([r"\bcan be considered\b"], [("is mandatory", "屬於必要治療"), ("has no role", "通常沒有角色")], "recommendation mismatch"),
    ([r"\bmore common\b", r"\b較常見\b"], [("less common", "較少見")], "frequency mismatch"),
    ([r"\bmost common\b", r"\b最常見\b"], [("least common", "最少見"), ("uncommon", "不常見")], "frequency mismatch"),
    ([r"\baggressive\b", r"\b侵襲性高\b"], [("indolent", "惰性"), ("less aggressive", "侵襲性較低")], "biology mismatch"),
    ([r"\bobservation\b", r"\b觀察\b"], [("routine radiotherapy", "常規放射治療"), ("immediate surgery", "立即手術")], "management mismatch"),
    ([r"\bsurgery alone\b", r"\b單獨手術\b"], [("routine postoperative radiotherapy", "常規術後放射治療"), ("systemic therapy alone", "單獨全身治療")], "management mismatch"),
]

COMPARISON_RULES = [
    (r"\bimproves OS\b", "improves OS", [("improves local control without OS benefit", "僅改善局部控制而無整體存活效益"), ("does not improve OS", "不改善整體存活")], "endpoint interpretation mismatch"),
    (r"\bnon-inferior\b", "non-inferior", [("inferior", "劣於標準治療"), ("superior", "優於標準治療")], "trial-interpretation mismatch"),
    (r"\bsuperior\b", "superior", [("non-inferior", "非劣性"), ("inferior", "劣於標準治療")], "trial-interpretation mismatch"),
    (r"\bno OS benefit\b", "no OS benefit", [("clear OS benefit", "有明確整體存活效益"), ("inferior overall survival", "整體存活較差")], "trial-interpretation mismatch"),
]

ACRONYM_EXPANSIONS = {
    "IGRT": [("Intensity-Guided RT", "強度導引放射治療"), ("Image-Gated RT", "影像閘控放射治療"), ("Inverse-Geometry RT", "反向幾何放射治療")],
    "IMRT": [("Image-Modulated RT", "影像調控放射治療"), ("Intensity-Matched RT", "強度匹配放射治療"), ("Integrated-Modality RT", "整合模式放射治療")],
    "VMAT": [("Volumetric-Modulated Arc Therapy", "容積調控弧形治療"), ("Variable-Margin Arc Therapy", "可變邊界弧形治療"), ("Voxel-Matched Arc Therapy", "體素匹配弧形治療")],
    "CTV": [("Central Target Volume", "中央靶體積"), ("Complete Tumor Volume", "完整腫瘤體積"), ("Critical Treatment Volume", "關鍵治療體積")],
    "PTV": [("Planning Treatment Volume", "治療計畫體積"), ("Primary Tumor Volume", "原發腫瘤體積"), ("Protected Target Volume", "保護靶體積")],
    "OAR": [("Optimized Anatomical Region", "最佳化解剖區"), ("Objective At-Risk Region", "目標風險區"), ("Operational Assessment Region", "作業評估區")],
    "SRS": [("Stereotactic Radiation Schedule", "立體定位放射時程"), ("Single-Region Stereotaxis", "單區立體定位"), ("Segmented Radiosurgical Series", "分段放射手術序列")],
    "SBRT": [("Stereotactic Boost RT", "立體定位加強放射治療"), ("Site-Based RT", "部位導向放射治療"), ("Single-Beam RT", "單束放射治療")],
    "BED": [("Biologic Equivalent Dose", "生物等效劑量"), ("Beam Energy Density", "射束能量密度"), ("Boundary Effective Dose", "邊界有效劑量")],
    "EQD2": [("Equivalent Quality Dose 2", "等效品質劑量 2"), ("Equalized Dose 2", "均衡劑量 2"), ("Equivalent Dose to 2-cm depth", "等效 2 公分深度劑量")],
}


def load_data(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return json.loads(text.split("window.QUIZ_DATA = ", 1)[1].rsplit(";", 1)[0])


def save_data(path: Path, data: dict) -> None:
    path.write_text(
        "/* Rad Onc Interactive Quiz - refined bilingual question bank.\n"
        " * Source: rebuilt from the preserved original database with refined stems, distractors, and explanations.\n"
        " * Schema per question: type=\"single\"|\"multi\"|\"tf\"; ans letter or list; stem/A/B/C/D/exp bilingual.\n"
        " */\nwindow.QUIZ_DATA = "
        + json.dumps(data, ensure_ascii=False, indent=1)
        + ";\n",
        encoding="utf-8",
    )


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("：", ":")).strip()


def split_fact(zh: str, en: str) -> tuple[str | None, str, str | None, str]:
    for sep in (":", "："):
        if sep in en:
            en_label, en_body = [part.strip() for part in en.split(sep, 1)]
            zh_parts = zh.split(sep, 1) if sep in zh else zh.split("：", 1) if "：" in zh else None
            if zh_parts:
                zh_label, zh_body = [part.strip() for part in zh_parts]
            else:
                zh_label, zh_body = None, zh.strip()
            if 2 <= len(en_label) <= 80 and len(en_body) >= 10:
                return zh_label, zh_body, en_label, en_body
    m = re.match(r"^([A-Z][A-Z0-9+/\-]{1,12})\s+(.+)$", en)
    if m and len(m.group(2)) >= 8:
        label_en = m.group(1).strip()
        body_en = m.group(2).strip()
        label_zh = label_en if zh.startswith(label_en) else None
        body_zh = zh[len(label_en):].strip(" -：:") if label_zh else zh
        return label_zh, body_zh, label_en, body_en
    return None, zh.strip(), None, en.strip()


def is_generic_label(label_zh: str | None, label_en: str | None) -> bool:
    if not label_en and not label_zh:
        return True
    if label_en and normalize_space(label_en).lower() in GENERIC_LABELS_EN:
        return True
    if label_zh and normalize_space(label_zh) in GENERIC_LABELS_ZH:
        return True
    return False


def classify_fact(label_en: str | None, body_en: str, sub_en: str) -> str:
    text = f"{label_en or ''} {body_en}".lower()
    if re.search(r"\b\d+(\.\d+)?\s*gy\b|\bfx\b|\bfractions?\b|\b\d+\s*次\b", text):
        return "dose"
    if re.search(r"\bv\d+\b|\bdmax\b|\bdmean\b|\bconstraint\b|\boar\b|\brisk\b", text):
        return "constraint"
    if re.search(r"\bphase\b|\btrial\b|\bos\b|\bpfs\b|\bnon-inferior\b|\bsuperior\b|\binferior\b", text):
        return "trial"
    if re.search(r"\bstage\b|\bajcc\b|\bfigo\b|\btnm\b|\bt[0-4][a-c]?\b|\bn[0-3]\b|\bm1[a-c]?\b|\bgg\d\b|\bdeauville\b", text):
        return "staging"
    if re.search(r"\bmeans?\b|\bstands for\b|\bclinical target volume\b|\bplanning target volume\b|\bimage-guided\b|\bmodality\b|acronym", text):
        return "definition"
    if re.search(r"\brequires\b|\bpreferred\b|\brecommended\b|\bcan be considered\b|\bfavors\b|\bindicated\b|\bstandard\b|\bobservation\b", text):
        return "management"
    if re.search(r"\bmarker\b|\bmutation\b|\bhistology\b|\bmost common\b|\bassociated\b|\bpositive\b|\bnegative\b|\bcd\d+\b|\bp16\b|\bmgmt\b|\bidh\b", text):
        return "association"
    if re.search(r"\blevel\b|\bborder\b|\bstation\b|\bdrainage\b|\banatomy\b|\bcompartment\b|\blayer\b|\btectum\b", text):
        return "anatomy"
    if "physics" in sub_en.lower() or "radiation biology" in sub_en.lower():
        return "foundation"
    return "general"


def extract_numbers(text: str, unit: str) -> list[str]:
    return re.findall(rf"\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?\s*{unit}", text, flags=re.I)


def mutate_with_replacement(text: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, text, count=1, flags=re.I)


def make_numeric_variants(body_zh: str, body_en: str, kind: str) -> list[tuple[str, str, str]]:
    variants: list[tuple[str, str, str]] = []

    dose_matches_en = extract_numbers(body_en, "Gy")
    dose_matches_zh = extract_numbers(body_zh, "Gy")
    if dose_matches_en:
        match_en = dose_matches_en[0]
        base = float(re.findall(r"\d+(?:\.\d+)?", match_en)[0])
        for delta in (-10, -5, 5, 10):
            new_num = max(1, round(base + delta, 1))
            replacement = re.sub(r"\d+(?:\.\d+)?", f"{new_num:g}", match_en, count=1)
            zh_replacement = re.sub(r"\d+(?:\.\d+)?", f"{new_num:g}", dose_matches_zh[0], count=1) if dose_matches_zh else replacement
            variants.append(
                (
                    body_zh.replace(dose_matches_zh[0], zh_replacement, 1) if dose_matches_zh else body_zh.replace(match_en, replacement, 1),
                    body_en.replace(match_en, replacement, 1),
                    "dose mismatch",
                )
            )

    fx_match_en = re.search(r"(\d+)\s*(?:fx|fractions?)", body_en, flags=re.I)
    fx_match_zh = re.search(r"(\d+)\s*(?:Fx|fx|次)", body_zh, flags=re.I)
    if fx_match_en:
        base = int(fx_match_en.group(1))
        for delta in (-5, -2, 2, 5):
            new_val = max(1, base + delta)
            variants.append(
                (
                    re.sub(r"(\d+)\s*(?:Fx|fx|次)", f"{new_val} Fx", body_zh, count=1),
                    re.sub(r"(\d+)\s*(?:fx|fractions?)", f"{new_val} fractions", body_en, count=1, flags=re.I),
                    "fractionation mismatch",
                )
            )

    pct_match_en = re.search(r"(\d+(?:\.\d+)?)\s*%", body_en)
    pct_match_zh = re.search(r"(\d+(?:\.\d+)?)\s*%", body_zh)
    if pct_match_en:
        base = float(pct_match_en.group(1))
        for delta in (-15, -10, 10, 15):
            new_val = max(0, min(100, round(base + delta, 1)))
            variants.append(
                (
                    re.sub(r"(\d+(?:\.\d+)?)\s*%", f"{new_val:g}%", body_zh, count=1),
                    re.sub(r"(\d+(?:\.\d+)?)\s*%", f"{new_val:g}%", body_en, count=1),
                    "numeric threshold mismatch",
                )
            )

    cm_match_en = re.search(r"(\d+(?:\.\d+)?)\s*cm", body_en, flags=re.I)
    if cm_match_en:
        base = float(cm_match_en.group(1))
        for delta in (-1, 1, 2):
            new_val = max(0.5, round(base + delta, 1))
            variants.append(
                (
                    re.sub(r"(\d+(?:\.\d+)?)\s*cm", f"{new_val:g} cm", body_zh, count=1, flags=re.I),
                    re.sub(r"(\d+(?:\.\d+)?)\s*cm", f"{new_val:g} cm", body_en, count=1, flags=re.I),
                    "size-threshold mismatch",
                )
            )

    return variants


def make_token_variants(body_zh: str, body_en: str) -> list[tuple[str, str, str]]:
    variants: list[tuple[str, str, str]] = []
    for patterns, replacements, reason in TOKEN_GROUPS:
        if any(re.search(pattern, body_en, flags=re.I) or re.search(pattern, body_zh, flags=re.I) for pattern in patterns):
            for en_alt, zh_alt in replacements:
                new_en = body_en
                new_zh = body_zh
                for pattern in patterns:
                    new_en = re.sub(pattern, en_alt, new_en, count=1, flags=re.I)
                    new_zh = re.sub(pattern, zh_alt, new_zh, count=1, flags=re.I)
                if new_en != body_en or new_zh != body_zh:
                    variants.append((new_zh, new_en, reason))
    return variants


def make_comparison_variants(body_zh: str, body_en: str) -> list[tuple[str, str, str]]:
    variants: list[tuple[str, str, str]] = []
    for pattern, target, replacements, reason in COMPARISON_RULES:
        if re.search(pattern, body_en, flags=re.I):
            for en_alt, zh_alt in replacements:
                new_en = re.sub(pattern, en_alt, body_en, count=1, flags=re.I)
                new_zh = body_zh.replace(target, zh_alt) if target in body_zh else body_zh + "（" + zh_alt + "）"
                variants.append((new_zh, new_en, reason))
    return variants


def make_acronym_variants(label_zh: str | None, body_zh: str, label_en: str | None, body_en: str) -> list[tuple[str, str, str]]:
    variants: list[tuple[str, str, str]] = []
    if label_en and label_en in ACRONYM_EXPANSIONS:
        for wrong_en, wrong_zh in ACRONYM_EXPANSIONS[label_en]:
            variants.append((wrong_zh, wrong_en, "acronym-expansion mismatch"))
    return variants


def choose_fallback_options(item: dict, pool: list[dict]) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for other in pool:
        if other["id"] == item["id"]:
            continue
        out.append((other["option_zh"], other["option_en"], "same-subsection alternative fact"))
    out.sort(key=lambda opt: abs(len(opt[1]) - len(item["option_en"])))
    return out


def build_distractors(item: dict, pools_by_kind: dict[tuple[str, str], list[dict]]) -> tuple[list[tuple[str, str, str]], bool]:
    variants: list[tuple[str, str, str]] = []
    seen_en = {normalize_space(item["option_en"]).lower()}
    seen_zh = {normalize_space(item["option_zh"])}
    generators = [
        make_numeric_variants(item["option_zh"], item["option_en"], item["kind"]),
        make_token_variants(item["option_zh"], item["option_en"]),
        make_comparison_variants(item["option_zh"], item["option_en"]),
        make_acronym_variants(item["label_zh"], item["option_zh"], item["label_en"], item["option_en"]),
    ]

    for bucket in generators:
        for zh_text, en_text, reason in bucket:
            key_en = normalize_space(en_text).lower()
            key_zh = normalize_space(zh_text)
            if key_en in seen_en or key_zh in seen_zh:
                continue
            if key_en == normalize_space(item["option_en"]).lower() or key_zh == normalize_space(item["option_zh"]):
                continue
            if len(en_text) < 8 or len(zh_text) < 4:
                continue
            seen_en.add(key_en)
            seen_zh.add(key_zh)
            variants.append((key_zh, normalize_space(en_text), reason))

    used_fallback = False
    if len(variants) < 3:
        fallback_pool = pools_by_kind.get((item["sub_zh"], item["kind"]), [])
        for zh_text, en_text, reason in choose_fallback_options(item, fallback_pool):
            key_en = normalize_space(en_text).lower()
            key_zh = normalize_space(zh_text)
            if key_en in seen_en or key_zh in seen_zh:
                continue
            seen_en.add(key_en)
            seen_zh.add(key_zh)
            variants.append((key_zh, normalize_space(en_text), reason))
            used_fallback = True
            if len(variants) >= 3:
                break

    if len(variants) < 3:
        generic_pool = pools_by_kind.get((item["sub_zh"], "general"), [])
        for zh_text, en_text, reason in choose_fallback_options(item, generic_pool):
            key_en = normalize_space(en_text).lower()
            key_zh = normalize_space(zh_text)
            if key_en in seen_en or key_zh in seen_zh:
                continue
            seen_en.add(key_en)
            seen_zh.add(key_zh)
            variants.append((key_zh, normalize_space(en_text), reason))
            used_fallback = True
            if len(variants) >= 3:
                break

    variants.sort(key=lambda opt: abs(len(opt[1]) - len(item["option_en"])))
    return variants[:3], used_fallback


def make_stem(item: dict, oral_index: int | None = None) -> tuple[str, str]:
    label_zh = item["label_zh"] or item["section_zh"]
    label_en = item["label_en"] or item["section_en"]
    if is_generic_label(item["label_zh"], item["label_en"]):
        label_zh = item["section_zh"]
        label_en = item["section_en"]

    kind = item["kind"]
    if kind in {"dose", "constraint"}:
        stem_zh = f"關於「{label_zh}」，下列哪一項劑量／分割最合適？"
        stem_en = f'For "{label_en}", which dose/fractionation is most appropriate?'
    elif kind == "staging":
        stem_zh = f"關於「{label_zh}」，下列何者最符合分期或風險分層原則？"
        stem_en = f'Which statement best reflects the staging or risk-stratification principle for "{label_en}"?'
    elif kind == "definition":
        stem_zh = f"下列何者最能正確描述「{label_zh}」？"
        stem_en = f'Which description of "{label_en}" is most accurate?'
    elif kind == "management":
        stem_zh = f"在「{label_zh}」的臨床情境中，下列何者最適當？"
        stem_en = f'In the clinical setting of "{label_en}", which management choice is most appropriate?'
    elif kind == "trial":
        stem_zh = f"下列哪一項最符合「{label_zh}」的臨床結論？"
        stem_en = f'Which conclusion is best supported for "{label_en}"?'
    elif kind == "association":
        stem_zh = f"關於「{label_zh}」，下列敘述何者最正確？"
        stem_en = f'Which statement about "{label_en}" is most accurate?'
    elif kind == "anatomy":
        stem_zh = f"下列何者最能正確描述「{label_zh}」的解剖或邊界？"
        stem_en = f'Which description of the anatomy or boundary for "{label_en}" is most accurate?'
    else:
        stem_zh = f"關於「{label_zh}」，下列何者最正確？"
        stem_en = f'Which statement regarding "{label_en}" is most accurate?'

    if oral_index is not None:
        abbr = ORAL_ABBR.get(item["sub_zh"], "ORB")
        stem_zh = f"案例 {abbr}-{oral_index:02d}：{stem_zh}"
        stem_en = f"Case {abbr}-{oral_index:02d}: {stem_en}"

    return stem_zh, stem_en


def build_explanation(item: dict, distractors: list[tuple[str, str, str]]) -> tuple[str, str]:
    label_zh = item["label_zh"] or item["section_zh"]
    label_en = item["label_en"] or item["section_en"]
    reason_labels = []
    for _, _, reason in distractors:
        if reason not in reason_labels:
            reason_labels.append(reason)
    reason_zh_map = {
        "dose mismatch": "其他選項多半把劑量範圍或總劑量改成不適用於此情境的數值。",
        "fractionation mismatch": "其他選項混淆了總劑量與分割次數，因此不符合此治療情境。",
        "numeric threshold mismatch": "其他選項改動了關鍵數值門檻，會導致病人選擇或風險判讀錯誤。",
        "size-threshold mismatch": "其他選項改動了尺寸門檻，會改變臨床分層或適應症。",
        "laterality mismatch": "其他選項混淆了同側、對側或雙側的解剖定義。",
        "tumor location mismatch": "其他選項把周邊、中央或超中央病灶的策略混為一談。",
        "biomarker polarity mismatch": "其他選項將陽性與陰性的生物標記意義顛倒。",
        "molecular marker mismatch": "其他選項混淆了分子亞型或分子標記狀態。",
        "risk-group mismatch": "其他選項把不同風險層級的建議互相套用。",
        "response-category mismatch": "其他選項將完全緩解、部分緩解或疾病進展的策略混用。",
        "treatment-setting mismatch": "其他選項把根治、術前、術後或挽救治療的原則混在一起。",
        "treatment-intent mismatch": "其他選項混淆了根治性與緩和性治療目標。",
        "recommendation mismatch": "其他選項把『可考慮』、『標準』與『不建議』等建議強度混淆。",
        "frequency mismatch": "其他選項顛倒了常見與少見、或預後高低的描述。",
        "biology mismatch": "其他選項混淆了腫瘤生物學或臨床行為。",
        "management mismatch": "其他選項雖是其他情境可能出現的策略，但不適合本題指定的病人或治療目的。",
        "endpoint interpretation mismatch": "其他選項誤把局部控制、無進展存活與整體存活的結論互相取代。",
        "trial-interpretation mismatch": "其他選項扭曲了試驗的主要結論或其臨床外推。",
        "acronym-expansion mismatch": "其他選項是常見的縮寫誤讀，並非正確術語。",
        "same-subsection alternative fact": "其他選項本身可能是同章節的另一個真實重點，但不是本題所問的核心概念。",
    }
    reason_en_map = {
        "dose mismatch": "The distractors mainly alter the dose range or total dose to values that do not fit this setting.",
        "fractionation mismatch": "The distractors confuse total dose with fraction number, so they do not match the intended regimen.",
        "numeric threshold mismatch": "The distractors change the key numeric threshold and would misclassify risk or patient selection.",
        "size-threshold mismatch": "The distractors change the size cut-off and therefore alter staging or eligibility.",
        "laterality mismatch": "The distractors confuse ipsilateral, contralateral, and bilateral anatomy.",
        "tumor location mismatch": "The distractors mix up peripheral, central, and ultracentral disease, which are managed differently.",
        "biomarker polarity mismatch": "The distractors reverse the meaning of a positive versus negative biomarker result.",
        "molecular marker mismatch": "The distractors confuse the relevant molecular subtype or marker state.",
        "risk-group mismatch": "The distractors apply recommendations from a different risk group.",
        "response-category mismatch": "The distractors mix complete response, partial response, and progression-based strategies.",
        "treatment-setting mismatch": "The distractors confuse definitive, preoperative, postoperative, or salvage indications.",
        "treatment-intent mismatch": "The distractors mix curative and palliative intents.",
        "recommendation mismatch": "The distractors blur the distinction between standard, optional, and not-routinely-recommended care.",
        "frequency mismatch": "The distractors reverse common versus uncommon patterns or expected prognosis.",
        "biology mismatch": "The distractors misstate the underlying biology or clinical behavior.",
        "management mismatch": "The distractors may be real strategies in other scenarios, but they are not appropriate for the patient or intent stated here.",
        "endpoint interpretation mismatch": "The distractors swap local control, progression-free survival, and overall survival conclusions.",
        "trial-interpretation mismatch": "The distractors distort the main trial conclusion or its practical implication.",
        "acronym-expansion mismatch": "The distractors represent common but incorrect acronym expansions.",
        "same-subsection alternative fact": "The distractors may be true statements from the same chapter, but they do not answer the specific concept being asked.",
    }
    reason_zh = " ".join(reason_zh_map[r] for r in reason_labels[:2] if r in reason_zh_map)
    reason_en = " ".join(reason_en_map[r] for r in reason_labels[:2] if r in reason_en_map)
    exp_zh = (
        f"正確答案是「{item['option_zh']}」。本題考的是「{label_zh}」的核心原則："
        f"{item['option_zh']}。{reason_zh or '其他選項不是把關鍵條件、時序或數值改錯，就是把其他情境的真實事實誤套用到本題。'}"
    )
    exp_en = (
        f'The best answer is "{item["option_en"]}". The key teaching point for "{label_en}" is: '
        f'{item["option_en"]}. {reason_en or "The distractors either alter the critical condition, timing, or numeric threshold, or they import a true statement from a different clinical setting."}'
    )
    return exp_zh, exp_en


def rebalance_answer(order_seed: int) -> list[str]:
    letters = list(LETTERS)
    RNG.shuffle(letters)
    local = random.Random(order_seed)
    local.shuffle(letters)
    return letters


def main() -> None:
    src = load_data(SRC_PATH)
    subjects = src["radonc"]["subjects"]

    analyzed_items = []
    item_lookup = {}
    for top_zh, subsections in subjects.items():
        for sub_zh, questions in subsections.items():
            for idx, question in enumerate(questions, start=1):
                ans = question["ans"]
                correct_zh = question[ans]
                correct_en = question[f"{ans}_en"]
                label_zh, body_zh, label_en, body_en = split_fact(correct_zh, correct_en)
                option_zh = body_zh if label_en and not is_generic_label(label_zh, label_en) else correct_zh
                option_en = body_en if label_en and not is_generic_label(label_zh, label_en) else correct_en
                item = {
                    "id": len(analyzed_items),
                    "top_zh": top_zh,
                    "sub_zh": sub_zh,
                    "section_zh": label_zh or sub_zh,
                    "section_en": label_en or src["radonc"]["labels_en"].get(sub_zh, sub_zh),
                    "label_zh": label_zh,
                    "label_en": label_en,
                    "option_zh": normalize_space(option_zh),
                    "option_en": normalize_space(option_en),
                    "correct_zh": correct_zh,
                    "correct_en": correct_en,
                    "kind": classify_fact(label_en, option_en, src["radonc"]["labels_en"].get(sub_zh, sub_zh)),
                    "oral": top_zh == "口試複習",
                }
                analyzed_items.append(item)
                item_lookup[(top_zh, sub_zh, idx)] = item

    pools_by_kind: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for item in analyzed_items:
        pools_by_kind[(item["sub_zh"], item["kind"])].append(item)
        pools_by_kind[(item["sub_zh"], "general")].append(item)

    refined_subjects = {}
    stats = {
        "original_question_count": len(analyzed_items),
        "final_question_count": 0,
        "substantially_rewritten": 0,
        "fallback_distractor_questions": 0,
        "rule_generated_distractor_questions": 0,
        "oral_case_ids_added": 0,
        "answer_distribution": Counter(),
        "question_count_by_section": {},
    }

    for top_zh, subsections in subjects.items():
        refined_subjects[top_zh] = {}
        oral_counter = 0
        for sub_zh, questions in subsections.items():
            refined_questions = []
            for idx, _ in enumerate(questions, start=1):
                item = item_lookup[(top_zh, sub_zh, idx)]
                if item["oral"]:
                    oral_counter += 1
                    stats["oral_case_ids_added"] += 1
                distractors, used_fallback = build_distractors(item, pools_by_kind)
                if used_fallback:
                    stats["fallback_distractor_questions"] += 1
                else:
                    stats["rule_generated_distractor_questions"] += 1

                stem_zh, stem_en = make_stem(item, oral_counter if item["oral"] else None)
                exp_zh, exp_en = build_explanation(item, distractors)

                answer_letters = rebalance_answer(item["id"])
                option_bank = [(item["option_zh"], item["option_en"], True)] + [
                    (zh_text, en_text, False) for zh_text, en_text, _ in distractors
                ]
                local = random.Random(item["id"] * 31 + 7)
                local.shuffle(option_bank)

                question = {
                    "type": "single",
                    "stem": stem_zh,
                    "stem_en": stem_en,
                    "exp": exp_zh,
                    "exp_en": exp_en,
                }

                for letter, (opt_zh, opt_en, is_correct) in zip(LETTERS, option_bank):
                    question[letter] = opt_zh
                    question[f"{letter}_en"] = opt_en
                    if is_correct:
                        question["ans"] = letter
                        stats["answer_distribution"][letter] += 1

                refined_questions.append(question)
                stats["substantially_rewritten"] += 1

            refined_subjects[top_zh][sub_zh] = refined_questions
            stats["question_count_by_section"][sub_zh] = len(refined_questions)

    refined = {
        "radonc": {
            "label": src["radonc"]["label"],
            "label_en": src["radonc"]["label_en"],
            "labels_en": src["radonc"]["labels_en"],
            "subjects": refined_subjects,
        }
    }

    stats["final_question_count"] = sum(
        len(qs) for top in refined_subjects.values() for qs in top.values()
    )

    save_data(OUT_PATH, refined)
    STATS_PATH.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_PATH.name} with {stats['final_question_count']} questions.")
    print(f"Fallback distractor questions: {stats['fallback_distractor_questions']}")


if __name__ == "__main__":
    main()
