# Phase 1 — Stable LA Map

**Objective**  
Public, stable Louisiana provider map with a basic, styled frontend.

## Scope — IN
- Supabase Postgres + PostGIS (dev + prod) with LA seed (3–10 rows)
- Tables: `providers`, `addresses (geog POINT 4326, is_primary)` + GiST/BTREE indexes
- FastAPI `/health`, `/providers?state&bbox&q` (≤500) joined to primary address
- React + Vite + Leaflet + Mapbox tiles; TanStack Query
- Basic layout (header + padded container), popups with Name/Practice/City-State ZIP
- Deploy to Vercel (FE) and Render (BE); CORS/envs set

## Scope — OUT
- Auth, clustering, advanced filters, nationwide data
- Monitoring dashboards / error tracking

## Deliverables
- Public FE URL (Vercel); BE URL (Render)
- Working map with LA pins and popups
- Repo docs: README, Runbook, Release Checklist, ADRs

## Exit Criteria (Definition of Done)
- Bbox query p95 ≤ 150 ms on Supabase dev (seed data)
- `/health` 200 on Render; FE→BE CORS verified
- Mapbox tiles load reliably on first paint
- First cold API hit ≤ 2–3 s

## Risks & Mitigations
- **Tile limits** → Mapbox key + attribution
- **Cold starts** → Accept on free tier; note for Phase 2
- **Data accuracy (seed)** → Hand-check LA seed rows

## Links
- Roadmap: ../ROADMAP.md
- ADRs: ../../engineering/DECISIONS.md
- Runbook: ../../engineering/RUNBOOK.md
- Release Checklist: ../../engineering/RELEASE-CHECKLIST.md
