# Backend (FastAPI)

## Endpoints
- `GET /health` → `{ "status": "ok" }`
- `GET /providers?state=LA&bbox=minLon,minLat,maxLon,maxLat&q=term` → up to 500 results

## Environment
Copy `.env.example` to `.env`. If `DATABASE_URL` is unset, the API serves data from `data/seed_la.csv`.

Run locally:
```
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
