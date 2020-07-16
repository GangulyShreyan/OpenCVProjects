import cv2
import numpy as np
import colorpicker
import imutils

color = colorpicker.color()
cap = cv2.VideoCapture(1)

cXprev = 0
cYprev = 0

while(True):
    _, frame = cap.read()
    framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('framehsv', framecvt)
    bg = cv2.inRange(framecvt, color[0], color[1])
    bginv = cv2.bitwise_not(bg)

    mask = cv2.bitwise_and(frame, frame, mask = bginv)

    cv2.imshow('frame', mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()