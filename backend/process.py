import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.3)

def blur_face(img, method="blur"):
    """
    Обнаруживает лица на изображении с помощью MediaPipe и применяет выбранный метод скрытия.

    Args:
        img (numpy.ndarray): Входное изображение в цветовом пространстве BGR (формат OpenCV).
        method (str): Способ обработки области лица. Поддерживаемые значения:
            - "blur": размытие фильтром среднего.
            - "black": полное затемнение области.
            - "pixel": пикселизация.
            По умолчанию: "blur".

    Returns:
        numpy.ndarray: Изображение с обработанными областями лиц. 
    """
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_img)
    h, w, _ = img.shape
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            x = max(0, int(bboxC.xmin * w))
            y = max(0, int(bboxC.ymin * h))
            w_box = min(w - x, int(bboxC.width * w))
            h_box = min(h - y, int(bboxC.height * h))
            if w_box > 0 and h_box > 0:
                if method == "blur":
                    img[y:y+h_box, x:x+w_box] = cv2.blur(img[y:y+h_box, x:x+w_box], (30, 30))
                elif method == "black":
                    img[y:y+h_box, x:x+w_box] = 0
                elif method == "pixel":
                    face_roi = img[y:y+h_box, x:x+w_box]
                    small = cv2.resize(face_roi, (10, 10), interpolation=cv2.INTER_LINEAR)
                    img[y:y+h_box, x:x+w_box] = cv2.resize(small, (w_box, h_box), interpolation=cv2.INTER_NEAREST)
    return img