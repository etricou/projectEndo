# ADR 0003 — Tiles: Mapbox
Status: Accepted

## Context
OpenStreetMap default tiles are not meant for production traffic. We need reliable tiles with a clear ToS and free tier.

## Decision
Use **Mapbox** tiles for public deployments (Mapbox token, proper attribution).

## Consequences
+ Reliable tiles, styled maps, usage-based pricing with free tier
– Requires a token and monitoring usage
– Vendor dependency (alternatives: MapTiler paid plans)

## Links
- Roadmap: ../../product/ROADMAP.md
