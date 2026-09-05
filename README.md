# Backend — AI Skill Intelligence & Learning Platform

FastAPI skeleton with all endpoints from `API_CONTRACT.md` stubbed with mock data.
Everyone can start integrating against these right away.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:
- http://localhost:8000/docs — interactive Swagger UI (test every endpoint here)
- http://localhost:8000/ — health check

## Project structure

```
backend/
├── main.py                    # FastAPI app, mounts all routers
├── requirements.txt
├── app/
│   ├── mock_data.py            # Central mock data (swap for real DB later)
│   ├── models/
│   │   └── schemas.py          # Pydantic request/response models
│   └── routers/
│       ├── profile.py          # GET /profile/{employee_id}      -> Member 1's data
│       ├── assess.py           # POST /assess                    -> Member 2's AI logic
│       ├── gap_analysis.py     # GET /gap-analysis/{employee_id} -> Member 2's logic
│       ├── recommendations.py  # GET /recommendations/{id}       -> Member 3's logic
│       ├── quiz.py             # POST /generate-quiz             -> Member 3's logic
│       └── dashboard.py        # GET /dashboard-data/...         -> aggregation
```

## How to plug in real logic (Members 2 & 3)

Each router file has a clearly marked `MOCK LOGIC` section. Replace only that
section with your real function calls — leave the request/response shape
(the Pydantic models in `schemas.py`) untouched unless you've updated
`API_CONTRACT.md` and told the rest of the team first.

## Database

Currently using in-memory mock data (`app/mock_data.py`) for speed. To move to
SQLite:
1. Add `sqlalchemy` to `requirements.txt`.
2. Create `app/database.py` with an SQLite engine + session.
3. Replace the functions in `mock_data.py` with real queries, keeping the
   same function names/signatures so the routers don't need to change.

## Testing

- Use `/docs` for quick manual testing of each endpoint.
- Export a Postman collection from `/docs` (Swagger → "Export") and share it
  with Member 5 so the frontend always has a working reference.
- Re-test the full flow (profile → assess → gap-analysis → recommendations →
  dashboard) every few hours, not just during the integration phase.
