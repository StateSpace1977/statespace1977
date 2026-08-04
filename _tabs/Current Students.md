---
# the default layout is 'page'
icon: fas fa-address-book
order: 5
---

<script>
function selectStudentTab(targetId) {
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
    <label class="year-filter-label" for="student-intake-select">Select Program / Intake:</label>
        <select id="student-intake-select" class="year-select-dropdown" onchange="selectStudentTab(this.value)">
      <option value="mtech-2026">2026 Intake (18)</option>
      <option value="mtech-2025">2025 Intake (25)</option>
      <option value="mtech-2024">2024 Intake (4)</option>
      <option value="idddp">IDDDP (3)</option>
      <option value="all">All Students (50)</option>
    </select>

        <div class="quick-year-pills">
      <button class="quick-pill active" data-target="mtech-2026" onclick="selectStudentTab('mtech-2026')">2026 Intake</button>
      <button class="quick-pill" data-target="mtech-2025" onclick="selectStudentTab('mtech-2025')">2025 Intake</button>
      <button class="quick-pill" data-target="mtech-2024" onclick="selectStudentTab('mtech-2024')">2024 Intake</button>
      <button class="quick-pill" data-target="idddp" onclick="selectStudentTab('idddp')">IDDDP</button>
      <button class="quick-pill" data-target="all" onclick="selectStudentTab('all')">All</button>
    </div>
  </div>

    <div id="mtech-2026" class="tab-pane active">
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Mahendra.jpg" alt="Mahendra" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Mahendra</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Control system
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Electronic</span>
      <a href="mailto:mahendranegi123456@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Sagar Kumar Wadhwani.jpg" alt="Sagar Kumar Wadhwani" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Sagar Kumar Wadhwani</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> AI ML
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI ML</span>
      <a href="mailto:26m2004@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Kingshuk Pal.jpg" alt="Kingshuk Pal" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Kingshuk Pal</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Exploring Latest Technology, Playing Video Games, Watching Football
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI/ML</span>
      <a href="mailto:26M2005@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Kiran Gullapalli.jpg" alt="Kiran Gullapalli" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Kiran Gullapalli</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Control Systems, AI/ML
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI/ML</span>
      <a href="mailto:26M2006@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Aryan Patel.jpg" alt="Aryan Patel" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Aryan Patel</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> AI/ML , People , Exploring ,Good Vibes
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AiML</span>
      <a href="mailto:26M2007@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Rishita Parashar.jpg" alt="Rishita Parashar" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rishita Parashar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> coding , problem solving
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI ML</span>
      <a href="mailto:26M2009@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Anurag Pandey.jpg" alt="Anurag Pandey" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Anurag Pandey</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> ML, robotics, automation
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: ML, Control & Automation</span>
      <a href="mailto:26M2011@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Adithya Sriraman.jpg" alt="Adithya Sriraman" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Adithya Sriraman</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> RTL Design and Verification, Embedded Software, SoC, ASIC Design, Python SystemVerilog/Verilog, C++/C.
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: System and Control, Electronics oriented</span>
      <a href="mailto:adithyasriraman12@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Shahan Malik.jpg" alt="Shahan Malik" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Shahan Malik</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Gym,football,movies
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Intelligent autonomous system</span>
      <a href="mailto:shahanmalikc@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Tanishq Sahu.jpg" alt="Tanishq Sahu" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Tanishq Sahu</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Playing badminton, chess, beatboxing
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: ML, VLSI</span>
      <a href="mailto:sahutanishq14@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Shri Keshavinee Ramachandran.jpg" alt="Shri Keshavinee Ramachandran" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Shri Keshavinee Ramachandran</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Basketball, Swimming
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Robotics</span>
      <a href="mailto:26M2019@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Amitvikram Sanjeev Pujar.jpg" alt="Amitvikram Sanjeev Pujar" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Amitvikram Sanjeev Pujar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Yoga, Watching Podcast
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Deep Learning</span>
      <a href="mailto:26M2020@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Lakshay Wadhwani.jpg" alt="Lakshay Wadhwani" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Lakshay Wadhwani</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Sports, Video Games, Shows & Movies
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: AI & Robotics</span>
      <a href="mailto:26M2021@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Karan prasad Ahirwar.jpg" alt="Karan prasad Ahirwar" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Karan prasad Ahirwar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> To learn about Hardware design ,FPGA programming, and excited to
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Embedded system and VLSI Design</span>
      <a href="mailto:26m2022@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Rahul Singh.jpg" alt="Rahul Singh" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rahul Singh</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Electrical vehicle, Mechatronics
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control Systems, Automation, Robotics</span>
      <a href="mailto:rahul.singh.31910@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Hardik Jain.jpg" alt="Hardik Jain" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Hardik Jain</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Robotics, Artificial Intelligence, Control
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Mechanical Engineering</span>
      <a href="mailto:26M2026@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Sandip Biswas.jpg" alt="Sandip Biswas" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Sandip Biswas</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Modern Control System
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: System and Control</span>
      <a href="mailto:sandipbiswas101197@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>

<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/26/Santhosh Krishna.jpg" alt="Santhosh Krishna" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Santhosh Krishna</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Trekking, Paragliding, Adventure Sports, Badminton, Legos, Motorsport
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Gas Turbines & Naval Control Systems</span>
      <a href="mailto:mskrishna.1996@gmail.com" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
  </div>
</div>

  <div id="mtech-2025" class="tab-pane">
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Adarsh Korde.jpg" alt="Adarsh Korde" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Adarsh Korde</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof.Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Robotics, Volleyball
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Embodied AI</span>
      <a href="mailto:adarsh02@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Shubh Shah.jpg" alt="Shubh Shah" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Shubh Shah</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:shubhshah@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/SARMAN SINGH.jpg" alt="SARMAN SINGH" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">SARMAN SINGH</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Approximate Multiagent Reinforcement Learning for Urban Mobility. <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Playing Basketball,Cricket and Badminton
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Embedded Systems,Machine Learning and Software Engineering</span>
      <a href="mailto:sarmansingh@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Soham Banerjee.jpg" alt="Soham Banerjee" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Soham Banerjee</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Arpita Maam <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Control of Bipeds <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Building stuffs, reading stories, playing games
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Robotics and Control</span>
      <a href="mailto:soham_syscon@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Rehan Khan.jpg" alt="Rehan Khan" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rehan Khan</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Machine Learning</span>
      <a href="mailto:25m2006@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Md Saif Ali.jpg" alt="Md Saif Ali" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Md Saif Ali</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Sukumar Srikant <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Exploring the Cosmos
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Machine Learning & Deep Learning,  Generative AI & NLP, Computer Vision, Cloud & IOT</span>
      <a href="mailto:mdsaifali@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Vinay Bujja.jpg" alt="Vinay Bujja" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Vinay Bujja</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Professor Debasish Chatterjee <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Optimization <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:vinaybujja@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Tejash Raj.jpg" alt="Tejash Raj" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Tejash Raj</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Table Tennis , Reading
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control</span>
      <a href="mailto:raj_tejash@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Pamanji Nagaraju.jpg" alt="Pamanji Nagaraju" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Pamanji Nagaraju</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Raj Anguluri <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Raj Anguluri <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Teaching & academic content creation
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:25m2011@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/MADDILI AKHIL.jpg" alt="MADDILI AKHIL" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">MADDILI AKHIL</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof.Rajasekhar Anguluri <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Stochastic Interpolants for diffusion models. <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: CSE</span>
      <a href="mailto:akhil12@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Arunodaya devi.jpg" alt="Arunodaya devi" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Arunodaya devi</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Local motion planning for collaborative multi-robot manipulation of deformable objects <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Playing chess
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Robotics and Automation</span>
      <a href="mailto:arunodaya@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/PRIYA BISWAS.jpg" alt="PRIYA BISWAS" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">PRIYA BISWAS</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> arpita sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:priyabiswas@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Rahul Kumar.jpg" alt="Rahul Kumar" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rahul Kumar</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Dr.Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Machine learning / Applied AI</span>
      <a href="mailto:rahulkumarh3@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/LOHITH NAIK R.jpg" alt="LOHITH NAIK R" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">LOHITH NAIK R</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:lohithnaik_syscon@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Arun P Madhu.jpg" alt="Arun P Madhu" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Arun P Madhu</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Reading, PC gaming,
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control and Perception on UAVs</span>
      <a href="mailto:arunpmadhu@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Allan Joseph.jpg" alt="Allan Joseph" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Allan Joseph</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Reading and fitness
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:allanjoseph@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Amit.jpg" alt="Amit" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Amit</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Dr. Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Watching movies, cycling, reading
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control</span>
      <a href="mailto:amitphogat34@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Ajay J.jpg" alt="Ajay J" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Ajay J</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Collision avoidance on autonomous vessel <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Badminton, Cricket
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:jajay602@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Bharat Kandpal.jpg" alt="Bharat Kandpal" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Bharat Kandpal</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof Arpita Sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Squash, Table Tennis, Hiking
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Mechanical Engineering</span>
      <a href="mailto:bharatk96@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Mandar Maruti Jondhale.jpg" alt="Mandar Maruti Jondhale" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Mandar Maruti Jondhale</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Navin Khaneja <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Robust control of quantum systems <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Fitness, Volleyball
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:mandarjondhale@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Rakesh Krushna Joshi.jpg" alt="Rakesh Krushna Joshi" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rakesh Krushna Joshi</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Leena Vachhani <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Space exploration, Meditation, studying ancient history and Indian society, watching sci-fi and romantic drama films.
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Machine Learning, Computer Vision, Deep Learning, Natural Language Processing</span>
      <a href="mailto:rakeshjoshi@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Avi chourasiya.jpg" alt="Avi chourasiya" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Avi chourasiya</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof.arpita sinha <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Modelling
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Machine learning</span>
      <a href="mailto:25M2027@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Mihir Kalal.jpg" alt="Mihir Kalal" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Mihir Kalal</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Navin Khaneja <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Robust control of quantum systems <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Badminton, road trips, treks
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: CSE</span>
      <a href="mailto:mihir.kalal@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Ayush Vats.jpg" alt="Ayush Vats" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Ayush Vats</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Software Development, Machine Learning
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Computer Science & Engineering</span>
      <a href="mailto:25m2029@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/25/Sai Teja Lodagala.jpg" alt="Sai Teja Lodagala" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Sai Teja Lodagala</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Rajasekhar Anguluri <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Audio Signal Processing(Demixing and Remixing of Songs and Individual Stems) <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Playing Chess and Pool.
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Electronics and communication</span>
      <a href="mailto:saiteja@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>
  </div>

  <div id="mtech-2024" class="tab-pane">
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Rohit Patil.jpg" alt="Rohit Patil" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Rohit Patil</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Vivek Natarajan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> PDE Modelling and MPC <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Running, Marathons
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Controls & Robotics</span>
      <a href="mailto:24m0135@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Carlyn Medona.jpg" alt="Carlyn Medona" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Carlyn Medona</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Vivek Natarajan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Magnetic Bearings <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Sleeping, Eating and Surfing internet
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control systems and Signal Processing</span>
      <a href="mailto:24m2018@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Shailaja Manchala.jpg" alt="Shailaja Manchala" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Shailaja Manchala</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Ravi. N. Banavar <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> nan
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: nan</span>
      <a href="mailto:shailajamanchala@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/24/Narendra Muley.jpg" alt="Narendra Muley" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Narendra Muley</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> nan <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Books, History, Geo-politics
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Control Systems, Power Electronics and Machines</span>
      <a href="mailto:24m2020@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>
  </div>

  <div id="idddp" class="tab-pane">
<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/others/Shreyas N B.jpg" alt="Shreyas N B" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Shreyas N B</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Ravi Banavar <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Robust Least-Squares Optimization and Data Driven Control <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Books, Volleyball & Badminton, Travel
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Nonlinear control, Differential geometry, Robotics</span>
      <a href="mailto:shreyasnb@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/others/Vaibhav Upadhyay.jpg" alt="Vaibhav Upadhyay" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Vaibhav Upadhyay</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Debasish Chatterjee <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Constrained feedback synthesis for nonlinear control systems <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Trekking, photography, and ancient Indian philosophy
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Applied mathematics</span>
      <a href="mailto:vaibhav.u@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>


<div class="student-card" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; padding: 20px; margin-bottom: 16px; border: 1px solid var(--card-border-color, rgba(0,0,0,0.08)); border-radius: 12px; background: var(--card-bg, rgba(255,255,255,0.02)); box-shadow: 0 2px 8px rgba(0,0,0,0.02); transition: transform 0.2s ease, box-shadow 0.2s ease;">
  <div style="flex: 0 0 120px; width: 120px;">
    <img src="/assets/students/others/Arkadeep Saha.jpg" alt="Arkadeep Saha" onerror="this.onerror=null; this.src='/assets/avatar/avatar.png';" style="width: 100%; height: auto; display: block; border-radius: 4px;">
  </div>
  <div style="flex: 1; min-width: 240px; display: flex; flex-direction: column; gap: 6px;">
    <span style="font-size: 1.25em; font-weight: 700; color: var(--heading-color);">Arkadeep Saha</span>
    <div style="font-size: 0.9em; line-height: 1.4;">
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Guide:</span> Prof. Ravi Banavar <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Thesis:</span> Nonlinear state estimation in aerial robotics <br>
      <span style="color: var(--text-muted-color, #888); font-weight: 500;">Interests:</span> Cinephilia, Reading, Painting
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; align-items: center;">
      <span style="background-color: var(--tag-bg, rgba(52, 152, 219, 0.12)); color: var(--link-color, #3498db); padding: 3px 10px; border-radius: 20px; font-size: 0.8em; font-weight: 600;">Domain: Robotics, State Estimation, SLAM</span>
      <a href="mailto:22b1270@iitb.ac.in" style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; background: var(--link-color, #007bff); color: var(--card-bg, #fff) !important; border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: 600;">
        <span>✉</span> Email
      </a>
    </div>
  </div>
</div>
  </div>
</div>