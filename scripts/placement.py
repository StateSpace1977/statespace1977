import csv
import os
import re
from datetime import datetime

INPUT_CSV = "csv_dropbox/placement.csv"
OUTPUT_DIR = "_posts/placement"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text

def parse_timestamp(timestamp):
    try:
        return datetime.strptime(timestamp.strip(), "%m/%d/%Y %H:%M:%S")
    except:
        return datetime.now()

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
        company = row.get("Company Name", "company")
        timestamp = row.get("Timestamp", "")

        dt = parse_timestamp(timestamp)
        file_date = dt.strftime("%Y-%m-%d")
        full_date = dt.strftime("%Y-%m-%d %H:%M:%S +0800")

        slug = slugify(f"{company}-{student_name}")
        filename = f"{file_date}-{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        generated_files.add(filename)

        name_to_key_map = {
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
            "sanku venkatesh": "Sanku Venkatesh"
        }
        
        clean_name = student_name.strip().lower()
        author_key = name_to_key_map.get(clean_name, student_name)
        
        tag_fixes = {
            "kas global": "Kas Global",
            "eaton": "Eaton",
            "gruve": "Gruve",
            "ideaforge": "IdeaForge",
            "bombay stock exchange": "Bombay Stock Exchange",
            "texas instruments": "Texas Instruments",
            "visa": "Visa"
        }
        
        clean_company = company.strip().lower()
        tag_name = tag_fixes.get(clean_company, company)

        with open(filepath, "w", encoding="utf-8") as md:
            md.write("---\n")
            md.write(f"title: {company}\n")
            md.write(f"author: {author_key}\n")
            md.write(f"date: {full_date}\n")
            md.write("categories: [PlacementReview]\n")
            md.write(f"tags: [{tag_name}]\n")
            md.write("render_with_liquid: false\n")
            md.write("auto_generated: true\n")
            md.write("---\n\n")

            for field, value in row.items():
                md.write(f"## {field}\n")
                md.write(f"{value}\n\n")

    # Clean up any stale markdown files in the directory
    if os.path.exists(OUTPUT_DIR):
        for existing_file in os.listdir(OUTPUT_DIR):
            if existing_file.endswith(".md") and existing_file not in generated_files:
                file_path_to_check = os.path.join(OUTPUT_DIR, existing_file)
                with open(file_path_to_check, "r", encoding="utf-8") as f:
                    content = f.read()
                # ONLY delete if it has the auto_generated flag
                if "auto_generated: true" in content:
                    os.remove(file_path_to_check)

print("Placement markdown files generated successfully and stale files cleaned up.")
