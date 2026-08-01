import csv
import os
import re
from datetime import datetime

INPUT_CSV = "csv_dropbox/placement.csv"
OUTPUT_DIR = "_posts/placement"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text

def parse_timestamp(timestamp):
    for fmt in ("%m/%d/%Y %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
        try:
            return datetime.strptime(timestamp.strip(), fmt)
        except:
            pass
    return datetime.now()

def is_empty(val):
    return not val or val.strip().lower() in ("", "n/a", "na", "none", "null", "-", "—")

def make_field(icon, label, value):
    if is_empty(value):
        return ""
    return (f'<div class="review-field">\n'
            f'  <span class="review-label">{icon} {label}</span>\n'
            f'  <span class="review-value">{value.strip()}</span>\n'
            f'</div>')

def make_field_block(icon, label, value):
    if is_empty(value):
        return ""
    vh = value.strip().replace("\n", "<br>")
    return (f'<div class="review-field-block">\n'
            f'  <span class="review-label">{icon} {label}</span>\n'
            f'  <div class="review-block-value">{vh}</div>\n'
            f'</div>')

def make_round_block(num, content):
    if is_empty(content):
        return ""
    ch = content.strip().replace("\n", "<br>")
    return (f'<div class="review-round">\n'
            f'  <span class="review-round-badge">Round {num}</span>\n'
            f'  <div class="review-round-content">{ch}</div>\n'
            f'</div>\n')

# ─────────────────────────────────────────────
# Name & tag mappings
# ─────────────────────────────────────────────

NAME_KEY_MAP = {
    "jatinkumar": "Jatinkumar",
    "narendra muley": "Narendra Muley",
    "nithin kumar": "Nithin Kumar",
    "avik ghosh": "Avik Ghosh",
    "bharat kandpal": "Bharat Kandpal",
    "vaibhav upadhyay": "Vaibhav Upadhyay",
    "carlyn medona": "Carlyn Medona",
    "vinay bujja": "Vinay Bujja",
    "rohit dilip patil": "Rohit Dilip Patil",
    "rohit patil": "Rohit Patil",
    "shailesh kishor mahindrakar": "Shailesh Kishor Mahindrakar",
    "prashik patil": "Prashik Patil",
    "vinayak bhardwaj": "Vinayak Bhardwaj",
    "rohit kumar": "Rohit Kumar",
    "sanku venkatesh": "Sanku Venkatesh",
    "md saif ali": "Md Saif Ali",
}

TAG_FIXES = {
    "kas global": "Kas Global",
    "eaton": "Eaton",
    "gruve": "Gruve",
    "ideaforge": "IdeaForge",
    "bombay stock exchange": "Bombay Stock Exchange",
    "texas instruments": "Texas Instruments",
    "visa": "Visa",
}

# ─────────────────────────────────────────────
# CSV → HTML card
# ─────────────────────────────────────────────

if not os.path.exists(INPUT_CSV):
    print(f"No CSV found at {INPUT_CSV}, skipping.")
    exit(0)

with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames = [h.strip() for h in reader.fieldnames]

    generated_files = set()

    for row in reader:
        row = {k.strip(): (v.strip() if v else "") for k, v in row.items()}

        student_name = row.get("Student's Name", "Unknown")
        roll_no      = row.get("Student's Roll Number", "") or row.get("Roll Number", "") or row.get("Roll No", "")
        company      = row.get("Company Name", "Company")
        timestamp    = row.get("Timestamp", "")
        year         = row.get("Placement Year", "")
        season       = row.get("Placement season", "")
        domain       = row.get("Domain", "")
        position     = row.get("Position/Job Titlle", "") or row.get("Position/Job Title", "")
        comp_d       = row.get("Compensation Details", "")
        job_desc     = row.get("Job Description", "")
        screening    = row.get("Online Test/ Screening Details", "")
        selected     = row.get("Selected for Interview?", "")
        total_r      = row.get("Total Interview Rounds", "")
        verdict      = row.get("Final Verdict", "")
        prep         = row.get("Any preparation strategy", "")
        tips         = row.get("Suggestions/Tips", "")

        dt        = parse_timestamp(timestamp)
        file_date = dt.strftime("%Y-%m-%d")
        full_date = dt.strftime("%Y-%m-%d %H:%M:%S +0800")

        clean_name  = re.sub(r'\s+', ' ', student_name.lower().strip())
        author_key  = NAME_KEY_MAP.get(clean_name, student_name)

        clean_co    = company.strip().lower()
        tag_name    = TAG_FIXES.get(clean_co, company)

        slug        = slugify(f"{company}-{student_name}")
        filename    = f"{file_date}-{slug}.md"
        filepath    = os.path.join(OUTPUT_DIR, filename)
        generated_files.add(filename)

        # Verdict badge
        verdict_cls = ("badge-selected" if verdict.lower() == "selected"
                       else "badge-rejected" if verdict.lower() == "rejected"
                       else "badge-neutral")

        # Build rounds section
        rounds_html = ""
        for i in range(1, 8):
            r = row.get(f"Round {i}", "")
            block = make_round_block(i, r)
            if block:
                rounds_html += block

        # Grid fields
        grid = "".join(filter(None, [
            make_field("👤", "Student", student_name),
            make_field("🆔", "Roll No.", roll_no),
            make_field("📅", "Placement Year", year),
            make_field("📆", "Season", season),
            make_field("💼", "Position", position),
            make_field("💰", "Compensation", comp_d),
        ]))

        extra = "".join(filter(None, [
            make_field_block("📋", "Job Description", job_desc),
            make_field_block("🖥️", "Online Test / Screening", screening),
            f'<div class="review-field-block"><span class="review-label">✅ Selected for Interview</span><div class="review-block-value">{selected}</div></div>' if not is_empty(selected) else "",
            f'<div class="review-field-block"><span class="review-label">🔄 Total Interview Rounds</span><div class="review-block-value">{total_r}</div></div>' if not is_empty(total_r) else "",
        ]))

        meta_text = domain + (" · " + position if position else "")

        card = f"""---
title: {company}
author: {author_key}
date: {full_date}
categories:
- PlacementReview
tags:
- {tag_name}
render_with_liquid: false
auto_generated: true
---

<div class="review-card">

<div class="review-header">
  <div class="review-header-info">
    <span class="review-company-name">{company}</span>
    <span class="review-meta">{meta_text}</span>
  </div>
  <span class="review-verdict-badge {verdict_cls}">{verdict or "—"}</span>
</div>

<div class="review-grid">
{grid}
</div>

{extra}

{('<div class="review-rounds-section"><h3 class="review-section-title">📝 Interview Rounds</h3>' + rounds_html + '</div>') if rounds_html else ""}

{make_field_block("🎯", "Preparation Strategy", prep)}
{make_field_block("💡", "Suggestions & Tips", tips)}

</div>
"""

        with open(filepath, "w", encoding="utf-8") as md:
            md.write(card)

    # Clean stale auto-generated files
    if os.path.exists(OUTPUT_DIR):
        for existing_file in os.listdir(OUTPUT_DIR):
            if existing_file.endswith(".md") and existing_file not in generated_files:
                fpath_check = os.path.join(OUTPUT_DIR, existing_file)
                with open(fpath_check, "r", encoding="utf-8") as f:
                    content = f.read()
                if "auto_generated: true" in content:
                    os.remove(fpath_check)

print("Placement review markdown files generated successfully.")
