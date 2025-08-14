# Data Glossary

## providers
- id (uuid, pk)
- npi (text, optional)
- provider_first_name (text)
- provider_last_name (text)
- practice_name (text)
- taxonomy_code (text)
- created_at, updated_at (timestamptz)

## addresses
- id (uuid, pk)
- provider_id (uuid, fk → providers.id)
- address1, address2 (text)
- city, state, zip (text)
- country (text, optional; keep for future global scope)
- geog (geography(Point, 4326)) — lat/lon point
- is_primary (boolean)
- created_at, updated_at (timestamptz)

## Indexes
- GiST on addresses.geog
- BTREE on (state, zip)
- GIN trigram on provider name/practice for q-search
