# Phase 2 — Map UX + Light Access + Hardening

**Objective**  
Improve UX and add simple access control without over-scoping.

## Scope — IN
- Supabase Auth (email link/OTP) for admin-only surfaces (public map stays public)
- Provider List pane (click→zoom), debounced search, empty/error/loading states
- Backend paging/limits; basic rate limit; structured logs
- Optional single uptime probe against `/health`
- Optional small multi-state pilot for performance check

## Scope — OUT
- Full clustering, nationwide ingestion

## Exit Criteria
- Auth happy path functional; unauthorized actions blocked
- With ~10–50k rows, `/providers` p95 ≤ 200 ms
- Uptime probe green for 7 days

## Links
- Roadmap: ../ROADMAP.md
- ADRs: ../../engineering/DECISIONS.md
