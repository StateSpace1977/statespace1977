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

<details class="roadmap-details">
<summary class="roadmap-summary">1. Pure Controls & Systems Theory</summary>
<div class="roadmap-content" markdown="1">

This path is for students aiming for PhDs, Core Engineering jobs (ISRO, DRDO, Aerospace), or hardcore theoretical research.

```mermaid
flowchart TD
    classDef core fill:#e0f2fe,stroke:#0369a1,color:#0369a1,stroke-width:2px,font-weight:bold;
    classDef elective fill:#dcfce7,stroke:#15803d,color:#15803d,stroke-width:2px;
    classDef milestone fill:#ffedd5,stroke:#c2410c,color:#c2410c,stroke-width:2px,stroke-dasharray: 5 5;

    subgraph Sem1 [Semester 1: Autumn]
        C1[SC 625: Systems Theory]:::core
        C2[SC 639: Math Structures]:::core
        E1[SC 613: Multivariable Control]:::elective
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 602: Nonlinear Systems]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2[SC 624: Geometric Methods]:::elective
        E3[SC 623: Optimal & Robust]:::elective
        
        C1 --> C3
        C2 --> E2
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[SC 618: Analytic Dynamics]:::elective
        E5[SC 617: Adaptive Control]:::elective
        M1[MTP Stage 1]:::milestone
        
        C3 --> E5
        E2 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

</div>
</details>

<details class="roadmap-details">
<summary class="roadmap-summary">2. Robotics & Autonomous Systems</summary>
<div class="roadmap-content" markdown="1">

For students targeting robotics startups, autonomous vehicle companies, and embedded systems.

```mermaid
flowchart TD
    classDef core fill:#e0f2fe,stroke:#0369a1,color:#0369a1,stroke-width:2px,font-weight:bold;
    classDef elective fill:#dcfce7,stroke:#15803d,color:#15803d,stroke-width:2px;
    classDef milestone fill:#ffedd5,stroke:#c2410c,color:#c2410c,stroke-width:2px,stroke-dasharray: 5 5;

    subgraph Sem1 [Semester 1: Autumn]
        C1[SC 625: Systems Theory]:::core
        C2[SC 639: Math Structures]:::core
        E1[SC 649: Embedded Control & Robotics]:::elective
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 602: Nonlinear Systems]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2[SC 635: Advanced Mobile Robotics]:::elective
        E3[SC 627: Motion Planning]:::elective
        
        C1 --> C3
        E1 --> E2
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[SC 634: Intro to Mobile Robotics]:::elective
        E5[SC 619: Lagrangian Systems]:::elective
        M1[MTP Stage 1]:::milestone
        
        E2 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

</div>
</details>

<details class="roadmap-details">
<summary class="roadmap-summary">3. AI, Machine Learning & Data Science</summary>
<div class="roadmap-content" markdown="1">

The most popular path for students targeting Data Scientist, ML Engineer, or Applied Scientist roles.

```mermaid
flowchart TD
    classDef core fill:#e0f2fe,stroke:#0369a1,color:#0369a1,stroke-width:2px,font-weight:bold;
    classDef elective fill:#dcfce7,stroke:#15803d,color:#15803d,stroke-width:2px;
    classDef milestone fill:#ffedd5,stroke:#c2410c,color:#c2410c,stroke-width:2px,stroke-dasharray: 5 5;
    classDef cross fill:#f3e8ff,stroke:#7e22ce,color:#7e22ce,stroke-width:2px;

    subgraph Sem1 [Semester 1: Autumn]
        C1[SC 655: Random Processes in ML]:::core
        C2[SC 625: Systems Theory]:::core
        E1["CS 725: Foundations of ML <br><i>(if eligible)</i>"]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 607: Optimization]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2[SC 646: Distributed Opt & ML]:::elective
        E3["CS 748: Advanced ML <br><i>(if eligible)</i>"]:::cross
        
        C1 --> E2
        E1 --> E3
        C3 --> E2
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4["CS 747: Reinforcement Learning <br><i>(if eligible)</i>"]:::cross
        E5["CS 728: Computer Vision <br><i>(if eligible)</i>"]:::cross
        M1[MTP Stage 1]:::milestone
        
        E3 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

</div>
</details>

<details class="roadmap-details">
<summary class="roadmap-summary">4. Software Development Engineering (SDE)</summary>
<div class="roadmap-content" markdown="1">

Focused purely on cracking top-tier software engineering placements (FAANG).

```mermaid
flowchart TD
    classDef core fill:#e0f2fe,stroke:#0369a1,color:#0369a1,stroke-width:2px,font-weight:bold;
    classDef elective fill:#dcfce7,stroke:#15803d,color:#15803d,stroke-width:2px;
    classDef milestone fill:#ffedd5,stroke:#c2410c,color:#c2410c,stroke-width:2px,stroke-dasharray: 5 5;
    classDef cross fill:#f3e8ff,stroke:#7e22ce,color:#7e22ce,stroke-width:2px;

    subgraph Sem1 [Semester 1: Autumn]
        C1[SC Core 1]:::core
        C2[SC Core 2]:::core
        E1["CS 601: Algorithms <br><i>(if eligible)</i>"]:::cross
        E2["CS Elective <br><i>(if eligible)</i>"]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC Core 3]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E3["CS 631: Databases <br><i>(if eligible)</i>"]:::cross
        
        E1 --> E3
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4["CS 744: Computing Systems <br><i>(if eligible)</i>"]:::cross
        E5[SC Elective]:::elective
        M1[MTP Stage 1]:::milestone
        
        E3 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

