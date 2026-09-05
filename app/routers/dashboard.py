from fastapi import APIRouter, HTTPException, Depends
from app.mock_data import get_profile
from app.auth_utils import require_role

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard-data/admin")
def get_admin_dashboard(user: dict = Depends(require_role("admin"))):
    """
    Aggregated org-level data for the Admin Dashboard.
    TODO: replace with real aggregation once real employee data is loaded.
    Defined before the /{employee_id} route so 'admin' isn't swallowed as
    an employee_id.
    """
    return {
        "total_employees": 30,
        "overall_skill_gaps": [
            {"skill": "Python", "avg_gap": 1.8},
            {"skill": "Data Visualization", "avg_gap": 1.2},
        ],
        "competency_heatmap": [
            {"department": "Ministry of Statistics", "skill": "Python", "avg_level": 2.1}
        ],
        "training_progress_percent": 55,
    }


@router.get("/dashboard-data/{employee_id}")
def learner_dashboard(employee_id: str):
    """
    Aggregated data for a single employee's Learner Dashboard.
    TODO: once /assess, /gap-analysis, /recommendations are real, call
    them here (or query their stored results) instead of hand-building
    this mock response.
    """
    profile = get_profile(employee_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")

    return {
        "employee_id": employee_id,
        "competency_levels": profile["existing_skills"],
        "skill_gaps": [{"skill": "Python", "gap": 2}],
        "recommended_courses": ["Introduction to Python for Data Analysis"],
        "learning_progress_percent": 40,
        "recent_quiz_scores": [{"quiz_id": "Q1001", "score": 8, "total": 10}],
    }