"""Generate one bilingual HTML page per Rad Onc topic.
Combines curated overview content (EN/ZH) with trial cards pulled from trials.json.
"""
import json, os, html, re

ROOT = r"C:\Users\ydai\Desktop\RT2\radonc-tutorial"
TRIALS = json.load(open(os.path.join(ROOT, "data", "trials.json"), encoding="utf-8"))

# Nav (matches index.html)
NAV = '''<nav class="top-nav"><div class="top-nav-inner">
  <a href="index.html" class="top-nav-brand"><span>☢️</span> <span data-zh="放射腫瘤學教學" data-en="Rad Onc Tutorial">Rad Onc Tutorial</span></a>
  <ul class="top-nav-links">
    <li><a href="intro-clinical.html" data-zh="臨床" data-en="Clinical">Clinical</a></li>
    <li><a href="physics.html" data-zh="物理" data-en="Physics">Physics</a></li>
    <li><a href="radbio.html" data-zh="放射生物" data-en="RadBio">RadBio</a></li>
    <li><a href="cns.html" data-zh="CNS" data-en="CNS">CNS</a></li>
    <li><a href="headneck.html" data-zh="頭頸" data-en="H&amp;N">H&amp;N</a></li>
    <li><a href="brain-mets.html" data-zh="腦轉移" data-en="Brain mets">Brain mets</a></li>
    <li><a href="lung.html" data-zh="肺" data-en="Lung">Lung</a></li>
    <li><a href="breast.html" data-zh="乳癌" data-en="Breast">Breast</a></li>
    <li><a href="gi.html" data-zh="消化道" data-en="GI">GI</a></li>
    <li><a href="gu.html" data-zh="泌尿" data-en="GU">GU</a></li>
    <li><a href="prostate.html" data-zh="攝護腺" data-en="Prostate">Prostate</a></li>
    <li><a href="gyn.html" data-zh="婦科" data-en="Gyn">Gyn</a></li>
    <li><a href="lymphoma.html" data-zh="淋巴瘤" data-en="Lymphoma">Lymphoma</a></li>
    <li><a href="sarcoma.html" data-zh="肉瘤" data-en="Sarcoma">Sarcoma</a></li>
    <li><a href="skin.html" data-zh="皮膚" data-en="Skin">Skin</a></li>
    <li><a href="peds.html" data-zh="兒童" data-en="Peds">Peds</a></li>
    <li><a href="palliative.html" data-zh="緩和" data-en="Palliative">Palliative</a></li>
    <li><a href="radonc-quiz/index.html" target="_blank" data-zh="📝 考題" data-en="📝 Quiz">📝 Quiz</a></li>
  </ul>
</div></nav>'''

def esc(s):
    return html.escape(s or "", quote=True)

def render_trial_card(t):
    """Render one trial as a card."""
    trial = esc(t.get("trial",""))
    citation = esc(t.get("citation",""))
    n = esc(str(t.get("n","")))
    patients = esc(t.get("patients",""))
    methods = esc(t.get("methods","")).replace("\n","<br>")
    results = esc(t.get("results","")).replace("\n","<br>")
    interp = esc(t.get("interpretation","")).replace("\n","<br>")
    topic = esc(t.get("topic",""))
    sub = esc(t.get("subtopic",""))
    return f'''<div class="card" style="margin-bottom:14px">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <h4 style="margin:0">{trial or '(Unnamed)'}</h4>
        <span style="font-size:.75rem;color:var(--c-ink-muted);white-space:nowrap">{topic} · {sub}</span>
      </div>
      <p style="margin:0 0 6px;font-size:.85rem;color:var(--c-ink-muted)"><strong>{citation}</strong>{f" · N={n}" if n and n!="None" else ""}</p>
      {f'<p style="margin:0 0 8px;font-size:.9rem"><strong data-zh="病人族群：" data-en="Population: ">Population: </strong>{patients}</p>' if patients else ''}
      {f'<p style="margin:0 0 8px;font-size:.9rem"><strong data-zh="方法：" data-en="Methods: ">Methods: </strong>{methods}</p>' if methods else ''}
      {f'<p style="margin:0 0 8px;font-size:.9rem"><strong data-zh="結果：" data-en="Results: ">Results: </strong>{results}</p>' if results else ''}
      {f'<p style="margin:0;font-size:.9rem;background:var(--c-accent-light);padding:8px 12px;border-radius:6px"><strong data-zh="解讀：" data-en="Interpretation: ">Interpretation: </strong>{interp}</p>' if interp else ''}
    </div>'''

