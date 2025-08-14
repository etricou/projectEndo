# Roadmap (Phases 1–5)

**North Star:** Provider discovery map with research and patient-record pillars.

## Phase 1 — Stable LA Map
Goal: Public, stable Louisiana provider map with a basic, styled frontend.

In:
- Supabase Postgres + PostGIS (dev + prod) with seed LA data
- FastAPI backend: `/health`, `/providers?state&bbox&q` (≤500), CORS
- React + Vite + Leaflet with Mapbox tiles, TanStack Query
- Deploy: Vercel (FE), Render (BE)
- Basic styling: header + padded container, popups (Name, Practice, City/State ZIP)

Out:
- Auth, clustering, advanced filters, nationwide data, monitoring suites

Risk Gates:
- Bbox query p95 ≤ 150 ms on Supabase (LA seed)
- `/health` 200 from Render; FE→BE CORS okay
- Mapbox tiles load on first paint
- First cold API hit ≤ 2–3 s (note free-tier cold starts)

## Phase 2 — Map UX + Light Access + Hardening
Goal: Pleasant UX + small access control without over-scoping.

In:
- Supabase Auth (email link/OTP) for **admin-only** surface (public map remains public)
- UX: Provider List pane (click→zoom), debounced search, empty/error/loading
- Hardening: pagination/limit on `/providers`, basic rate limit, structured logs
- One uptime probe (optional)
- Data: remain LA or small multi-state pilot

Out:
- Full clustering, nationwide ingestion

Risk Gates:
- Auth happy path works; unauthorized actions blocked
- With ~10–50k rows: `/providers` p95 ≤ 200 ms
- Uptime probe green for 7 days

## Phase 3 — Finish Map Pillar (Coverage + Scale + UX Completeness)
Goal: “Done” map with real coverage and performance.

In:
- Nationwide ingestion (NPPES or equivalent), dedupe, geocoding for gaps
- Filters: taxonomy, city/ZIP; server-side filtering
- Performance UX: **marker clustering**, server pagination, cache headers
- Ops: error tracking (e.g., Sentry), clearer logs, stricter rate limits
- A11y & polish: focus management, contrast, mobile height tuning

Out:
- Research Hub / Patient Records features (next phases)

Risk Gates:
- Nationwide: bbox query p95 ≤ 250 ms on Supabase prod
- FE remains smooth in dense metros (clustering on)
- Error rates within threshold; no PII/PHI in logs

## Phase 4 — Research Hub (New Pillar)
Goal: Foundation + light UI.

In:
- Schema & API: `signals`, `studies`, tagging/metadata
- Simple research dashboard (non-PHI)
- Roles: reuse Supabase Auth; basic roles/claims
- Ingestion hooks for sources

Risk Gates:
- CRUD works with role checks
- Privacy review passes (no sensitive data)

## Phase 5 — Patient Records Hub (New Pillar)
Goal: Minimal safe vault.

In:
- Schema & API: `vault_documents`, RBAC, audit log
- Storage: Supabase Storage or S3 with signed URLs
- Security: encryption at rest, short-lived tokens, least privilege, redaction in logs
- Consent UX: upload, share/revoke

Risk Gates:
- Privacy checklist passes
- Access control verified by tests
