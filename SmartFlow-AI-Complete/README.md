# SmartFlow AI
Open this folder in VS Code. Install Live Server, right-click `frontend/index.html` > Open with Live Server. Frontend demo works without backend.
Optional backend (PowerShell): `cd backend`; `py -m venv .venv`; ` .\.venv\Scripts\Activate.ps1`; `pip install -r requirements.txt`; `uvicorn app:app --reload`.
API: http://127.0.0.1:8000 · Docs: http://127.0.0.1:8000/docs
Optional MySQL: run `backend/schema.sql`, then set DB_HOST, DB_USER, DB_PASSWORD, DB_NAME environment variables.
Optional YOLO: place your trained weights at `backend/models/best.pt` or set YOLO_MODEL_PATH.
All dashboard numbers, camera cards and forecasts are demo data until connected to real sources. Signal timings are illustrative and must not control real traffic lights.
