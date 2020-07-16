import cv2
import numpy as np
import colorpicker
import imutils
import frameratechecker

color = colorpicker.color()
dt = 1/frameratechecker.fps()
cap = cv2.VideoCapture(1)

cXprev = 0
cYprev = 0

while(True):
    _, frame = cap.read()
    framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue = cv2.inRange(framecvt, color[0], color[1])

    cnts = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

    mask =cv2.bitwise_and(frame, frame, mask = blue)
    if len(cnts)!= 0:
        M = cv2.moments(cnts[0])
        if(M["m00"] != 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), 10)
            if(cXprev != 0 ) and (cYprev != 0):
                cv2.line(frame, (cX, cY), (cXprev, cYprev), (255, 2550, 0), 3)
            cXprev = cX
            cYprev = cY
            
    #cv2.drawContours(frame, cnts, -1, (0, 0, 255), 5) 
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()