"""
Central mock data store.

Swap this out for real DB queries (SQLite/PostgreSQL) once Member 1's
data is loaded. Keeping it in one file makes that swap easy later --
just replace the functions below with DB calls, keep the return shapes.
"""

MOCK_PROFILES = {
    "EMP001": {
        "employee_id": "EMP001",
        "name": "Aditi Sharma",
        "designation": "Statistical Officer",
        "department": "Ministry of Statistics",
        "experience_years": 3,
        "current_role": "Data Analyst",
        "existing_skills": [
            {"skill": "Survey Design", "level": 3},
            {"skill": "Python", "level": 1},
            {"skill": "Data Analysis", "level": 4},
        ],
        "training_history": ["Intro to Data Collection (2023)"],
    }
}

REQUIRED_LEVELS_BY_ROLE = {
    "Statistical Officer": {
        "Survey Design": 4,
        "Python": 3,
        "Data Analysis": 4,
    }
}

MOCK_COURSES = [
    {
        "course_name": "Introduction to Python for Data Analysis",
        "related_skills": ["Python"],
        "difficulty": "Beginner",
        "duration_hours": 10,
    },
    {
        "course_name": "Advanced Statistical Analysis",
        "related_skills": ["Survey Design", "Data Analysis"],
        "difficulty": "Advanced",
        "duration_hours": 15,
    },
    {
        "course_name": "Data Visualization Using Power BI",
        "related_skills": ["Data Visualization"],
        "difficulty": "Intermediate",
        "duration_hours": 8,
    },
]


def get_profile(employee_id: str):
    return MOCK_PROFILES.get(employee_id)


def get_required_levels(role: str):
    return REQUIRED_LEVELS_BY_ROLE.get(role, {})
