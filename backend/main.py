from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
from io import BytesIO
import cv2
import numpy as np

from process import blur_face

app = FastAPI()

instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=["/metrics"],
)
instrumentator.instrument(app).expose(app)

@app.post("/")
async def pred(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Invalid media format")
    img = blur_face(img)
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()
    return StreamingResponse(BytesIO(img_bytes), media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)