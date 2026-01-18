from typing import List, Tuple
from math import ceil
from app.data import SKILLS, ROLE_SKILLS


# ================================
# 1. MATCHING & MISSING SKILLS
# ================================
def get_matching_and_missing_skills(
    candidate_skills: List[str],
    target_role: str,
    target_skills: list
) -> Tuple[List[str], List[str]]:

    required_skills=set(target_skills)
    candidate_set = {s for s in candidate_skills if s in required_skills}

    matching = sorted(candidate_set & required_skills)
    missing = sorted(required_skills - candidate_set)

    return matching, missing


# ================================
# 2. READINESS SCORE
# ================================
def calculate_readiness_score(
    candidate_skills: List[str],
    target_role: str,
    target_skills:list

) -> int:

    role_skills = target_skills
    candidate_set = set(candidate_skills)

    current_score = 0.0
    max_score = 0.0
    contribution=0.0
    for skill, importance in ROLE_SKILLS[target_role]["skills"].items():
        if skill not in SKILLS or skill not in role_skills:
            continue
        
        meta = SKILLS[skill]
        contribution = importance * meta["market"] * (1 / meta["difficulty"])
        max_score += contribution

        if skill in candidate_set:
            current_score += contribution
        
            

    return round((current_score / max_score) * 100) if max_score else 0


# ================================
# 3. WEIGHTED SKILL GAP
# ================================
def calculate_weighted_skill_gap_percentage(
    missing_skills: List[str],
    target_role: str,
    target_skills:list
) -> int:

    role_skills = target_skills
    x=0
    expected_skills=ROLE_SKILLS[target_role]["skills"] 
    relevant_skills = [
        skill for skill in target_skills
        if skill in expected_skills
    ]
    
    # Total weight only from relevant skills
    total_weight = sum(expected_skills[skill] for skill in relevant_skills)

    # Weight of missing skills
    missing_weight = sum(expected_skills[skill] for skill in missing_skills if skill in expected_skills)

    return round((missing_weight / total_weight) * 100) if total_weight else 0


# ================================
# 4. ESTIMATED LEARNING TIME
# ================================
def estimate_learning_time_months(missing_skills: List[str]) -> int:
    return ceil(sum(SKILLS[s]["time"] for s in missing_skills if s in SKILLS))


# ================================
# 5. SUCCESS RATE CALCULATION
# ================================
def calculate_success_rate(
    readiness_score: int,
    learning_months: int,
    experience_years: int,
    target_role: str
) -> str:

    min_exp, _ = ROLE_SKILLS[target_role]["experience"]

    readiness_factor = readiness_score / 100
    experience_factor = min(experience_years / min_exp, 1)
    learning_factor = max(0, 1 - learning_months / 18)

    success = (
        0.4 * readiness_factor +
        0.3 * experience_factor +
        0.3 * learning_factor
    )

 

    return f"{round(success * 100)}%"