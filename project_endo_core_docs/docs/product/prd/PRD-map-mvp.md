# PRD — Map MVP (Phase 1)

## Problem
Users need a reliable way to find providers in Louisiana on a stable, public map.

## Goals / Non-Goals
- G: Public URL; smooth pan/zoom; popups with key fields
- NG: Clustering, advanced filters, nationwide data (later phases)

## Users & Use Cases
- Public viewer: open URL, search by name or practice, view pins and popups

## UX Notes
- Header + padded container with map (~65–70vh)
- Debounced search input

## API / Data Touchpoints
- `GET /providers?state=LA&bbox&q`

## Acceptance Criteria
- LA seed returns visible pins
- Pan/zoom triggers bbox fetch; popups show Name/Practice/City/State ZIP

## Open Questions
- None for Phase 1
