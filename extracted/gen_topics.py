"""Generate one bilingual HTML page per Rad Onc topic.

Combines curated overview content (EN/ZH) with trial cards pulled from trials.json.

Each page can define:
- its own stylesheet
- a page-specific body class
- CSS variables
- custom CSS
- custom head HTML
- section-specific classes and styles
"""

import json
import os
import html


ROOT = r"/Users/arthurdai/Desktop/radonc-tutorial/radonc-tutorial-main"

TRIALS_PATH = os.path.join(ROOT, "data", "trials.json")

with open(TRIALS_PATH, encoding="utf-8") as f:
    TRIALS = json.load(f)


# ---------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------

NAV = """
<nav class="top-nav">
  <div class="top-nav-inner">

    <a href="index.html" class="top-nav-brand">
      <span>☢️</span>
      <span
        data-zh="放射腫瘤學教學"
        data-en="Rad Onc Tutorial"
      >
        Rad Onc Tutorial
      </span>
    </a>

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
      <li>
        <a
          href="radonc-quiz/index.html"
          target="_blank"
          rel="noopener noreferrer"
          data-zh="📝 考題"
          data-en="📝 Quiz"
        >
          📝 Quiz
        </a>
      </li>
    </ul>

  </div>
</nav>
"""


# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------

def esc(value):
    """Escape text for safe insertion into HTML attributes or content."""
    return html.escape(str(value or ""), quote=True)


def render_style_attribute(styles):
    """Convert a dict of CSS properties into an inline style attribute.

    Example:
        {
            "background": "#f7fbff",
            "border-left": "4px solid #2474a6"
        }

    Returns:
        style="background:#f7fbff;border-left:4px solid #2474a6"
    """
    if not styles:
        return ""

    style_text = ";".join(
        f"{esc(property_name)}:{esc(property_value)}"
        for property_name, property_value in styles.items()
        if property_name and property_value is not None
    )

    return f' style="{style_text}"' if style_text else ""


def render_css_variables(variables):
    """Convert a dictionary into CSS custom properties.

    Example:
        {
            "accent": "#1565c0",
            "accent-light": "#e3f2fd"
        }

    Returns:
        --accent:#1565c0;--accent-light:#e3f2fd;
    """
    if not variables:
        return ""

    return "".join(
        f"--{esc(name)}:{esc(value)};"
        for name, value in variables.items()
        if name and value is not None
    )


def render_stylesheet_links(stylesheets):
    """Render additional page-specific stylesheet links."""
    if not stylesheets:
        return ""

    if isinstance(stylesheets, str):
        stylesheets = [stylesheets]

    links = []

    for stylesheet in stylesheets:
        if stylesheet:
            links.append(
                f'<link rel="stylesheet" href="{esc(stylesheet)}">'
            )

    return "\n".join(links)


# ---------------------------------------------------------------------
# Trial cards
# ---------------------------------------------------------------------

