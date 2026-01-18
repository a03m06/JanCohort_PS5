from scores import (
    get_matching_and_missing_skills,
    calculate_readiness_score,
    calculate_weighted_skill_gap_percentage,
    estimate_learning_time_months,
    calculate_success_rate
)
from ps5 import get_text_response


def process_ps5_input(ps5_input: dict) -> dict:
    """
    Accesses PS-5 input structure and returns skill gap analysis
    """

    candidate = ps5_input["candidate"]
    target_role = ps5_input["target_role"]["title"]
    target_skills=ps5_input["target_role"]["required_skills"]

    
    matching, missing = get_matching_and_missing_skills(
        candidate["current_skills"],
        target_role,
        target_skills
    )

    readiness_score = calculate_readiness_score(
        candidate["current_skills"],
        target_role,
        target_skills
    )

    skill_gap_percentage = calculate_weighted_skill_gap_percentage(
        missing,
        target_role,
        target_skills
    )

    estimated_learning_time = estimate_learning_time_months(missing)
    success_rate=calculate_success_rate(readiness_score=readiness_score,learning_months=estimated_learning_time,
                                        experience_years=candidate['experience_years'],target_role=target_role)

    return {
        "analysis": {
            "matching_skills": matching,
            "missing_skills": missing,
            "skill_gap_percentage": skill_gap_percentage,
            "readiness_score": readiness_score,
            "estimated_learning_time_months": estimated_learning_time
        },
        "similar_transition":{
            "success_rate":success_rate,
            "avg_transition_time_months":(estimated_learning_time+6)/2
        }
    }


