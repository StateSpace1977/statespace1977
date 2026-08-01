---
# the default layout is page
icon: fas fa-address-book
order: 4
---

<script>
function selectAlumniTab(targetId) {
  const container = document.querySelector(".tabs-wrapper");
  if (!container) return;
  container.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
  
  const dropdown = container.querySelector(".year-select-dropdown");
  if (dropdown && dropdown.value !== targetId) {
    dropdown.value = targetId;
  }
  
  container.querySelectorAll(".quick-pill").forEach(pill => {
    if (pill.getAttribute("data-target") === targetId) {
      pill.classList.add("active");
    } else {
      pill.classList.remove("active");
    }
  });

  if (targetId === "all") {
    container.querySelectorAll(".tab-pane").forEach(p => p.classList.add("active"));
  } else {
    const target = container.querySelector("#" + targetId);
    if (target) target.classList.add("active");
  }
}
</script>

<div class="tabs-wrapper">
  <div class="year-filter-bar">
    <label class="year-filter-label" for="alumni-year-select">Select Year / Batch:</label>
    <select id="alumni-year-select" class="year-select-dropdown" onchange="selectAlumniTab(this.value)">
      <option value="batch-2025">Batch 2025 (9)</option>
      <option value="batch-2024">Batch 2024 (27)</option>
      <option value="batch-2023">Batch 2023 (7)</option>
      <option value="batch-2022">Batch 2022 (1)</option>
      <option value="batch-2021">Batch 2021 (3)</option>
      <option value="batch-2020">Batch 2020 (1)</option>
      <option value="batch-2019">Batch 2019 (2)</option>
      <option value="batch-2018">Batch 2018 (3)</option>
      <option value="batch-2017">Batch 2017 (1)</option>
      <option value="batch-2016">Batch 2016 (1)</option>
      <option value="batch-2014">Batch 2014 (2)</option>
      <option value="batch-2005">Batch 2005 (1)</option>
      <option value="batch-1999">Batch 1999 (1)</option>
      <option value="batch-n/a">Other Alumni (2)</option>
      <option value="all">All Alumni (61)</option>
    </select>

    <div class="quick-year-pills">
      <button class="quick-pill active" data-target="batch-2025" onclick="selectAlumniTab('batch-2025')">2025</button>
      <button class="quick-pill" data-target="batch-2024" onclick="selectAlumniTab('batch-2024')">2024</button>
      <button class="quick-pill" data-target="batch-2023" onclick="selectAlumniTab('batch-2023')">2023</button>
      <button class="quick-pill" data-target="all" onclick="selectAlumniTab('all')">All</button>
    </div>
  </div>

  <div id="batch-2025" class="tab-pane active">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Aditya Ashribad</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> L&T Precision Engineering & Systems
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Amit Kumar</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Nanyang Technological University (NTU), Singapore
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Ashmita Roy</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> IUCAA
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Nallae Gowtham kumarswamy</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Qualcomm
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Oza Harsh Mukundbhai</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> KPIT Technologies
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Siddhartha Ganguly</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Kyoto University
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Souvik Das</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Uppsala University
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Sudipta Chattopadhyay</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> SEDEMAC
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Vipul Notani</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2025 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Mathworks
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2025</span>
    </div>
</div>
  </div>

  <div id="batch-2024" class="tab-pane">
  </div>

  <div id="batch-2024" class="tab-pane">
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Anuj Yadav.jpg" alt="Anuj Yadav" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Anuj Yadav</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:anuj.yadav@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Anupam.jpg" alt="Anupam" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Anupam</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Srikant Sukumar <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Trajectory mapping on Moon terrain <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Arts & Craft, writing
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Software domain</span>
      <a href="mailto:24m2015@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Arjun Sadananda</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> nsideFPV
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Ashutosh Jindal</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Post-Doc, University of Groningen
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Chanakya vihar Challa.jpg" alt="Chanakya vihar Challa" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Chanakya vihar Challa</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Sukumar Srikant <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Quadcopter Orientation Control (3-DOF) <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:24m2028@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Chandra Vikas.jpg" alt="Chandra Vikas" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Chandra Vikas</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:24m2030@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Chetan Teli</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Fuji Electric India pvt. Ltd.
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Devyansh Shukla</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> National Stock Exchange
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Jatinkumar.jpg" alt="Jatinkumar" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Jatinkumar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof vivek natrajan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Suspension for vehicles <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Yoga
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control system</span>
      <a href="mailto:24m2021@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Kadapalla Nithin Kumar.jpg" alt="Kadapalla Nithin Kumar" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Kadapalla Nithin Kumar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Gruve <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Leena Vachhani <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> RL for UAV based localization application <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Software & Robotics</span>
      <a href="mailto:nithinkumar@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Maitreyee Dutta</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Tokyo Institute of Technology
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Manauwar Alam</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Inspecity Space Labs
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Mohammed Mairajuddin Musharraf</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Micron
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Mukesh Kumar</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> IDDDP <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Ph.D. at Georgia Institute of Technology
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">PALLAVI SINHA</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Halliburton
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Paras Pandey.jpg" alt="Paras Pandey" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Paras Pandey</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Vivek Natarajan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Control System Design of Active Magnetic Bearing for Marine Centrifugal Pumps <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Running, squash, badminton, reading
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Marine Engineering, Control & Automation</span>
      <a href="mailto:24m2022@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Prabhat Patel.jpg" alt="Prabhat Patel" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Prabhat Patel</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Sukumar shrikant <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Lunar navigation system <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Solving DSA , Singing and playing Cricket
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI& ML, Data science. Software Engineering</span>
      <a href="mailto:24m2005@iitb.ac" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Prashik Patil.jpg" alt="Prashik Patil" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Prashik Patil</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Visa <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Prof. Leena Vachhani <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Quantum computing and its applications in robotics <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Running, Swimming, Exploring Art and Food
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Software Engineering</span>
      <a href="mailto:24m2014@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Ramavath Sai Dinesh</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Airbus
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Rohit kumar.jpg" alt="Rohit kumar" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rohit kumar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Kas Global <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Sukumar srikant sir <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Relative position and orientation of spacecraft in space using cnn <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Playing cricket, listening to music and traveling
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Associate ai researcher</span>
      <a href="mailto:24m2029@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Sambeda Sarkar</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Ola Electric
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Shreyam Mishra</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> IDDDP <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> PhD at the University of Pennsylvania
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Siddhartha Ganguly</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Postdoctoral researcher and Professor at the Kyoto University, Japan.
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Smit Kesaria</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> - -
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Souvik Das</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> NEC Japan
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Sudip Mondal</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Accenture
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/vinayak bhardwaj.jpg" alt="vinayak bhardwaj" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">vinayak bhardwaj</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span>  2024 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Eaton <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Advisor:</span> Arpita sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Human–Robot Collaboration Framework for Object Transportation <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Tinkering, learning new things, gaming, and anime
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2024</span>
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control and Robotics</span>
      <a href="mailto:24m2007@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>
  </div>

  <div id="batch-2023" class="tab-pane">
  </div>

  <div id="batch-2023" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Akash Deep Arya</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> PGET, Adani Green Energy Pvt Ltd
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Manuraj PM</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Engineer-II, RnD software dept, ideaforge
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Mirza Aman Baig</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Asst Managar, Systems Engineering, Suzlon Energy Ltd
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Muthyala Anjali</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Flight COntrols Development Engineer, Airbus India
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Rohan More</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Research Specialist, Connected Digital Systems Pvt Ltd
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Sayan Ray</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Software Engg, Bajaj RnD
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Shashank Deshpande</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> IDDDP <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2023 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Grad Student, MIT
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2023</span>
    </div>
