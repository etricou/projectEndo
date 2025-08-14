import csv
import os
from dataclasses import dataclass
from typing import List, Optional, Tuple

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from .db import get_engine, SQL_QUERY

load_dotenv()

app = FastAPI(title="Project Endo API", version="1.0.0")

# CORS
allowed = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
origins = [o.strip() for o in allowed.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- Data models -----

class ProviderOut(BaseModel):
    provider_first_name: Optional[str] = ""
    provider_last_name: Optional[str] = ""
    practice_name: Optional[str] = ""
    city: Optional[str] = ""
    state: Optional[str] = ""
    zip: Optional[str] = ""
    lat: float
    lon: float

# ----- Seed loader (CSV fallback if no DB) -----

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "seed_la.csv")

def load_seed() -> List[ProviderOut]:
    items: List[ProviderOut] = []
    try:
        with open(SEED_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                try:
                    items.append(ProviderOut(
                        provider_first_name=r.get("provider_first_name",""),
                        provider_last_name=r.get("provider_last_name",""),
                        practice_name=r.get("practice_name",""),
                        city=r.get("city",""),
                        state=r.get("state",""),
                        zip=r.get("zip",""),
                        lat=float(r["lat"]),
                        lon=float(r["lon"]),
                    ))
                except Exception:
                    continue
    except FileNotFoundError:
        pass
    return items

SEED_CACHE = load_seed()

def in_bbox(lat: float, lon: float, bbox: Tuple[float,float,float,float]) -> bool:
    minLon, minLat, maxLon, maxLat = bbox
    return (minLat <= lat <= maxLat) and (minLon <= lon <= maxLon)

# ----- Routes -----

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/providers", response_model=List[ProviderOut])
def get_providers(
    state: Optional[str] = Query(None, description="Two-letter state code (e.g., LA)"),
    bbox: Optional[str] = Query(None, description="minLon,minLat,maxLon,maxLat"),
    q: str = Query("", description="Name/practice search term"),
):
    # Parse bbox
    bbox_tuple: Optional[Tuple[float,float,float,float]] = None
    if bbox:
        try:
            parts = [float(x) for x in bbox.split(",")]
            if len(parts) != 4:
                raise ValueError()
            bbox_tuple = (parts[0], parts[1], parts[2], parts[3])
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid bbox format. Use minLon,minLat,maxLon,maxLat")

    engine = get_engine()
    if engine is None:
        # Fallback to seed CSV
        data = SEED_CACHE
        # filter by state
        if state:
            data = [d for d in data if (d.state or "").upper() == state.upper()]
        # filter by bbox
        if bbox_tuple:
            data = [d for d in data if in_bbox(d.lat, d.lon, bbox_tuple)]
        # filter by q
        if q:
            needle = q.lower()
            def mk_name(d: ProviderOut):
                return f"{(d.provider_first_name or '')} {(d.provider_last_name or '')} {(d.practice_name or '')}".lower()
            data = [d for d in data if needle in mk_name(d)]
        return data[:500]

    # DB path
    params = {
        "state": state,
        "minLon": bbox_tuple[0] if bbox_tuple else None,
        "minLat": bbox_tuple[1] if bbox_tuple else None,
        "maxLon": bbox_tuple[2] if bbox_tuple else None,
        "maxLat": bbox_tuple[3] if bbox_tuple else None,
        "q": q or "",
    }
    with engine.connect() as conn:
        rows = conn.execute(SQL_QUERY, params).fetchmany(500)
    out: List[ProviderOut] = []
    for r in rows:
        out.append(ProviderOut(
            provider_first_name=r[0],
            provider_last_name=r[1],
            practice_name=r[2],
            city=r[3],
            state=r[4],
            zip=r[5],
            lat=float(r[6]),
            lon=float(r[7]),
        ))
    return out