def render_trial_card(trial, card_class="", card_styles=None):
    """Render one clinical trial as a card."""

    trial_name = esc(trial.get("trial", ""))
    citation = esc(trial.get("citation", ""))
    sample_size = esc(trial.get("n", ""))
    patients = esc(trial.get("patients", ""))
    methods = esc(trial.get("methods", "")).replace("\n", "<br>")
    results = esc(trial.get("results", "")).replace("\n", "<br>")
    interpretation = esc(
        trial.get("interpretation", "")
    ).replace("\n", "<br>")
    topic = esc(trial.get("topic", ""))
    subtopic = esc(trial.get("subtopic", ""))

    class_names = ["card", "trial-card"]

    if card_class:
        class_names.append(card_class)

    class_attribute = " ".join(class_names)

    default_card_styles = {
        "margin-bottom": "14px"
    }

    if card_styles:
        default_card_styles.update(card_styles)

    style_attribute = render_style_attribute(default_card_styles)

    sample_size_html = ""

    if sample_size and sample_size.lower() not in {"none", "null"}:
        sample_size_html = f" · N={sample_size}"

    patients_html = ""

    if patients:
        patients_html = f"""
        <p class="trial-population">
          <strong
            data-zh="病人族群："
            data-en="Population: "
          >
            Population:
          </strong>
          {patients}
        </p>
        """

    methods_html = ""

    if methods:
        methods_html = f"""
        <p class="trial-methods">
          <strong
            data-zh="方法："
            data-en="Methods: "
          >
            Methods:
          </strong>
          {methods}
        </p>
        """

    results_html = ""

    if results:
        results_html = f"""
        <p class="trial-results">
          <strong
            data-zh="結果："
            data-en="Results: "
          >
            Results:
          </strong>
          {results}
        </p>
        """

    interpretation_html = ""

    if interpretation:
        interpretation_html = f"""
        <p class="trial-interpretation">
          <strong
            data-zh="解讀："
            data-en="Interpretation: "
          >
            Interpretation:
          </strong>
          {interpretation}
        </p>
        """

    return f"""
    <article class="{class_attribute}"{style_attribute}>

      <div class="trial-card-header">
        <h4>{trial_name or "(Unnamed)"}</h4>

        <span class="trial-topic">
          {topic} · {subtopic}
        </span>
      </div>

      <p class="trial-citation">
        <strong>{citation}</strong>{sample_size_html}
      </p>

      {patients_html}
      {methods_html}
      {results_html}
      {interpretation_html}

    </article>
    """


# ---------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------

def render_section(section, section_index):
    """Render one content section with optional custom styling."""

    label_zh = esc(section.get("label_zh", "章節"))
    label_en = esc(section.get("label_en", "SECTION"))

    h2_zh = esc(section.get("h2_zh", ""))
    h2_en = esc(section.get("h2_en", ""))

    # body_zh and body_en intentionally remain raw HTML.
    # Only use trusted content in topics_config.py.
    body_zh = section.get("body_zh", "")
    body_en = section.get("body_en", "")

    section_id = esc(
        section.get("id", f"section-{section_index + 1}")
    )

    custom_class = section.get("class", "")
    class_names = ["section"]

    if custom_class:
        class_names.append(custom_class)

    class_attribute = " ".join(class_names)

    style_attribute = render_style_attribute(
        section.get("styles")
    )

    label_class = esc(
        section.get("label_class", "")
    )

    heading_class = esc(
        section.get("heading_class", "")
    )

    zh_class = esc(
        section.get("zh_class", "")
    )

    en_class = esc(
        section.get("en_class", "")
    )

    return f"""
    <section
      id="{section_id}"
      class="{class_attribute}"
      {style_attribute}
    >

      <div
        class="section-label {label_class}"
        data-zh="{label_zh}"
        data-en="{label_en}"
      >
        {label_zh}
      </div>

      <h2
        class="{heading_class}"
        data-zh="{h2_zh}"
        data-en="{h2_en}"
      >
        {h2_zh}
      </h2>

      <div
        class="section-body section-body-zh {zh_class}"
        data-lang="zh"
      >
        {body_zh}
      </div>

      <div
        class="section-body section-body-en {en_class}"
        data-lang="en"
      >
        {body_en}
      </div>

    </section>
    """


# ---------------------------------------------------------------------
# Page navigation
# ---------------------------------------------------------------------

def render_page_navigation(previous_page, next_page):
    """Render previous/next chapter navigation."""

    parts = ['<div class="page-nav">']

    if previous_page:
        previous_href = esc(previous_page[0])
        previous_zh = esc(previous_page[1])
        previous_en = esc(previous_page[2])

        parts.append(f"""
        <a href="{previous_href}" class="page-nav-link page-nav-prev">
          <span class="nav-dir">
            ←
            <span data-zh="上一章" data-en="Previous">
              上一章
            </span>
          </span>

          <span
            class="nav-title"
            data-zh="{previous_zh}"
            data-en="{previous_en}"
          >
            {previous_zh}
          </span>
        </a>
        """)
    else:
        parts.append('<div class="placeholder"></div>')

    if next_page:
        next_href = esc(next_page[0])
        next_zh = esc(next_page[1])
        next_en = esc(next_page[2])

        parts.append(f"""
        <a href="{next_href}" class="page-nav-link page-nav-next">
          <span class="nav-dir">
            <span data-zh="下一章" data-en="Next">
              下一章
            </span>
            →
          </span>

          <span
            class="nav-title"
            data-zh="{next_zh}"
            data-en="{next_en}"
          >
            {next_zh}
          </span>
        </a>
        """)
    else:
        parts.append('<div class="placeholder"></div>')

    parts.append("</div>")

    return "\n".join(parts)


