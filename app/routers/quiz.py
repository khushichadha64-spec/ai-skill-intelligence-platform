from fastapi import APIRouter, UploadFile, File
from app.models.schemas import QuizResponse, QuizQuestion

router = APIRouter(tags=["Quiz"])


@router.post("/generate-quiz", response_model=QuizResponse)
async def generate_quiz(file: UploadFile = File(...)):
    """
    Accepts an uploaded PDF/PPT and returns AI-generated MCQs.

    TODO (Member 3): replace this stub with real document text extraction
    (PyPDF2 / python-pptx) + LLM-based MCQ generation. Keep the response
    shape the same so the frontend quiz interface doesn't need changes.
    """
    # NOTE: file bytes are available via `await file.read()` when you wire
    # in real extraction. Not read here since this is a mock response.

    mock_questions = [
        QuizQuestion(
            question="What is the main purpose of descriptive statistics?",
            options={
                "A": "Predict future data",
                "B": "Summarize data",
                "C": "Train AI models",
                "D": "Encrypt data",
            },
            correct_answer="B",
            explanation=(
                "Descriptive statistics are used to summarize and describe "
                "the main features of data."
            ),
        )
    ]

    return QuizResponse(
        quiz_id="Q1001",
        source_file=file.filename,
        questions=mock_questions,
    )
