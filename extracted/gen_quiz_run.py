# -*- coding: utf-8 -*-
"""Orchestrator: assembles the 1000-Q bilingual quiz data.js."""
import json, os, random, re
random.seed(42)

# Load QBANK by importing both parts
from gen_quiz import QBANK  # base 4 sections
import gen_quiz_part2       # extends QBANK
from ronc_translate import translate_en_to_zh

ROOT = r"C:\Users\ydai\Desktop\RT2\radonc-tutorial"
TRIALS = json.load(open(os.path.join(ROOT, "data", "trials.json"), encoding="utf-8"))

def to_q(t):
    kind = t[0]
    if kind == "tf":
        return dict(type="tf", stem=t[1], stem_en=t[2], ans=t[4], exp=t[5], exp_en=t[6])
    zh_stem, en_stem, opts, ans, zh_exp, en_exp = t[1], t[2], t[3], t[4], t[5], t[6]
    q = dict(type=kind, stem=zh_stem, stem_en=en_stem, ans=ans, exp=zh_exp, exp_en=en_exp)
    for i,(zh,en) in enumerate(opts):
        letter = chr(ord('A')+i)
        q[letter] = zh
        q[letter+'_en'] = en
    return q

def clean(s):
    return (s or '').strip()

def trim(s, n=420):
    """Trim at word boundary. Never cut mid-word.
    Backtracks up to 60 chars to find a space/punct so we don't split words.
    """
    s = (s or '').strip()
    if len(s) <= n: return s
    cut = s[:n]
    # find rightmost whitespace or sentence-punct within the tail window
    tail = cut[-60:]
    best = -1
    for ch in ' \t\n.;,)':
        idx = tail.rfind(ch)
        if idx > best: best = idx
    if best >= 0:
        cut = cut[:len(cut)-60+best]
    return cut.rstrip(' ,;:.-') + '…'

def trial_qs_for_site(site, trials, seed_offset=0):
    """Generate Qs from trials of one site — options rendered in both EN (source) and ZH (term-substituted)."""
    rng = random.Random(hash(site) + seed_offset)
    qs = []

    good = [t for t in trials if t.get("trial") and (t.get("interpretation") or t.get("results")) and t.get("patients")]
    rng.shuffle(good)

    # Interpretation-based
    interp_pool = [t for t in good if t.get("interpretation")]
    interp_en_pool = [trim(x["interpretation"]) for x in interp_pool if x.get("interpretation")]

    for t in interp_pool:
        name = clean(t["trial"]).replace("⭐","").strip()
        pop_en = trim(t["patients"], 140)
        pop_zh = translate_en_to_zh(pop_en)
        interp_en = trim(t["interpretation"])
        interp_zh = translate_en_to_zh(interp_en)

        # Distractors — sample 3 other interpretations
        distractors_en_all = [x for x in interp_en_pool if x != interp_en]
        distractors_en = rng.sample(distractors_en_all, min(3, len(distractors_en_all)))
        while len(distractors_en) < 3:
            distractors_en.append("No conclusive difference between arms in the primary endpoint.")

        # Build EN and ZH option lists in sync
        options_en = distractors_en + [interp_en]
        # Shuffle EN and ZH the same way so the answer letter stays consistent
        order = list(range(len(options_en)))
        rng.shuffle(order)
        options_en = [options_en[i] for i in order]
        options_zh = [translate_en_to_zh(opt) for opt in options_en]
        ans_idx = options_en.index(interp_en)
        ans_letter = chr(ord('A') + ans_idx)

        q = dict(
            type="single",
            stem=f"「{name}」試驗（{pop_zh}）的關鍵發現為何？",
            stem_en=f'In the "{name}" trial ({pop_en}), what was the key finding?',
            ans=ans_letter,
            exp=f"「{name}」的臨床詮釋：{interp_zh}",
            exp_en=f'Clinical interpretation of "{name}": {interp_en}',
        )
        for i, (en, zh) in enumerate(zip(options_en, options_zh)):
            L = chr(ord('A')+i)
            q[L] = zh          # Chinese mode
            q[L+'_en'] = en    # English mode
        qs.append(q)

    # Population-based
    pop_pool = good[:]
    rng.shuffle(pop_pool)
    pop_en_pool = [trim(x["patients"], 180) for x in pop_pool if x.get("patients")]

    for t in pop_pool[:min(30, len(pop_pool))]:
        name = clean(t["trial"]).replace("⭐","").strip()
        pop_en = trim(t["patients"], 180)
        pop_zh = translate_en_to_zh(pop_en)

        distractors_en_all = [x for x in pop_en_pool if x != pop_en]
        distractors_en = rng.sample(distractors_en_all, min(3, len(distractors_en_all)))
        while len(distractors_en) < 3:
            distractors_en.append("Healthy volunteers with no cancer.")

        options_en = distractors_en + [pop_en]
        order = list(range(len(options_en)))
        rng.shuffle(order)
        options_en = [options_en[i] for i in order]
        options_zh = [translate_en_to_zh(opt) for opt in options_en]
        ans_idx = options_en.index(pop_en)
        ans_letter = chr(ord('A') + ans_idx)

        q = dict(
            type="single",
            stem=f"「{name}」試驗招募了哪一類病人？",
            stem_en=f'Which population did the "{name}" trial enroll?',
            ans=ans_letter,
            exp=f"「{name}」招募條件：{pop_zh}",
            exp_en=f'"{name}" enrolled: {pop_en}',
        )
        for i, (en, zh) in enumerate(zip(options_en, options_zh)):
            L = chr(ord('A')+i)
            q[L] = zh
            q[L+'_en'] = en
        qs.append(q)
    return qs

