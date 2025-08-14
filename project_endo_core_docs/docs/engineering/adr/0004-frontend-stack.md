# ADR 0004 — Frontend Stack: React + Vite + Leaflet + TanStack + Bootstrap/Sass
Status: Accepted

## Context
We need a responsive map UI that feels good and ships quickly without over-engineering.

## Decision
Use **React + Vite**; **Leaflet** with Mapbox tiles; **TanStack Query** for fetch/caching; **Bootstrap + Sass** for layout.

## Consequences
+ Fast iteration, good developer ergonomics, minimal boilerplate
– Adds TanStack dependency (small), Bootstrap styling conventions

## Links
- Roadmap: ../../product/ROADMAP.md
