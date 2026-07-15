import csv
import os
import re
from datetime import datetime

INPUT_CSV = "csv_dropbox/CourseReview.csv"
OUTPUT_DIR = "_posts/courses"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text

def parse_timestamp(timestamp):
    try:
        dt = datetime.strptime(timestamp.strip(), "%m/%d/%Y %H:%M:%S")
        return dt
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
        row = {k.strip(): v for k, v in row.items()}
        student_name = row.get("Name", "").strip()
        course_code = row.get("course code", "").strip()
        timestamp = row.get("Timestamp", "").strip()

        if not student_name:
            student_name = "Unknown"

        dt = parse_timestamp(timestamp)
        file_date = dt.strftime("%Y-%m-%d")
        full_date = dt.strftime("%Y-%m-%d %H:%M:%S +0800")

        title_slug = slugify(f"{course_code}-{student_name}")
        filename = f"{file_date}-{title_slug}.md"
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
            "prashik patil": "Prashik Patil"
        }
        
        clean_name = student_name.strip().lower()
        clean_name = re.sub(r'\s+', ' ', clean_name)
        author_key = name_to_key_map.get(clean_name, student_name)
        
        tag_fixes = {
            "sc602": "SC602",
            "sc 602": "SC602",
            "ee622": "EE622",
            "ee 622": "EE622",
            "ee706": "EE706",
            "ee 706": "EE706",
            "sc625": "SC625",
            "sc 625": "SC625",
            "sc649": "SC649",
            "sc 649": "SC649",
            "sc639": "SC639",
            "sc 639": "SC639",
            "cs725": "CS725",
            "cs 725": "CS725",
            "cs747": "CS747",
            "cs 747": "CS747",
            "ee601": "EE601",
            "ee 601": "EE601",
            "ee603": "EE603",
            "ee 603": "EE603",
            "me779": "ME779",
            "me 779": "ME779",
            "sc624": "SC624",
            "sc 624": "SC624",
            "sc655": "SC655",
            "sc 655": "SC655",
            "sc664": "SC664",
            "sc 664": "SC664"
        }
        
        clean_course = course_code.strip().lower()
        tag_name = tag_fixes.get(clean_course, course_code)

        # Define course names mapping
        course_names = {
            "CS747": "Foundations of intelligent and learning agents",
            "CS 747": "Foundations of intelligent and learning agents",
            "EE622": "Optimal control",
            "EE 622": "Optimal control",
            "SC602": "Control of Nonlinear Dynamical Systems",
            "SC 602": "Control of Nonlinear Dynamical Systems",
            "SC649": "Embedded Control and Robotics",
            "SC 649": "Embedded Control and Robotics",
            "SC655": "Random Processes in Learning and Control",
            "SC 655": "Random Processes in Learning and Control",
            "SC664": "Active vibration and control",
            "SC 664": "Active vibration and control",
            "EE601": "Statistical signal Analysis",
            "EE 601": "Statistical signal Analysis",
            "EE603": "Digital Signal Processing",
            "EE 603": "Digital Signal Processing",
            "ME779": "Control Systems",
            "ME 779": "Control Systems",
            "SC625": "Systems Theory",
            "SC 625": "Systems Theory",
            "SC639": "Mathematical Structure for Control",
            "SC 639": "Mathematical Structure for Control",
            "SC624": "Differential Geometric Methods in Control",
            "SC 624": "Differential Geometric Methods in Control",
            "CS725": "Foundation of machine learning",
            "CS 725": "Foundation of machine learning",
            "CS728": "Organization of Web Information",
            "CS 728": "Organization of Web Information",
            "EE706": "Communication Networks",
            "EE 706": "Communication Networks",
        }
        
        # Look up course name
        clean_course_lookup = course_code.strip()
        course_name_val = course_names.get(clean_course_lookup, "")
        if not course_name_val:
            # Check case-insensitive
            for code, name in course_names.items():
                if code.lower().replace(" ", "") == clean_course_lookup.lower().replace(" ", ""):
                    course_name_val = name
                    break

        # Also update authors.yml
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

        with open(filepath, "w", encoding="utf-8") as md:
            md.write("---\n")
            md.write(f"title: {tag_name}\n")
            md.write(f"author: {author_key}\n")
            md.write(f"date: {full_date}\n")
            md.write("categories: [CourseReview]\n")
            md.write(f"tags: [{tag_name}]\n")
            md.write("render_with_liquid: false\n")
            md.write("auto_generated: true\n")
            md.write("---\n\n")

            # Clean and write Timestamp
            clean_ts = timestamp
            if " GMT" in clean_ts:
                clean_ts = clean_ts.split(" GMT")[0].strip()
            md.write("## Timestamp\n")
            md.write(f"{clean_ts}\n\n")
            
            # Print Posted by
            md.write(f"Posted by {student_name}\n\n")

            # Print Course Name
            if course_name_val:
                md.write("## Course Name\n")
                md.write(f"{course_name_val}\n\n")

            # Write other fields
            for field, value in row.items():
                # Skip fields we already handled or want to omit
                field_lower = field.lower().strip()
                if field_lower in ["timestamp", "course code", "job profile", "review"]:
                    continue
                # Also skip empty values to keep it clean
                if not value.strip():
                    continue
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

print("Markdown files generated successfully and stale files cleaned up.")