def build_topic_html(page):
    """page is a dict describing one page."""
    slug = page["slug"]
    title_zh = page["title_zh"]
    title_en = page["title_en"]
    emoji = page.get("emoji","🩺")
    subtitle_zh = page.get("sub_zh","")
    subtitle_en = page.get("sub_en","")
    sections = page.get("sections", [])
    excel_sheet = page.get("excel_sheet")
    trial_filter = page.get("trial_filter")  # function-like: keywords list to filter subtopic
    prev_page = page.get("prev")
    next_page = page.get("next")

    # Collect trials for this topic
    trial_html = ""
    if excel_sheet and excel_sheet in TRIALS:
        trials = TRIALS[excel_sheet]
        if trial_filter:
            trials = [t for t in trials if any(kw.lower() in (t.get("topic","")+" "+t.get("subtopic","")+" "+t.get("trial","")).lower() for kw in trial_filter)]
        # cap to first 25 to keep page reasonable
        trials = trials[:25]
        if trials:
            trial_html = '<section class="section"><div class="section-label" data-zh="關鍵試驗" data-en="KEY TRIALS">關鍵試驗</div><h2 data-zh="關鍵臨床試驗 (Estes 2025)" data-en="Key Clinical Trials (Estes 2025)">關鍵臨床試驗</h2>'
            trial_html += '<p data-lang="zh">以下為此主題的核心隨機試驗與樞紐研究，資料源自 Estes 2025 Key Studies 資料表，已整合於本章。</p>'
            trial_html += '<p data-lang="en">Core randomized trials and pivotal studies for this topic, from the Estes 2025 Key Studies tables, are integrated into this chapter.</p>'
            for t in trials:
                trial_html += render_trial_card(t)
            trial_html += '</section>'

    # Build sections
    sect_html = ""
    for i, s in enumerate(sections):
        label_zh = s.get("label_zh", "章節")
        label_en = s.get("label_en", "SECTION")
        h2_zh = s.get("h2_zh", "")
        h2_en = s.get("h2_en", "")
        body_zh = s.get("body_zh", "")
        body_en = s.get("body_en", "")
        sect_html += f'''<section class="section">
<div class="section-label" data-zh="{label_zh}" data-en="{label_en}">{label_zh}</div>
<h2 data-zh="{h2_zh}" data-en="{h2_en}">{h2_zh}</h2>
<div data-lang="zh">{body_zh}</div>
<div data-lang="en">{body_en}</div>
</section>
'''

    # Page nav
    nav_html = '<div class="page-nav">'
    if prev_page:
        nav_html += f'<a href="{prev_page[0]}"><span class="nav-dir">← <span data-zh="上一章" data-en="Previous">上一章</span></span><span class="nav-title" data-zh="{prev_page[1]}" data-en="{prev_page[2]}">{prev_page[1]}</span></a>'
    else:
        nav_html += '<div class="placeholder"></div>'
    if next_page:
        nav_html += f'<a href="{next_page[0]}"><span class="nav-dir"><span data-zh="下一章" data-en="Next">下一章</span> →</span><span class="nav-title" data-zh="{next_page[1]}" data-en="{next_page[2]}">{next_page[1]}</span></a>'
    else:
        nav_html += '<div class="placeholder"></div>'
    nav_html += '</div>'

    html_out = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title_en} — Rad Onc Tutorial</title>
<link rel="stylesheet" href="styles.css"></head><body>
{NAV}
<div class="progress-bar-container"><div class="progress-bar" id="progressBar"></div></div>
<header class="page-hero"><div class="step-badge">{emoji} {title_en.upper()}</div>
<h1 data-zh="{title_zh}" data-en="{title_en}">{title_zh}</h1>
<p class="subtitle" data-lang="zh">{subtitle_zh}</p>
<p class="subtitle" data-lang="en">{subtitle_en}</p>
</header>
<main class="content-wrap">
{sect_html}
{trial_html}
{nav_html}
</main>
<footer class="site-footer">© Rad Onc Interactive Tutorial · <a href="index.html" data-zh="返回首頁" data-en="Back to home">Back to home</a></footer>
<script src="i18n.js"></script>
<script>
window.addEventListener('scroll',()=>{{
  const bar=document.getElementById('progressBar');
  if(!bar) return;
  const h=document.documentElement,b=document.body;
  const st='scrollTop',sh='scrollHeight';
  const p=(h[st]||b[st])/((h[sh]||b[sh])-h.clientHeight)*100;
  bar.style.width=p+'%';
}});
</script>
</body></html>'''
    return html_out


if __name__ == "__main__":
    from topics_config import PAGES
    for p in PAGES:
        outp = os.path.join(ROOT, p["slug"] + ".html")
        with open(outp, "w", encoding="utf-8") as f:
            f.write(build_topic_html(p))
        print("Wrote", outp)
