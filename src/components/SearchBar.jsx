import React from 'react'

export default function SearchBar({ value, onChange }) {
  const [local, setLocal] = React.useState(value || '')
  React.useEffect(() => setLocal(value || ''), [value])

  // Debounce
  React.useEffect(() => {
    const t = setTimeout(() => onChange(local), 300)
    return () => clearTimeout(t)
  }, [local])

  return (
    <input
      className="form-control"
      placeholder="Search by name or practice…"
      value={local}
      onChange={e => setLocal(e.target.value)}
    />
  )
}
