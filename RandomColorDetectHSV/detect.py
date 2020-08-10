import cv2
import numpy as np
import imutils
import random


class detect:
    def __init__(self):

        try:
            self.number = int(input("Enter number of objects to be detected : "))
        except ValueError:
            self.close('Integer expected.')

        self.cap = cv2.VideoCapture(1)
        self.cXprev = 0
        self.cYprev = 0
        self.color = []
        

    def colorpicker(self):
        for index in range(self.number):
            while True:
                _, frame = self.cap.read()
                roi = frame[100:300, 0:200]
                roicvt = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                min = np.min(roicvt, axis = 1)
                actualmin = np.min(min, axis = 0)
                max = np.max(roicvt, axis = 1)
                actualmax = np.max(max, axis = 0)

                cv2.imshow('frame', roicvt)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.color.append([actualmin, actualmax])
                    break
            print("Object " + str(index + 1) + " Scanned")

    def core(self):
        while(True):
            _, frame = self.cap.read()
            framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            for color in self.color:

                col = cv2.inRange(framecvt, color[0], color[1])

                cnts = cv2.findContours(col.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

                mask =cv2.bitwise_and(frame, frame, mask = col)
                if len(cnts)!= 0:
                    M = cv2.moments(cnts[0])
                    if(M["m00"] != 0):
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        discol = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                        cv2.circle(frame, (cX, cY), 5,  discol, 10) 
                        print(cX, cY)       
            
            cv2.imshow('frame', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def run(self):
        print("****CODE IS RUNNING****") 
        self.colorpicker()
        self.core()

if __name__ == '__main__':
    app = detect()
    app.run()