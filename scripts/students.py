import pandas as pd
import os

csv_file = "csv_dropbox/students.csv"
output_file = "_tabs/Current Students.md"
base_path = "/statespace1977/assets/students"

if not os.path.exists(csv_file):
    print(f"No CSV found at {csv_file}, skipping.")
    exit(0)

df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip()

blocks_by_folder = {
    "others": [],
    "24": [],
    "25": []
}

def get_folder(roll):
    roll = str(roll).strip()
    if roll.startswith("24"):
        return "24"
    elif roll.startswith("25"):
        return "25"
    else:
        return "others"

for _, row in df.iterrows():
    name = str(row["Name"]).strip()
    roll = str(row["Roll Number"]).strip()
    advisor = str(row["M.Tech/PhD Advisor"]).strip()
    thesis = str(row["M.Tech/PhD Thesis Topic"]).strip()
    interests = str(row["Hobbies & Interests"]).strip()
    domain = str(row["Domain"]).strip()
    email = str(row["IITB Email"]).strip()

    folder = get_folder(roll)
    image_path = f"{base_path}/{folder}/{name}.jpg"

    block = f"""
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="{image_path}" alt="{name}" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">{name}</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> {advisor} <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> {thesis} <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> {interests}
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: {domain}</span>
      <a href="mailto:{email}" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>
"""
    blocks_by_folder[folder].append(block)

markdown_content = """---
# the default layout is 'page'
icon: fas fa-address-book
order: 5
---

<details >
<summary><strong>🎓🎓 IDDDP</strong></summary>

<br>
""" + "\n".join(blocks_by_folder["others"]) + """
</details>

---

<details >
<summary><strong>🎓 M.Tech 2024 Intake</strong></summary>

<br>
""" + "\n".join(blocks_by_folder["24"]) + """
</details>

---

<details >
<summary><strong>🎓 M.Tech 2025 Intake</strong></summary>

<br>
""" + "\n".join(blocks_by_folder["25"]) + """
</details>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Current Students.md generated successfully!")
