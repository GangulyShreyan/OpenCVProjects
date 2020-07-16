import cv2
import numpy as np
import sys


frame = cv2.imread('frame.jpg')
roi = frame
roi = cv2.resize(frame, (1200, 1000), interpolation = cv2.INTER_AREA) 
for i in range(len(roi)):
        for j in range(len(roi[0])):
            roi[i][j][0] = 0
cv2.imshow('roicvt', roi) 
cv2.imwrite('frme.jpg', roi)
cv2.waitKey(0)
