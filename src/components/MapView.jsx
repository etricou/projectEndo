import React from 'react'
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet'
import L from 'leaflet'
import { useQuery } from '@tanstack/react-query'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'
const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN

// Default to Louisiana view
const DEFAULT_CENTER = [30.9843, -91.9623] // lat, lon
const DEFAULT_ZOOM = 7

// Simple marker icon fix for Leaflet + webpack/Vite
const DefaultIcon = L.icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41]
})
L.Marker.prototype.options.icon = DefaultIcon

function useBbox(map) {
  const [bbox, setBbox] = React.useState(null)
  React.useEffect(() => {
    if (!map) return
    const update = () => {
      const b = map.getBounds()
      const minLat = b.getSouth()
      const maxLat = b.getNorth()
      const minLon = b.getWest()
      const maxLon = b.getEast()
      setBbox([minLon, minLat, maxLon, maxLat].join(','))
    }
    update()
    map.on('moveend', update)
    return () => map.off('moveend', update)
  }, [map])
  return bbox
}

function MapEvents({ setMapRef }) {
  const map = useMapEvents({})
  React.useEffect(() => setMapRef(map), [map, setMapRef])
  return null
}

export default function MapView({ q }) {
  const [map, setMap] = React.useState(null)
  const bbox = useBbox(map)

  const query = useQuery({
    queryKey: ['providers', bbox, q],
    enabled: !!bbox,
    queryFn: async () => {
      const params = new URLSearchParams()
      params.set('state', 'LA')
      if (bbox) params.set('bbox', bbox)
      if (q) params.set('q', q)
      const res = await fetch(`${API_BASE}/providers?` + params.toString())
      if (!res.ok) throw new Error('Failed to fetch providers')
      return res.json()
    },
    staleTime: 30_000
  })

  const tileUrl =
    MAPBOX_TOKEN
      ? `https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${MAPBOX_TOKEN}`
      : 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

  const tileOptions = MAPBOX_TOKEN
    ? { id: 'mapbox/streets-v12', tileSize: 512, zoomOffset: -1, attribution: '© OpenStreetMap, © Mapbox' }
    : { attribution: '© OpenStreetMap contributors' }

  return (
    <div className="map-wrapper">
      <MapContainer center={DEFAULT_CENTER} zoom={DEFAULT_ZOOM} style={{ height: '70vh', width: '100%' }}>
        <TileLayer url={tileUrl} {...tileOptions} />
        <MapEvents setMapRef={setMap} />

        {query.isLoading && <div className="position-absolute top-0 end-0 m-2 badge bg-secondary">Loading…</div>}
        {query.isError && <div className="position-absolute top-0 end-0 m-2 badge bg-danger">Error loading</div>}

        {Array.isArray(query.data) && query.data.map((p, idx) => (
          <Marker key={idx} position={[p.lat, p.lon]}>
            <Popup>
              <strong>{[p.provider_first_name, p.provider_last_name].filter(Boolean).join(' ') || 'Provider'}</strong><br/>
              {p.practice_name || 'Practice'}<br/>
              {p.city}, {p.state} {p.zip}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  )
}
