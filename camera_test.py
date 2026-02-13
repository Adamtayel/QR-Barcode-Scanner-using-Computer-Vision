# welcome :) 
# first importing 
import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    barcodes = decode(frame)
    for barcode in barcodes:
        data = barcode.data.decode('utf-8')
        print("Scanned:", data)

     # draw a green line 
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Scanner Test", frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows() # stop 
