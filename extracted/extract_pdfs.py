"""Extract text from all Rad Onc Talks PDFs into a single JSON."""
import os, json, subprocess, re

ROOT = r"C:\Users\ydai\Desktop\RT2\Rad Onc Talks"
OUT = r"C:\Users\ydai\Desktop\RT2\radonc-tutorial\data\pdftext.json"

def extract(pdf_path):
    try:
        r = subprocess.run(
            ["pdftotext", "-layout", "-nopgbrk", pdf_path, "-"],
            capture_output=True, timeout=60
        )
        text = r.stdout.decode("utf-8", errors="replace")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()
    except Exception as e:
        return f"[ERROR: {e}]"

out = {}
for folder in sorted(os.listdir(ROOT)):
    fp = os.path.join(ROOT, folder)
    if not os.path.isdir(fp): continue
    topic = folder.replace("RadOncTalks ", "").strip()
    out[topic] = {}
    for f in sorted(os.listdir(fp)):
        if not f.lower().endswith(".pdf"): continue
        name = f[:-4]
        text = extract(os.path.join(fp, f))
        out[topic][name] = text
        print(f"{topic} / {name}: {len(text)} chars")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print(f"Done -> {OUT}")
