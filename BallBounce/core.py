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
epsilon = 20

flag = False

centerX = 320
centerY = 290
veloballX = 0
veloballY = 0

cX = 0
cY = 0

while(True):
    _, frame = cap.read()
    framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue = cv2.inRange(framecvt, color[0], color[1])

    cnts = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

    mask =cv2.bitwise_and(frame, frame, mask = blue)

    cv2.circle(frame, (centerX, centerY), 5, (255, 255, 0), 10)

    if len(cnts)!= 0:
        M = cv2.moments(cnts[0])
        if(M["m00"] != 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            ds = np.sqrt(np.square(cX - cXprev) + np.square(cY - cYprev))
            velo = ds/dt    
            veloX = (cX - cXprev)/dt
            veloY = (cY - cYprev)/dt
            if(np.abs(cX-centerX)< epsilon) and (np.abs(cY-centerY)< epsilon):
                veloballX = veloX
                veloballY = veloY
            cv2.circle(frame, (cX, cY), 15, (0, 0, 255), 25)
            cXprev = cX 
            cYprev = cY

    centerX = int(centerX + (veloballX * dt))
    centerY = int(centerY + (veloballY * dt))
    print(np.shape(frame)) #max value of cY = 480
    if ((centerX+10) >= np.shape(frame)[1]) or ((centerX-10) <= 0) or ((centerY+10) >= np.shape(frame)[0]) or ((centerY-10) <= 0):
        veloballX = -veloballX
        veloballY = -veloballY

    
    #cv2.drawContours(frame, cnts, -1, (0, 0, 255), 5) 
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()