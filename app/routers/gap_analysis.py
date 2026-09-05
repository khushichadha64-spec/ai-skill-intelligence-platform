from fastapi import APIRouter, HTTPException
from app.models.schemas import GapAnalysisResponse, SkillGap
from app.mock_data import get_profile, get_required_levels

router = APIRouter(tags=["Gap Analysis"])


@router.get("/gap-analysis/{employee_id}", response_model=GapAnalysisResponse)
def gap_analysis(employee_id: str):
    """
    Compares an employee's current skill levels against the required
    levels for their role.

    TODO (Member 2): this currently reads existing_skills straight from
    mock_data. Once your assessment logic is live, this should compare
    the OUTPUT of /assess against required levels instead.
    """
    profile = get_profile(employee_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")

    required = get_required_levels(profile["current_role"]) or get_required_levels(
        profile["designation"]
    )

    gaps = []
    for item in profile["existing_skills"]:
        skill = item["skill"]
        current = item["level"]
        req = required.get(skill, current)  # if no requirement defined, no gap
        gaps.append(
            SkillGap(
                skill=skill,
                current_level=current,
                required_level=req,
                gap=max(req - current, 0),
            )
        )

    return GapAnalysisResponse(
        employee_id=employee_id,
        role=profile["designation"],
        gaps=gaps,
    )
