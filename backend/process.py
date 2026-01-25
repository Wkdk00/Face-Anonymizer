import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(
    model_selection=1, 
    min_detection_confidence=0.3
)

def blur_face(img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_img)
    
    if results.detections:
        h, w, _ = img.shape
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            
            x = max(0, int(bboxC.xmin * w))
            y = max(0, int(bboxC.ymin * h))
            w_box = min(w - x, int(bboxC.width * w))
            h_box = min(h - y, int(bboxC.height * h))
            
            if w_box > 0 and h_box > 0:
                face_roi = img[y:y+h_box, x:x+w_box]
                if not face_roi.size == 0:
                    img[y:y+h_box, x:x+w_box] = cv2.blur(face_roi, (30, 30))
                    
    return img