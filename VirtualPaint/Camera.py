import cv2
import numpy as np
import math
import imutils

pointlst = []

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(1)
    
    def __del__(self):
        #releasing camera
        self.video.release()

    def get_roi(self):
        _, frame = self.video.read()
        roi = frame[100:300, 0:200]

        cv2.imwrite('output.jpg', roi)

        ret, jpeg = cv2.imencode('.jpg', roi)
        return jpeg.tobytes()


    def get_frame(self, colorobj1):
        _, frame = self.video.read()
        framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blue = cv2.inRange(framecvt, colorobj1[0], colorobj1[1])

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

                pointlst.append((cX, cY))

        for c in pointlst:
                cv2.circle(frame, (c[0], c[1]), 5, (0, 255, 255), 10)
            

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
   