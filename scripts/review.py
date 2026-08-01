import csv
import os
import re
from datetime import datetime

INPUT_CSV = "csv_dropbox/CourseReview.csv"
OUTPUT_DIR = "_posts/courses"

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

def diff_field(difficulty):
    if not difficulty or not difficulty.strip().isdigit():
        return ""
    d = int(difficulty.strip())
    d = max(1, min(5, d))
    dots = "●" * d + "○" * (5 - d)
    return (f'<div class="review-field">\n'
            f'  <span class="review-label">⚡ Difficulty</span>\n'
            f'  <span class="review-value"><span class="diff-dots">{dots}</span> {d}/5</span>\n'
            f'</div>')

# ─────────────────────────────────────────────
# Course & tag name mappings
# ─────────────────────────────────────────────

COURSE_NAMES = {
    "cs747": "Foundations of Intelligent and Learning Agents",
    "ee622": "Optimal Control",
    "sc602": "Control of Nonlinear Dynamical Systems",
    "sc649": "Embedded Control and Robotics",
    "sc655": "Random Processes in Learning and Control",
    "sc664": "Active Vibration and Control",
    "ee601": "Statistical Signal Analysis",
    "ee603": "Digital Signal Processing",
    "me779": "Control Systems",
    "sc625": "Systems Theory",
    "sc639": "Mathematical Structure for Control",
    "sc624": "Differential Geometric Methods in Control",
    "cs725": "Foundation of Machine Learning",
    "cs728": "Organization of Web Information",
    "ee706": "Communication Networks",
}

TAG_FIXES = {
    "sc602": "SC602", "sc 602": "SC602",
    "ee622": "EE622", "ee 622": "EE622",
    "ee706": "EE706", "ee 706": "EE706",
    "sc625": "SC625", "sc 625": "SC625",
    "sc649": "SC649", "sc 649": "SC649",
    "sc639": "SC639", "sc 639": "SC639",
    "cs725": "CS725", "cs 725": "CS725",
    "cs747": "CS747", "cs 747": "CS747",
    "ee601": "EE601", "ee 601": "EE601",
    "ee603": "EE603", "ee 603": "EE603",
    "me779": "ME779", "me 779": "ME779",
    "sc624": "SC624", "sc 624": "SC624",
    "sc655": "SC655", "sc 655": "SC655",
    "sc664": "SC664", "sc 664": "SC664",
    "cs728": "CS728", "cs 728": "CS728",
}

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
    "md saif ali": "Md Saif Ali",
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
        row = {k.strip(): v.strip() for k, v in row.items()}

        student_name = row.get("Name", "") or row.get("Student's Name", "") or "Unknown"
        roll_no      = row.get("Roll Number", "") or row.get("Student's Roll Number", "") or row.get("Roll No", "")
        course_code  = row.get("course code", "") or row.get("Course Code", "")
        timestamp    = row.get("Timestamp", "")
        semester     = row.get("Semester", "")
        year         = row.get("Year", "")
        instructor   = row.get("Instructor", "")
        prereqs      = row.get("Prerequisites", "")
        grading      = row.get("Grading Criteria (what was marks distribution for exams/assignments/etc..)", "") or \
                       row.get("Grading Criteria", "")
        course_c     = row.get("Course Content", "")
        lec_fb       = row.get("Feedback on Lectures", "")
        assign_fb    = row.get("Feedback on Assignments/Tutorials/Homework", "") or \
                       row.get("Feedback on Assignments", "")
        exam_fb      = row.get("Feedback on Exams", "")
        difficulty   = row.get("Difficulty (on a scale of 1-5 with 5 being very tough)", "") or \
                       row.get("Difficulty", "")
        textbooks    = row.get("Textbooks/References", "") or row.get("Textbooks", "")
        software     = row.get("Software Used (If any)", "") or row.get("Software Used", "")
        takeaway     = row.get("Final Takeaway", "")

        dt        = parse_timestamp(timestamp)
        file_date = dt.strftime("%Y-%m-%d")
        full_date = dt.strftime("%Y-%m-%d %H:%M:%S +0800")

        clean_name   = re.sub(r'\s+', ' ', student_name.lower().strip())
        author_key   = NAME_KEY_MAP.get(clean_name, student_name)

        clean_code   = course_code.strip().lower().replace(" ", "")
        tag_name     = TAG_FIXES.get(course_code.strip().lower(), course_code.upper().replace(" ", ""))
        course_name  = COURSE_NAMES.get(clean_code, "")

        title_slug  = slugify(f"{course_code}-{student_name}")
        filename    = f"{file_date}-{title_slug}.md"
        filepath    = os.path.join(OUTPUT_DIR, filename)
        generated_files.add(filename)

        # Update authors.yml
        authors_file = "_data/authors.yml"
        if os.path.exists(authors_file):
            try:
                import yaml
                with open(authors_file, "r", encoding="utf-8") as yf:
                    authors_data = yaml.safe_load(yf) or {}
                if author_key not in authors_data:
                    authors_data[author_key] = {"name": author_key}
                    with open(authors_file, "w", encoding="utf-8") as yf:
                        yaml.safe_dump(authors_data, yf, allow_unicode=True, default_flow_style=False)
            except Exception as e:
                print(f"Error updating authors.yml: {e}")

        # Build grid fields
        grid = "".join(filter(None, [
            make_field("👤", "Reviewed by", student_name),
            make_field("🆔", "Roll No.", roll_no),
            make_field("📘", "Course Code", tag_name),
            make_field("👩‍🏫", "Instructor", instructor),
            make_field("📅", "Year", year),
            make_field("🗓️", "Semester", semester),
            diff_field(difficulty),
        ]))

        # Header semester+year tag
        tag_text = ", ".join(filter(None, [semester, year]))
        meta_text = tag_name + (" · " + instructor if instructor else "")

        card = f"""---
title: {tag_name}
author: {author_key}
date: {full_date}
categories: [CourseReview]
tags: [{tag_name}]
render_with_liquid: false
auto_generated: true
---

<div class="review-card">

<div class="review-header">
  <div class="review-header-info">
    <span class="review-company-name">{course_name or tag_name}</span>
    <span class="review-meta">{meta_text}</span>
  </div>
  <span class="review-tag">{tag_text}</span>
</div>

<div class="review-grid">
{grid}
</div>

{make_field_block("🔗", "Prerequisites", prereqs)}
{make_field_block("📊", "Grading Criteria", grading)}
{make_field_block("📚", "Course Content", course_c)}
{make_field_block("🎙️", "Feedback on Lectures", lec_fb)}
{make_field_block("📝", "Feedback on Assignments", assign_fb)}
{make_field_block("📋", "Feedback on Exams", exam_fb)}
{make_field_block("📖", "Textbooks / References", textbooks)}
{make_field_block("💻", "Software Used", software)}
{make_field_block("🏁", "Final Takeaway", takeaway)}

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

print("Course review markdown files generated successfully.")
