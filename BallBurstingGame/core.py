import cv2
import numpy as np
import random


cap = cv2.VideoCapture(1)
alive = False

point = 0
speed = 2

fourcc = cv2.VideoWriter_fourcc(*'XVID')  #For the saved video codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #For the saved video codec


while True:
    _, frame = cap.read()
    mask = cv2.inRange(frame, (94, 56, 0), (218, 167, 33), None) 

    if alive is False:
         centerx = random.randint(10, 630)
         center = (centerx, 20)
         alive = True

    if(center[1] >= 450):
        alive = False
        point = 0
        
    
    centery = center[1] + speed
    center = (center[0], centery)
    zeroes = np.zeros((480, 640), dtype=np.uint8)
    zeroes[centery][center[0]] = np.uint8(1)
    

    mask2 = cv2.bitwise_and(mask,mask,mask = zeroes)
    points = cv2.findNonZero(mask2)
    if(points is not None):
        point = point + 1
        speed = speed + 1
        alive = False

    
    
    cv2.circle(frame, center, 5, (0, 0, 255), 10)
    cv2.putText(frame, "Points : " + str(point),(10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    out.write(frame) #Saving video...
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('zeroes', zeroes)
    
    #cv2.imshow('mask2', mask2)
   

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release() #Saves video
cv2.destroyAllWindows()