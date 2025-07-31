import cv2
from ultralytics import YOLO

# Modeli yüklə
model = YOLO('D:\MyPc\Desktop\Data\Face Detection\mask_detector.pt')

# sinif adları 
class_names = ['Maskali', 'Maskasiz']

# Kamera başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    main_label = "Maska yoxdur"
    for r in results:
        if r.boxes is not None and len(r.boxes) > 0:
            box = r.boxes[0] # first detectuin
            cls = int(box.cls[0])
            conf = box.conf[0]
            main_label = f"{class_names[cls]} ({conf:.2f})"
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            # qutu cek
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, main_label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        else:
            main_label = "Maska yoxdur"

    # yazi yeri
    cv2.putText(frame, main_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow('Mask Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()