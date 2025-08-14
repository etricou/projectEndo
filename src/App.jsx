import React from 'react'
import MapView from './components/MapView.jsx'
import SearchBar from './components/SearchBar.jsx'

export default function App() {
  const [q, setQ] = React.useState('')

  return (
    <div className="container py-3">
      <header className="mb-3">
        <h1 className="h4 mb-1">Project Endo — Provider Map (LA)</h1>
        <p className="text-muted mb-0">Basic MVP with Mapbox tiles and seed data. Type to search by name/practice.</p>
      </header>

      <div className="card shadow-sm">
        <div className="card-body">
          <div className="row g-3 align-items-center">
            <div className="col-12 col-md-6">
              <SearchBar value={q} onChange={setQ} />
            </div>
          </div>
          <div className="mt-3">
            <MapView q={q} />
          </div>
        </div>
      </div>
    </div>
  )
}
