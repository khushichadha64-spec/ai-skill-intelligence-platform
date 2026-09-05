from fastapi import APIRouter
from app.models.schemas import RecommendationsResponse, RecommendedCourse
from app.mock_data import MOCK_COURSES

router = APIRouter(tags=["Recommendations"])


@router.get("/recommendations/{employee_id}", response_model=RecommendationsResponse)
def get_recommendations(employee_id: str):
    """
    Returns recommended courses based on the employee's skill gaps.

    TODO (Member 3): replace this stub with real embedding similarity
    between skill gaps and course descriptions (FAISS/ChromaDB).
    Keep the response shape the same -- especially match_score, which
    the frontend uses to sort/display confidence.
    """
    # --- MOCK LOGIC (replace with Member 3's real recommender) ---
    recommended = [
        RecommendedCourse(**course, match_score=round(0.95 - 0.1 * i, 2))
        for i, course in enumerate(MOCK_COURSES)
    ]
    return RecommendationsResponse(
        employee_id=employee_id,
        recommended_courses=recommended,
    )
