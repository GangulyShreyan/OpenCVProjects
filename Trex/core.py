import cv2
import numpy as np
import colorpicker
import imutils
import keyboard

color = colorpicker.color()
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
            if(cX < 214) and (cY<160):
                keyboard.press_and_release('up, left') 
            if(cX > 214) and (cY < 160) and (cX < 428):
                keyboard.press_and_release('up')
            if(cX > 428) and (cY<160):
                keyboard.press_and_release('up, right')
            if(cX < 214) and (cY > 160) and (cY < 320):
                keyboard.press_and_release('left')
            if(cX > 428) and (cY > 160) and (cY < 320):
                keyboard.press_and_release('right')
            if(cX < 214) and (cY > 320):
                keyboard.press_and_release('down, left')
            if(cX > 214) and (cX < 428) and (cY > 320):
                keyboard.press_and_release('down')
            if(cX > 428) and (cY > 320):
                keyboard.press_and_release('down, right') 
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), 5)

    cv2.line(frame, (214, 0), (214, 480), (4, 82, 83), 3)
    cv2.line(frame, (428, 0), (428, 480), (4, 82, 83), 3)
    cv2.line(frame, (0, 160), (640, 160), (4, 82, 83), 3)
    cv2.line(frame, (0, 320), (640, 320), (4, 82, 83), 3)

    cv2.putText(frame, 'UP', (250, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (30, 50, 80), 4)
    cv2.putText(frame, 'DOWN', (230, 410), cv2.FONT_HERSHEY_SIMPLEX, 2, (30, 50, 80), 4)
    cv2.putText(frame, 'RIGHT', (30, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (30, 50, 80), 4)
    cv2.putText(frame, 'LEFT', (458, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (30, 50, 80), 4)
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()