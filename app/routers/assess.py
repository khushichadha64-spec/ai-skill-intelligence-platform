from fastapi import APIRouter
from app.models.schemas import AssessRequest, AssessResponse, SkillLevel

router = APIRouter(tags=["Assess"])


@router.post("/assess", response_model=AssessResponse)
def assess_experience(request: AssessRequest):
    """
    Extracts structured skills from free-text employee experience.

    TODO (Member 2): replace this stub with the real AI/LLM + rule-based
    logic. Keep the response shape (employee_id, extracted_skills) the same
    so nothing downstream breaks.
    """
    # --- MOCK LOGIC (replace with Member 2's real extraction) ---
    mock_extracted = [
        SkillLevel(skill="Survey Design", level=3),
        SkillLevel(skill="Data Collection", level=2),
    ]
    return AssessResponse(
        employee_id=request.employee_id,
        extracted_skills=mock_extracted,
    )
