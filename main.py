"""
Entry point for the AI Skill Intelligence & Learning Platform backend.

Run locally with:
    uvicorn main:app --reload

Then open http://localhost:8000/docs for interactive API docs.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import profile, assess, gap_analysis, recommendations, quiz, dashboard, auth

app = FastAPI(
    title="AI Skill Intelligence & Learning Platform",
    description="Backend API for PS 26101",
    version="0.1.0",
)

# Allow the frontend (running on a different port, e.g. Vite/React on 5173)
# to call this API during development. Tighten this before any real deploy.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router)
app.include_router(assess.router)
app.include_router(gap_analysis.router)
app.include_router(recommendations.router)
app.include_router(quiz.router)
app.include_router(dashboard.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running. See /docs for API reference."}
