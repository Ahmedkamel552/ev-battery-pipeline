# EV Battery Data Pipeline

A Python data pipeline that fetches, processes, and analyzes electric vehicle battery log data from a paginated REST API.

## What it does
- Fetches 320+ battery log records across 7 paginated API pages
- Filters and validates SOH (State of Health) readings
- Calculates average SOH across all vehicles
- Detects anomalies — records where SOH > 100% (physically impossible)
- Exports a clean JSON report with findings

## Key Finding
All 10 anomalies (SOH > 100%) originated from a single vehicle — **GEN-007** — suggesting sensor calibration issues or data corruption.

## Tech Stack
- Python
- Requests
- JSON

## Output
Generates `report.json` with:
- Total valid records
- Average SOH
- Highest SOH vehicle
- All anomalies flagged

## Run Locally
```bash
pip install requests
python report.py
```
