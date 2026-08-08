---
layout: page
title: 2. Robotics & Autonomous Systems
permalink: /roadmap-robotics/
---

<p class="lead" style="text-align: center; margin-bottom: 2rem;">
For students targeting robotics startups, autonomous vehicle companies, and embedded systems.
</p>

<div class="timeline">
    <div class="timeline-item left">
        <div class="timeline-content">
            <span class="semester-badge">Semester 1</span>
            <h4>Core Courses (2)</h4>
            <ul>
                <li>SC 625: Systems Theory</li>
                <li>SC 639: Math Structures</li>
            </ul>
            <h4>Electives (2)</h4>
            <ul>
                <li>SC 649: Embedded Control & Robotics</li>
                <li>SC 634: Intro to Mobile Robotics</li>
            </ul>
        </div>
    </div>
    
    <div class="timeline-item right">
        <div class="timeline-content">
            <span class="semester-badge">Semester 2</span>
            <h4>Core Courses (2)</h4>
            <ul>
                <li>SC 602: Nonlinear Systems</li>
                <li>SC 607: Optimization</li>
            </ul>
            <h4>Mandatory Lab & Seminar</h4>
            <ul>
                <li>SC 626: SysCon Lab</li>
                <li>SC 694: Seminar</li>
            </ul>
            <h4>Electives (1)</h4>
            <ul>
                <li>SC 635: Advanced Mobile Robotics</li>
            </ul>
        </div>
    </div>

    <div class="timeline-item left">
        <div class="timeline-content">
            <span class="semester-badge">Semester 3</span>
            <h4>Electives (2)</h4>
            <ul>
                <li>SC 627: Motion Planning</li>
                <li>SC 619: Lagrangian Systems</li>
            </ul>
            <h4>Project</h4>
            <ul>
                <li>MTP Stage 1</li>
            </ul>
        </div>
    </div>

    <div class="timeline-item right">
        <div class="timeline-content">
            <span class="semester-badge">Semester 4</span>
            <h4>Project</h4>
            <ul>
                <li>MTP Stage 2</li>
            </ul>
        </div>
    </div>
</div>

<style>
.timeline {
    position: relative;
    max-width: 800px;
    margin: 40px auto;
    padding: 20px 0;
}
.timeline::after {
    content: '';
    position: absolute;
    width: 4px;
    background: var(--link-color, #007bff);
    top: 0;
    bottom: 100%;
    left: 50%;
    margin-left: -2px;
    border-radius: 4px;
    animation: growTree 1.5s ease-out forwards;
}
@keyframes growTree {
    to { bottom: 0; }
}

.timeline-item {
    padding: 10px 40px;
    position: relative;
    background-color: inherit;
    width: 50%;
    opacity: 0;
    transform: translateY(30px);
    animation: popIn 0.8s ease-out forwards;
}
.timeline-item.left {
    left: 0;
}
.timeline-item.right {
    left: 50%;
}
.timeline-item::after {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    right: -10px;
    background: var(--card-bg, #1e1e1e);
    border: 4px solid var(--link-color, #007bff);
    top: 20px;
    border-radius: 50%;
    z-index: 1;
    opacity: 0;
    animation: fadeIn 0.4s ease-out forwards;
}
.timeline-item.right::after {
    left: -10px;
}
@keyframes popIn {
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    to { opacity: 1; }
}
.timeline-item:nth-child(1), .timeline-item:nth-child(1)::after { animation-delay: 0.3s; }
.timeline-item:nth-child(2), .timeline-item:nth-child(2)::after { animation-delay: 0.8s; }
.timeline-item:nth-child(3), .timeline-item:nth-child(3)::after { animation-delay: 1.3s; }
.timeline-item:nth-child(4), .timeline-item:nth-child(4)::after { animation-delay: 1.8s; }

.timeline-content {
    padding: 20px 30px;
    background: var(--card-bg, #1e1e1e);
    position: relative;
    border-radius: 12px;
    border: 1px solid var(--card-border-color, #444);
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}
.timeline-content:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}
.semester-badge {
    position: absolute;
    top: -12px;
    background: var(--link-color, #007bff);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: bold;
}
.timeline-item.left .semester-badge { right: 20px; }
.timeline-item.right .semester-badge { left: 20px; }

.timeline-content h4 {
    margin-top: 15px;
    margin-bottom: 5px;
    font-size: 1.1rem;
    color: var(--heading-color);
}
.timeline-content h4:first-of-type {
    margin-top: 5px;
}
.timeline-content ul {
    margin-top: 5px;
    padding-left: 20px;
    list-style-type: disc;
}
.timeline-content li {
    font-size: 0.95rem;
    margin-bottom: 4px;
    color: var(--text-color);
}

/* Mobile responsive */
@media screen and (max-width: 768px) {
    .timeline::after {
        left: 20px;
    }
    .timeline-item {
        width: 100%;
        padding-left: 50px;
        padding-right: 15px;
    }
    .timeline-item.left, .timeline-item.right {
        left: 0;
    }
    .timeline-item::after, .timeline-item.right::after {
        left: 10px;
    }
    .timeline-item.left .semester-badge, .timeline-item.right .semester-badge {
        left: 20px;
        right: auto;
    }
}
</style>
