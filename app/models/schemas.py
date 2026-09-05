from pydantic import BaseModel
from typing import List, Dict


class SkillLevel(BaseModel):
    skill: str
    level: int


class Profile(BaseModel):
    employee_id: str
    name: str
    designation: str
    department: str
    experience_years: int
    current_role: str
    existing_skills: List[SkillLevel]
    training_history: List[str]


class AssessRequest(BaseModel):
    employee_id: str
    experience_text: str


class AssessResponse(BaseModel):
    employee_id: str
    extracted_skills: List[SkillLevel]


class SkillGap(BaseModel):
    skill: str
    current_level: int
    required_level: int
    gap: int


class GapAnalysisResponse(BaseModel):
    employee_id: str
    role: str
    gaps: List[SkillGap]


class RecommendedCourse(BaseModel):
    course_name: str
    related_skills: List[str]
    difficulty: str
    duration_hours: int
    match_score: float


class RecommendationsResponse(BaseModel):
    employee_id: str
    recommended_courses: List[RecommendedCourse]


class QuizQuestion(BaseModel):
    question: str
    options: Dict[str, str]
    correct_answer: str
    explanation: str


class QuizResponse(BaseModel):
    quiz_id: str
    source_file: str
    questions: List[QuizQuestion]
