from fastapi import APIRouter, HTTPException
from app.models.schemas import Profile
from app.mock_data import get_profile

router = APIRouter(tags=["Profile"])


@router.get("/profile/{employee_id}", response_model=Profile)
def read_profile(employee_id: str):
    """
    Returns a single employee profile.
    TODO (Member 1 / Member 4): replace mock_data lookup with real DB query
    once the sample employee dataset (JSON/CSV) is loaded into SQLite.
    """
    profile = get_profile(employee_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")
    return profile
