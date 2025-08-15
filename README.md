# Project Endo — Frontend (React + Vite + Leaflet)

A simple React app that renders the provider map and talks to the FastAPI backend.

---

## Live

- **Site:** https://project-endo.vercel.app  
- **API (backend):** https://projectendo.onrender.com

---

## Environment variables

Create `frontend/.env` (or copy the example below).

```env
# API base URL (Render)
VITE_API_BASE=https://projectendo.onrender.com

# Map tiles
VITE_TILE_PROVIDER=mapbox
# Public Mapbox token (pk_... or pk....) with URL restrictions for:
#   http://localhost:5173
#   https://project-endo.vercel.app
VITE_MAPBOX_TOKEN=