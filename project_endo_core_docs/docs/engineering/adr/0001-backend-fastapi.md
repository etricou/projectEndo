# ADR 0001 — Backend: FastAPI (Python)
Status: Accepted

## Context
We need a backend that plays well with Postgres/PostGIS and favors Python strengths.

## Decision
Use **FastAPI** with **SQLAlchemy 2** and **GeoAlchemy2**; **Alembic** for migrations.

## Consequences
+ Strong typing & validation (Pydantic), great DX
+ Mature PostGIS patterns via SQLAlchemy/GeoAlchemy2
– Polyglot stack with React (JS) on the frontend
– Two dependency ecosystems to update

## Links
- Roadmap: ../../product/ROADMAP.md
