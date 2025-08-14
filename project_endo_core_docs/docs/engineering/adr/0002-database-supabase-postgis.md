# ADR 0002 — Database: Supabase Postgres + PostGIS
Status: Accepted

## Context
We need managed Postgres with spatial capabilities and easy dev/prod separation.

## Decision
Use **Supabase Postgres** for dev & prod; enable **PostGIS** and **pg_trgm**.

## Consequences
+ Managed backups, roles, console; easy connection strings
+ No lock-in when sticking to Postgres features
– Free tier has quotas; cold starts or pausing possible
– Tile usage policy still applies (see ADR 0003)

## Links
- Roadmap: ../../product/ROADMAP.md