</div>
  </div>

  <div id="batch-2022" class="tab-pane">
  </div>

  <div id="batch-2022" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Anuj Sanjay Vora</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2022 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Postdoc at TU Delft, Netherlands
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2022</span>
    </div>
</div>
  </div>

  <div id="batch-2021" class="tab-pane">
  </div>

  <div id="batch-2021" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Dr. Kiran Kumari</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2021 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Indian Institute of Science
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2021</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">MALLULA YASODA VENKATA KRISHNA TEJA</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2021 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> IFM ENGINEERING PVT LTD
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2021</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">YASODA VENKATA KRISHNA TEJA MALLULA</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2021 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Qualcomm
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2021</span>
    </div>
</div>
  </div>

  <div id="batch-2020" class="tab-pane">
  </div>

  <div id="batch-2020" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Saurabh Dhamne</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2020 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Dover corporation
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2020</span>
    </div>
</div>
  </div>

  <div id="batch-2019" class="tab-pane">
  </div>

  <div id="batch-2019" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Harivardhan Geddada</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2019 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> ABB India
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2019</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Kshitij Kadam</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2019 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Datamatics
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2019</span>
    </div>
</div>
  </div>

  <div id="older-batches" class="tab-pane">
<h3>Batch 2018</h3>
  </div>

  <div id="batch-2018" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Anurag Kashyap</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2018 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> PHILIPS HEALTHCARE
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2018</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Kawde rohit rajendra</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2018 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Ebara Corporation
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2018</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Kishan Kumar</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2018 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Mercedes-Benz Research and Development India Pvt Ltd
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2018</span>
    </div>
</div>

<h3>Batch 2017</h3>
  </div>

  <div id="batch-2017" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Rakesh R Warier</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2017 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> National Institute of Calicut
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2017</span>
    </div>
</div>

<h3>Batch 2016</h3>
  </div>

  <div id="batch-2016" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Sarat Chandra Nagavarapu</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2016 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Agency for Science, Technology and Research (A*STAR), Singapore
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2016</span>
    </div>
</div>

<h3>Batch 2014</h3>
  </div>

  <div id="batch-2014" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Ajay Singh</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> MTech <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2014 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Smartmicrowave sensors GmbH
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2014</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">SOUMYA RANJAN SAHOO</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2014 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> INDIAN INSTITUTE OF TECHNOLOGY KANPUR
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2014</span>
    </div>
</div>

<h3>Batch 2005</h3>
  </div>

  <div id="batch-2005" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Dhananjay Balu Talange</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 2005 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> DNA Precision Works
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 2005</span>
    </div>
</div>

<h3>Batch 1999</h3>
  </div>

  <div id="batch-1999" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">S Jayakumar</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> 1999 <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Independent consultant
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch 1999</span>
    </div>
</div>

<h3>Other Alumni</h3>
  </div>

  <div id="batch-n/a" class="tab-pane">
<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Prashant Patil</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Research Engineer, General Electric
    </div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch N/A</span>
    </div>
</div>

<div class="student-card" style="display: flex; flex-direction: column; padding: 20px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color); margin-bottom: 12px;">Shubhangi Nema</span>
    <div style="font-size: 0.9em; line-height: 1.5;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Degree:</span> PhD <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Batch:</span> N/A <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Organisation:</span> Research and Innovation Park, IIT Delhi (Principal Scientist)
    </div>
</div>

    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Batch N/A</span>
    </div>
</div>
  </div>
</div>
  </div>
</div>