</div>
</details>

<details class="roadmap-details">
<summary class="roadmap-summary">5. Quantitative Finance & OR</summary>
<div class="roadmap-content" markdown="1">

For students aiming for HFT firms, Quant Analyst roles, or supply chain optimization.

```mermaid
flowchart TD
    classDef core fill:#e0f2fe,stroke:#0369a1,color:#0369a1,stroke-width:2px,font-weight:bold;
    classDef elective fill:#dcfce7,stroke:#15803d,color:#15803d,stroke-width:2px;
    classDef milestone fill:#ffedd5,stroke:#c2410c,color:#c2410c,stroke-width:2px,stroke-dasharray: 5 5;
    classDef cross fill:#f3e8ff,stroke:#7e22ce,color:#7e22ce,stroke-width:2px;

    subgraph Sem1 [Semester 1: Autumn]
        C1[SC 655: Random Processes]:::core
        C2[SC 639: Math Structures]:::core
        E1["IE 609: Math Optimisation <br><i>(if eligible)</i>"]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 607: Optimization]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2["IE 616: Game Theory <br><i>(if eligible)</i>"]:::cross
        E3["IE 708: Markov Decision Processes <br><i>(if eligible)</i>"]:::cross
        
        C1 --> E3
        E1 --> C3
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[SC 631: Games and Information]:::elective
        E5["IE 611: Stochastic Models <br><i>(if eligible)</i>"]:::cross
        M1[MTP Stage 1]:::milestone
        
        E2 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

</div>
</details>

<style>
.roadmap-details {
    margin-bottom: 1rem;
    border: 1px solid var(--card-border-color, #444);
    border-radius: 8px;
    background: transparent;
    overflow: hidden;
}
.roadmap-summary {
    padding: 1.25rem;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    background: transparent;
    color: inherit;
    list-style: none; /* Hide default arrow in some browsers */
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.3s ease;
}
/* Custom dropdown arrow for summary */
.roadmap-summary::after {
    content: '\25BC';
    font-size: 0.9rem;
    transition: transform 0.3s ease;
}
.roadmap-details[open] .roadmap-summary::after {
    transform: rotate(180deg);
}
.roadmap-details[open] .roadmap-summary {
    border-bottom: 1px solid var(--card-border-color, #444);
    background: rgba(128, 128, 128, 0.05);
}
.roadmap-summary:hover {
    background: rgba(128, 128, 128, 0.05);
}
/* Hide default details marker in webkit */
.roadmap-summary::-webkit-details-marker {
    display: none;
}
.roadmap-content {
    padding: 1.5rem;
    overflow-x: auto;
}
.mermaid svg {
    max-width: 100%;
    height: auto;
    background-color: var(--card-bg, #1e1e1e) !important;
    border-radius: 8px;
    padding: 16px;
}
@media (max-width: 768px) {
    .roadmap-summary {
        font-size: 0.95rem;
        padding: 1rem;
    }
    .roadmap-content {
        padding: 1rem;
    }
}
</style>
