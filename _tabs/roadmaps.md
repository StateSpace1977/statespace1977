---
title: Course Roadmaps
icon: fas fa-route
order: 4
mermaid: true
---

# SysCon M.Tech Curriculum Rules 📜

Before diving into the domain pathways, here is the strict structure you must follow to complete your M.Tech at SysCon:

> [!IMPORTANT]
> - **4 Core Courses** (Typically completed in Sem 1 & 2)
> - **5 Department Electives** (Spread across Sem 1 to 3)
> - **1 Lab Course** (SC 626 in Sem 2)
> - **1 Seminar** (SC 694 in Sem 2)
> - **MTP (Master's Thesis Project)** (Starts in Sem 3, concludes in Sem 4)

---

# 1. Pure Controls & Systems Theory 🤖
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

---

# 2. Robotics & Autonomous Systems 🦾
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

---

# 3. AI, Machine Learning & Data Science 🧠
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
        E1[CS 725: Foundations of ML]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 607: Optimization]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2[SC 646: Distributed Opt & ML]:::elective
        E3[CS 748: Advanced ML]:::cross
        
        C1 --> E2
        E1 --> E3
        C3 --> E2
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[CS 747: Reinforcement Learning]:::cross
        E5[CS 728: Computer Vision]:::cross
        M1[MTP Stage 1]:::milestone
        
        E3 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

---

# 4. Software Development Engineering (SDE) 💻
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
        E1[CS 601: Algorithms]:::cross
        E2[CS 699: Software Lab]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC Core 3]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E3[CS 631: Databases]:::cross
        
        E1 --> E3
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[CS 744: Computing Systems]:::cross
        E5[SC Elective]:::elective
        M1[MTP Stage 1]:::milestone
        
        E3 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

---

# 5. Quantitative Finance & OR 📈
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
        E1[IE 609: Math Optimisation]:::cross
    end

    subgraph Sem2 [Semester 2: Spring]
        C3[SC 607: Optimization]:::core
        C4[SC 626: SysCon Lab]:::core
        S[SC 694: Seminar]:::milestone
        E2[IE 616: Game Theory]:::cross
        E3[IE 708: Markov Decision Processes]:::cross
        
        C1 --> E3
        E1 --> C3
    end

    subgraph Sem3 [Semester 3: Autumn]
        E4[SC 631: Games and Information]:::elective
        E5[IE 611: Stochastic Models]:::cross
        M1[MTP Stage 1]:::milestone
        
        E2 --> E4
    end

    subgraph Sem4 [Semester 4: Spring]
        M2[MTP Stage 2]:::milestone
        M1 --> M2
    end
```

<style>
/* Improve readability of Mermaid SVGs in dark mode */
.mermaid svg {
    max-width: 100%;
    height: auto;
    background-color: var(--card-bg) !important;
    border-radius: 8px;
    padding: 16px;
    border: 1px solid var(--card-border-color);
}
</style>
