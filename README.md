# JanCohort_PS5
skill gap analysis
# Problem Statement 5: Skill Gap Analysis Engine

##  Overview
This project implements a **Skill Gap Analysis Engine** that helps job seekers understand the gap between their **current skills** and a **target role**, along with readiness scoring, learning time estimation, and AI-assisted roadmap generation.

The system combines:
- **Deterministic, rule-based scoring logic**
- **Skill taxonomy and weighted importance**
- **Optional LLM-based roadmap & resource generation**
- **FastAPI backend for real-time analysis**

---

##  Objectives
- Identify **matching and missing skills**
- Compute **weighted skill gap percentage**
- Calculate **readiness score**
- Estimate **learning time**
- Predict **transition success rate**
- Generate **AI-powered learning roadmap** (Bonus)

---

##  Features Implemented

###  Core (Deterministic)
- Skill matching using **role-specific skill importance**
- Weighted gap calculation (not simple count-based)
- Readiness score using difficulty, market value & importance
- Learning time estimation based on skill difficulty
- Input validation using JSON Schema

###  Bonus (AI-Assisted)
- Gemini LLM integration for:
  - Learning roadmap generation
  - Resource recommendations
- Hybrid output:
  - Deterministic scores + AI explanations
--Added Comments
---