# ---------------------------------------------------------------------
# Main page generator
# ---------------------------------------------------------------------

def build_topic_html(page):
    """Build one topic page.

    Supported page-specific configuration fields:

    slug:
        Output filename without .html

    body_class:
        Additional class placed on <body>

    main_class:
        Additional class placed on <main>

    stylesheets:
        One stylesheet or a list of stylesheets

    css_variables:
        CSS variables inserted on <body>

    custom_css:
        Raw page-specific CSS inserted into <head>

    custom_head:
        Additional raw HTML inserted into <head>

    hero_class:
        Additional class for the page hero

    hero_styles:
        Inline styles for the page hero

    trial_card_class:
        Additional class for all trial cards on this page

    trial_card_styles:
        Inline styles for all trial cards on this page
    """

    slug = page["slug"]

    title_zh = page["title_zh"]
    title_en = page["title_en"]

    emoji = page.get("emoji", "🩺")

    subtitle_zh = page.get("sub_zh", "")
    subtitle_en = page.get("sub_en", "")

    sections = page.get("sections", [])

    excel_sheet = page.get("excel_sheet")
    trial_filter = page.get("trial_filter")

    previous_page = page.get("prev")
    next_page = page.get("next")

    # -------------------------------------------------------------
    # Page-specific styles
    # -------------------------------------------------------------

    body_class = page.get("body_class", "")
    main_class = page.get("main_class", "")
    hero_class = page.get("hero_class", "")

    extra_stylesheets = render_stylesheet_links(
        page.get("stylesheets")
    )

    css_variables = render_css_variables(
        page.get("css_variables")
    )

    body_style_attribute = (
        f' style="{css_variables}"'
        if css_variables
        else ""
    )

    custom_css = page.get("custom_css", "")
    custom_css_html = ""

    if custom_css.strip():
        custom_css_html = f"""
        <style>
        {custom_css}
        </style>
        """

    custom_head = page.get("custom_head", "")

    hero_style_attribute = render_style_attribute(
        page.get("hero_styles")
    )

    # -------------------------------------------------------------
    # Trial cards
    # -------------------------------------------------------------

    trial_html = ""

    if excel_sheet and excel_sheet in TRIALS:
        trials = TRIALS[excel_sheet]

        if trial_filter:
            filter_keywords = [
                keyword.lower()
                for keyword in trial_filter
            ]

            filtered_trials = []

            for trial in trials:
                searchable_text = " ".join([
                    str(trial.get("topic", "")),
                    str(trial.get("subtopic", "")),
                    str(trial.get("trial", ""))
                ]).lower()

                if any(
                    keyword in searchable_text
                    for keyword in filter_keywords
                ):
                    filtered_trials.append(trial)

            trials = filtered_trials

        trial_limit = page.get("trial_limit", 25)
        trials = trials[:trial_limit]

        if trials:
            trial_section_class = page.get(
                "trial_section_class",
                ""
            )

            trial_section_styles = render_style_attribute(
                page.get("trial_section_styles")
            )

            trial_html = f"""
            <section
              class="section trial-section {esc(trial_section_class)}"
              {trial_section_styles}
            >

              <div
                class="section-label"
                data-zh="關鍵試驗"
                data-en="KEY TRIALS"
              >
                關鍵試驗
              </div>

              <h2
                data-zh="關鍵臨床試驗 (Estes 2025)"
                data-en="Key Clinical Trials (Estes 2025)"
              >
                關鍵臨床試驗
              </h2>

              <p data-lang="zh">
                以下為此主題的核心隨機試驗與樞紐研究，資料源自
                Estes 2025 Key Studies 資料表，已整合於本章。
              </p>

              <p data-lang="en">
                Core randomized trials and pivotal studies for this
                topic, from the Estes 2025 Key Studies tables, are
                integrated into this chapter.
              </p>
            """

            for trial in trials:
                trial_html += render_trial_card(
                    trial,
                    card_class=page.get(
                        "trial_card_class",
                        ""
                    ),
                    card_styles=page.get(
                        "trial_card_styles"
                    )
                )

            trial_html += "</section>"

    # -------------------------------------------------------------
    # Main content sections
    # -------------------------------------------------------------

    sections_html = "".join(
        render_section(section, index)
        for index, section in enumerate(sections)
    )

    page_navigation_html = render_page_navigation(
        previous_page,
        next_page
    )

    safe_title_zh = esc(title_zh)
    safe_title_en = esc(title_en)
    safe_emoji = esc(emoji)
    safe_subtitle_zh = esc(subtitle_zh)
    safe_subtitle_en = esc(subtitle_en)

    body_classes = " ".join(
        item
        for item in [
            "topic-page",
            f"page-{esc(slug)}",
            esc(body_class)
        ]
        if item
    )

    main_classes = " ".join(
        item
        for item in [
            "content-wrap",
            esc(main_class)
        ]
        if item
    )

    hero_classes = " ".join(
        item
        for item in [
            "page-hero",
            esc(hero_class)
        ]
        if item
    )

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">

  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >

  <title>{safe_title_en} — Rad Onc Tutorial</title>

  <link rel="stylesheet" href="styles.css">

  {extra_stylesheets}

  {custom_css_html}

  {custom_head}
