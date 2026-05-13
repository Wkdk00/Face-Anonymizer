from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import Response
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn, cv2, numpy as np, tempfile, os
from process import blur_face

app = FastAPI()
Instrumentator(should_group_status_codes=False, excluded_handlers=["/metrics"]).instrument(app).expose(app)

@app.post("/")
async def pred(file: UploadFile = File(...), method: str = Form("blur")):
    """
    Обрабатывает загруженное изображение или видео, обнаруживая лица и применяя выбранный метод скрытия.

    Args:
        file (UploadFile): Загруженный файл медиа.
        method (str): Способ обработки области лица. Доступные значения:
            - "blur": гауссово размытие (по умолчанию)
            - "black": заполнение чёрным цветом
            - "pixel": пикселизация

    Returns:
        Response: HTTP-ответ с обработанным содержимым.
            - Для изображений: `image/jpeg`
            - Для видео: `video/webm` (кодек VP8)

    Raises:
        HTTPException: 400 Bad Request, если файл не удалось декодировать.
    """
    contents = await file.read()
    
    if file.content_type.startswith("video"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name
        
        cap = cv2.VideoCapture(tmp_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 25
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out_path = tmp_path + "_out.webm"
        fourcc = cv2.VideoWriter_fourcc(*"vp80")
        out = cv2.VideoWriter(out_path, fourcc, fps, (w, h))
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            processed = blur_face(frame, method)
            out.write(processed)
        
        cap.release()
        out.release()
        os.unlink(tmp_path)
        
        with open(out_path, "rb") as f:
            result = f.read()
        
        os.unlink(out_path)
        
        return Response(result, media_type="video/webm")
    
    else:
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise HTTPException(status_code=400, detail="Invalid media format")
        img = blur_face(img, method)
        _, img_encoded = cv2.imencode('.jpg', img)
        return Response(content=img_encoded.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)