import os
from typing import Optional
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

def get_engine() -> Optional[Engine]:
    url = os.getenv("DATABASE_URL")
    if not url:
        return None
    # SQLAlchemy 2.0 style engine
    engine = create_engine(url, pool_pre_ping=True)
    return engine

SQL_QUERY = text("""
select
  p.provider_first_name,
  p.provider_last_name,
  p.practice_name,
  a.city, a.state, a.zip,
  ST_Y(a.geog::geometry) as lat,
  ST_X(a.geog::geometry) as lon
from providers p
join addresses a on a.provider_id = p.id and a.is_primary = true
where (:state is null or a.state = :state)
  and (
    :minLon is null or
    ST_Intersects(
      a.geog::geometry,
      ST_MakeEnvelope(:minLon, :minLat, :maxLon, :maxLat, 4326)
    )
  )
  and (
    :q = '' or
    (p.provider_first_name || ' ' || p.provider_last_name || ' ' || coalesce(p.practice_name,'')) ilike ('%' || :q || '%')
  )
order by p.provider_last_name nulls last, p.provider_first_name nulls last
limit 500;
""")
