from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import get_junctions, save_junctions
from detection import detect_vehicles
from prediction import predict_traffic, optimize_signals
app=FastAPI(title="SmartFlow AI API",description="Smart Traffic Intelligence System",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5500","http://127.0.0.1:5500","http://localhost:5501","http://127.0.0.1:5501","http://localhost:5173","http://127.0.0.1:5173"],allow_credentials=False,allow_methods=["*"],allow_headers=["*"])
DEMO=[{"id":"J-04","name":"Central Avenue","vehicles":142,"density":"High","signal":"Green","duration":48},{"id":"J-02","name":"Riverside Road","vehicles":89,"density":"Medium","signal":"Red","duration":32},{"id":"J-01","name":"Market Street","vehicles":54,"density":"Low","signal":"Green","duration":24},{"id":"J-03","name":"University Boulevard","vehicles":117,"density":"High","signal":"Yellow","duration":41}]
@app.get("/")
def home(): return {"message":"Welcome to SmartFlow AI","docs":"/docs"}
@app.get("/health")
def health(): return {"status":"online","project":"SmartFlow AI"}
@app.get("/api/junctions")
def junctions():
    try: return get_junctions()
    except Exception: return DEMO
@app.post("/api/detect")
async def detect(file:UploadFile=File(...)):
    if not file.content_type or not file.content_type.startswith("image/"): raise HTTPException(400,"Please upload a valid image.")
    raw=await file.read()
    if not raw or len(raw)>10*1024*1024: raise HTTPException(413,"Image must be non-empty and below 10 MB.")
    try: return detect_vehicles(raw)
    except RuntimeError as e: raise HTTPException(503,str(e))
    except ValueError as e: raise HTTPException(400,str(e))
    except Exception as e: raise HTTPException(500,f"Detection failed: {e}")
@app.post("/api/optimize")
def optimize():
    items=get_junctions()
    recs=optimize_signals(items)
    try: save_junctions(recs)
    except Exception: pass
    return {"message":"Illustrative recommendations generated","recommendations":recs}
@app.get("/api/predictions")
def predictions(): return {"forecast":predict_traffic()}
@app.get("/api/report")
def report():
    try: return get_junctions()
    except Exception: return DEMO
