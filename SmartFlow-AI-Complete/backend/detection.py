import os,base64,cv2,numpy as np
from ultralytics import YOLO
PATH=os.getenv("YOLO_MODEL_PATH",os.path.join(os.path.dirname(__file__),"models","best.pt"))
model=YOLO(PATH) if os.path.exists(PATH) else None
CLASSES={"car","motorcycle","bus","truck"}
def detect_vehicles(raw):
    if model is None: raise RuntimeError("YOLO weights not found. Add backend/models/best.pt or set YOLO_MODEL_PATH.")
    image=cv2.imdecode(np.frombuffer(raw,dtype=np.uint8),cv2.IMREAD_COLOR)
    if image is None: raise ValueError("Invalid image file.")
    result=model.predict(source=image,conf=.35,verbose=False)[0]
    counts={k:0 for k in CLASSES}
    for box in result.boxes:
        name=model.names[int(box.cls[0])]
        if name in counts: counts[name]+=1
    ok,encoded=cv2.imencode(".jpg",result.plot())
    if not ok: raise RuntimeError("Could not encode result image.")
    return {"message":"Vehicle detection completed","total":sum(counts.values()),"counts":counts,"annotated_image":base64.b64encode(encoded.tobytes()).decode()}
