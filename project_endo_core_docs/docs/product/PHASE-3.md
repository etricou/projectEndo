# Phase 3 — Finish Map Pillar (Coverage + Scale + UX Completeness)

**Objective**  
Nationwide coverage, performant UX (incl. clustering), and ops polish.

## Scope — IN
- Nationwide ingestion (NPPES or equivalent), dedupe, geocoding for gaps
- Filters: taxonomy, city/ZIP; server-side filtering
- Marker clustering, server pagination, cache headers
- Error tracking (e.g., Sentry), improved logs, stricter rate limits
- Accessibility polish

## Scope — OUT
- Research Hub / Patient Records (next phases)

## Exit Criteria
- Nationwide bbox query p95 ≤ 250 ms on Supabase prod
- Smooth panning/zooming in dense metros (clustering enabled)
- Error rates within threshold; no PII/PHI in logs
