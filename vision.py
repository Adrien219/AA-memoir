import cv2
from ultralytics import YOLO

class VisionEngine:
    def __init__(self):
        # Charge le modèle le plus léger pour la Raspberry Pi
        self.model = YOLO('yolov8n.pt') 
        
    def process(self, frame):
        # On réduit la taille de l'image (imgsz=320) pour booster les FPS sur la Pi
        results = self.model(frame, stream=True, conf=0.4, verbose=False, imgsz=320)
        detections = []
        for r in results:
            frame = r.plot() # Dessine les cadres sur l'image
            for box in r.boxes:
                label = self.model.names[int(box.cls[0])]
                detections.append(label)
        return frame, detections