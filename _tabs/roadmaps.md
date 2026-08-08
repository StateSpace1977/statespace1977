---
title: Course Roadmaps
icon: fas fa-route
order: 4
mermaid: true
---

## M.Tech Curriculum Guidelines

The M.Tech program in Systems and Control Engineering requires students to complete a structured set of core and elective courses alongside a Master's Thesis Project. The curriculum is designed to provide both a strong theoretical foundation and specialized domain expertise.

### Degree Requirements
To successfully graduate, students must complete the following:

- **Core Courses (4):** Foundational coursework typically completed during Semesters 1 and 2.
- **Department Electives (5):** Specialized courses chosen based on your selected domain pathway, distributed across Semesters 1 to 3.
- **Laboratory Course (1):** SC 626 (Systems and Control Laboratory), taken in Semester 2.
- **Seminar (1):** SC 694, taken in Semester 2.
- **Master's Thesis Project (MTP):** A two-stage research project starting in Semester 3 and concluding in Semester 4.

---

<div class="roadmap-grid">
    <a href="/roadmap-pure-controls/" class="roadmap-card">
        <div class="card-icon"><i class="fas fa-cogs"></i></div>
        <div class="card-content">
            <h3>1. Pure Controls & Systems Theory</h3>
            <p>For PhDs, Core Engineering (ISRO/DRDO), and theoretical research.</p>
        </div>
    </a>

    <a href="/roadmap-robotics/" class="roadmap-card">
        <div class="card-icon"><i class="fas fa-robot"></i></div>
        <div class="card-content">
            <h3>2. Robotics & Autonomous Systems</h3>
            <p>Targeting robotics startups and autonomous vehicle companies.</p>
        </div>
    </a>

    <a href="/roadmap-aiml/" class="roadmap-card">
        <div class="card-icon"><i class="fas fa-brain"></i></div>
        <div class="card-content">
            <h3>3. AI, Machine Learning & Data Science</h3>
            <p>The path for Data Scientists, ML Engineers, and Applied Scientists.</p>
        </div>
    </a>

    <a href="/roadmap-sde/" class="roadmap-card">
        <div class="card-icon"><i class="fas fa-laptop-code"></i></div>
        <div class="card-content">
            <h3>4. Software Development Engineering</h3>
            <p>Focused purely on cracking top-tier software engineering placements.</p>
        </div>
    </a>

    <a href="/roadmap-quant/" class="roadmap-card">
        <div class="card-icon"><i class="fas fa-chart-line"></i></div>
        <div class="card-content">
            <h3>5. Quantitative Finance & OR</h3>
            <p>For students aiming for HFT firms and Quant Analyst roles.</p>
        </div>
    </a>
</div>

<style>
.roadmap-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin-top: 2rem;
    margin-bottom: 3rem;
}
.roadmap-card {
    display: flex;
    align-items: center;
    background: var(--card-bg, #1e1e1e);
    border: 1px solid var(--card-border-color, #444);
    border-radius: 12px;
    padding: 1.5rem;
    text-decoration: none !important;
    color: inherit;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}
.roadmap-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    border-color: var(--link-color, #007bff);
}
.roadmap-card:hover h3 {
    color: var(--link-color, #007bff);
}
.card-icon {
    font-size: 2.5rem;
    color: var(--link-color, #007bff);
    margin-right: 1.5rem;
    min-width: 60px;
    text-align: center;
    transition: transform 0.3s ease;
}
.roadmap-card:hover .card-icon {
    transform: scale(1.1);
}
.card-content h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.25rem;
    font-weight: 700;
    transition: color 0.3s ease;
}
.card-content p {
    margin: 0;
    font-size: 0.95rem;
    color: var(--text-muted-color, #888);
    line-height: 1.4;
}
@media (min-width: 768px) {
    .roadmap-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
</style>
