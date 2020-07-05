import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()

    cv2.circle(frame, (100,100), 80, (0, 0, 255))
    roi = frame[50:200 , 50:200]

    print(roi)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()