# ============================================================
# ASSEMBLE
# ============================================================
SECTIONS_ORDER = [
    ("基礎入門", "Foundations", ["Physics","RadBio","Clinical","Lingo"]),
    ("中樞神經系統", "Central Nervous System", ["CNS","BrainMets"]),
    ("頭頸與胸腔", "Head, Neck & Thorax", ["HeadNeck","Lung"]),
    ("乳癌與消化道", "Breast & GI", ["Breast","GI"]),
    ("泌尿與婦科", "GU & Gyn", ["GU","Prostate","Gyn"]),
    ("血液、肉瘤、皮膚", "Heme, Sarcoma, Skin", ["Lymphoma","Sarcoma","Skin"]),
    ("兒童與緩和", "Pediatrics & Palliative", ["Peds","Palliative"]),
    ("Estes 2025 關鍵試驗", "Estes 2025 Key Trials", []),
]

subjects = {}
labels_en = {}
for zh_sec, en_sec, subjs in SECTIONS_ORDER:
    labels_en[zh_sec] = en_sec
    subjects[zh_sec] = {}
    for skey in subjs:
        info = QBANK.get(skey)
        if not info: continue
        section_zh = info["section_zh"]
        section_en = info["section_en"]
        labels_en[section_zh] = section_en
        qs = [to_q(t) for t in info["questions"]]
        subjects[zh_sec][section_zh] = qs

trial_section_zh = "Estes 2025 關鍵試驗"
subjects[trial_section_zh] = {}
site_disp = {"Breast":"乳癌","CNS":"CNS","Cutaneous":"皮膚","GI":"消化道","GU":"泌尿","Gyn":"婦科",
             "H&N":"頭頸","Lung":"肺","Lymphoma":"淋巴瘤","Palliation":"緩和","Peds":"兒童",
             "Prostate":"攝護腺","Sarcoma":"肉瘤","Benign":"良性"}

for site in ["Breast","CNS","GI","GU","Gyn","H&N","Lung","Lymphoma","Palliation","Peds","Prostate","Sarcoma","Cutaneous","Benign"]:
    site_trials = TRIALS.get(site, [])
    if not site_trials: continue
    qs = trial_qs_for_site(site, site_trials)
    zh_label = f"{site_disp.get(site,site)} 試驗"
    en_label = f"{site} Trials"
    labels_en[zh_label] = en_label
    subjects[trial_section_zh][zh_label] = qs

def count_all():
    n = 0
    for sec, subs in subjects.items():
        for skey, qs in subs.items():
            n += len(qs)
    return n

# Trim trial sub-sections if total exceeds 1000
TARGET = 1000

def trim_to_target(target):
    # trim from each trial subsection uniformly
    while count_all() > target:
        biggest = None
        for skey, qs in subjects[trial_section_zh].items():
            if biggest is None or len(qs) > len(subjects[trial_section_zh][biggest]):
                biggest = skey
        if not biggest: break
        subjects[trial_section_zh][biggest].pop()

def top_up(target):
    tries = 0
    while count_all() < target and tries < 20:
        tries += 1
        best_site = None; best_pool = 0
        for site in ["Breast","CNS","GI","H&N","Lung","Prostate","Gyn","Peds","Lymphoma","Palliation","GU","Sarcoma"]:
            pool = len(TRIALS.get(site, []))
            if pool > best_pool:
                best_pool = pool; best_site = site
        add = trial_qs_for_site(best_site, TRIALS[best_site], seed_offset=tries)
        zh_label = f"{site_disp.get(best_site, best_site)} 試驗 (延伸 {tries})"
        labels_en[zh_label] = f"{best_site} Trials (extended {tries})"
        remaining = target - count_all()
        subjects[trial_section_zh][zh_label] = add[:max(1, remaining)]
        if count_all() >= target: break

print("Before adjust:", count_all())
if count_all() < TARGET:
    top_up(TARGET)
if count_all() > TARGET:
    trim_to_target(TARGET)
print("Final count:", count_all())

# Print breakdown
for sec, subs in subjects.items():
    tot = sum(len(qs) for qs in subs.values())
    print(f"  {sec}: {tot} Q  ({len(subs)} subs)")

# Emit
DATA = {
    "radonc": {
        "label": "☢️ 放射腫瘤學互動考題",
        "label_en": "☢️ Rad Onc Interactive Quiz",
        "labels_en": labels_en,
        "subjects": subjects,
    }
}

out_path = os.path.join(ROOT, "radonc-quiz", "data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("/* Rad Onc Interactive Quiz — bilingual question bank (auto-generated).\n"
            " * Schema per question: type=\"single\"|\"multi\"|\"tf\"; ans letter or list; stem/A/B/C/D/exp bilingual.\n"
            " */\nwindow.QUIZ_DATA = ")
    json.dump(DATA, f, ensure_ascii=False, indent=1)
    f.write(";\n")
print("Wrote", out_path, "-", os.path.getsize(out_path), "bytes")
