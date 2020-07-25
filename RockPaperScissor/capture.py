import cv2
import numpy as np
import os

counter = 0
flag = 0

cap = cv2.VideoCapture(0)

path = 'images/scissor/'

while True:
    _, frame = cap.read()

    roi = frame[100:300, 100:300]
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    

    cv2.imwrite(path + str(counter) + '.jpg', roi)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        flag = 1

    if flag == 1:
        print(counter)
        counter = counter + 1

    if (cv2.waitKey(1) & 0xFF == ord('q')) or counter>200:
        break

cap.release()
cv2.destroyAllWindows