---
layout: page
title: 4. Software Development Engineering (SDE)
permalink: /roadmap-sde/
---

<p class="lead" style="text-align: center; margin-bottom: 2rem;">
Focused purely on cracking top-tier software engineering placements (FAANG).
</p>

<script>
window.roadmapData = {
  "name": "SDE (FAANG)",
  "children": [
    {
      "name": "Semester 1",
      "children": [
        {"name": "SC Core 1"},
        {"name": "SC Core 2"},
        {"name": "CS 601: Algorithms (Elec)"},
        {"name": "CS Elective"}
      ]
    },
    {
      "name": "Semester 2",
      "children": [
        {"name": "SC Core 3"},
        {"name": "SC Core 4"},
        {"name": "SC 626: SysCon Lab"},
        {"name": "SC 694: Seminar"},
        {"name": "CS 631: Databases (Elec)"}
      ]
    },
    {
      "name": "Semester 3",
      "children": [
        {"name": "CS 744: Computing Systems (Elec)"},
        {"name": "SC Elective"},
        {"name": "MTP Stage 1"}
      ]
    },
    {
      "name": "Semester 4",
      "children": [
        {"name": "MTP Stage 2"}
      ]
    }
  ]
};
</script>

{% include d3-tree.html %}
