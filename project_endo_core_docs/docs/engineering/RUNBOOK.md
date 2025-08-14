# Runbook

Services
- Frontend: Vercel (public URL)
- Backend: Render (public URL)
- Database: Supabase (dev + prod)

Environment Variables
- Frontend: `VITE_API_BASE`, `VITE_MAPBOX_TOKEN`
- Backend: `DATABASE_URL`, `ALLOWED_ORIGINS`

Common Ops
- Phase 1 uses LA seed only (no ingestion jobs)
- Keep secrets out of git; use platform env var settings

Known Issues
- Free tiers can pause/cold start; first hit may be slow
- Tile usage counted against Mapbox plan
