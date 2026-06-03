# DMV Offices California

Independent static directory of all California DMV field offices.
Built with Astro 5 (static SSG). Data from California Open Data (data.ca.gov).

## Structure
- 208 DMV office pages (`/offices/[office]/`)
- 208 wait-time sub-pages (`/offices/[office]/wait-times/`)
- 187 city pages (`/cities/[city]/`)
- 5 guides (REAL ID, license renewal, registration, written test, address change)
- Near-me locator with real lat/lng coordinates

## Update data
1. Download latest GeoJSON from:
   https://gis.data.ca.gov/datasets/DMVfac::department-of-motor-vehicles-office-locations.geojson
   Save as `data/dmv-ca-raw.geojson`
2. Run: `python3 scripts/build-data.py`
3. Run: `npm run build`
4. Commit + push → RunCloud deploys

## Deploy
GitHub → RunCloud (Static, public path → `dist/`)