</head>

<body class="{body_classes}"{body_style_attribute}>

  {NAV}

  <div class="progress-bar-container">
    <div class="progress-bar" id="progressBar"></div>
  </div>

  <header
    class="{hero_classes}"
    {hero_style_attribute}
  >

    <div class="step-badge">
      {safe_emoji} {safe_title_en.upper()}
    </div>

    <h1
      data-zh="{safe_title_zh}"
      data-en="{safe_title_en}"
    >
      {safe_title_zh}
    </h1>

    <p class="subtitle" data-lang="zh">
      {safe_subtitle_zh}
    </p>

    <p class="subtitle" data-lang="en">
      {safe_subtitle_en}
    </p>

  </header>

  <main class="{main_classes}">

    {sections_html}

    {trial_html}

    {page_navigation_html}

  </main>

  <footer class="site-footer">
    © Rad Onc Interactive Tutorial ·
    <a
      href="index.html"
      data-zh="返回首頁"
      data-en="Back to home"
    >
      Back to home
    </a>
  </footer>

  <script src="i18n.js"></script>

  <script>
    window.addEventListener("scroll", () => {{
      const progressBar = document.getElementById("progressBar");

      if (!progressBar) {{
        return;
      }}

      const documentElement = document.documentElement;
      const body = document.body;

      const scrollTop =
        documentElement.scrollTop ||
        body.scrollTop;

      const scrollHeight =
        documentElement.scrollHeight ||
        body.scrollHeight;

      const availableScroll =
        scrollHeight - documentElement.clientHeight;

      const progress =
        availableScroll > 0
          ? (scrollTop / availableScroll) * 100
          : 0;

      progressBar.style.width = `${{progress}}%`;
    }});
  </script>

</body>
</html>
"""


# ---------------------------------------------------------------------
# Generate files
# ---------------------------------------------------------------------

if __name__ == "__main__":
    from topics_config import PAGES

    for page in PAGES:
        output_path = os.path.join(
            ROOT,
            page["slug"] + ".html"
        )

        page_html = build_topic_html(page)

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(page_html)

        print("Wrote", output_path)
