import cv2
import numpy as np
import math

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(1)
    
    def __del__(self):
        #releasing camera
        self.video.release()


    def get_frame(self, object1, object2):
        _, frame = self.video.read()
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resImage = np.shape(frame)
        resScreen = resImage
        
        '''
        For obtaining the RGB pixel value of the object
        
        cv2.circle(frame, (100,100), 80, (0, 0, 255))
        roi = frame[50:200 , 50:200]

        '''

        mask = cv2.inRange(frame, object1.minbgr, object1.maxbgr, None) 
        mask2 = cv2.inRange(frame, object2.minbgr, object2.maxbgr,  None)


        points = cv2.findNonZero(mask)
        points2 = cv2.findNonZero(mask2)
        
        if (points is not None) and (points2 is not None):

            lent = np.shape(points)
            lent2 = np.shape(points2)

            middlepointcoordinate = points[int(lent[0]/2)]
            middlepointcoordinate2 = points2[int(lent2[0]/2)]

            middlepointcoordinate = (middlepointcoordinate[0][0], middlepointcoordinate[0][1])
            middlepointcoordinate2 = (middlepointcoordinate2[0][0], middlepointcoordinate2[0][1])

            avg = (int((middlepointcoordinate[0] + middlepointcoordinate2[0])/2) , int((middlepointcoordinate[1] + middlepointcoordinate2[1])/2))

            angle = math.degrees(np.arctan((middlepointcoordinate2[1] - middlepointcoordinate[1])/(middlepointcoordinate2[0] - middlepointcoordinate[0])))
            distance = math.sqrt((middlepointcoordinate2[0] - middlepointcoordinate[0])**2 + (middlepointcoordinate2[1] - middlepointcoordinate[1])**2)

            cv2.line(frame, middlepointcoordinate, middlepointcoordinate2, (0,255, 0))
            cv2.putText(frame, "Angle : " + str(angle), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
            cv2.putText(frame, "Length : " + str(distance), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

            cv2.circle(frame, middlepointcoordinate, 5, (0,0,255), 10)
            cv2.circle(frame, middlepointcoordinate2, 5, (0,0,255), 10)
            
        '''
        cv2.imshow('frame', frame)
        cv2.imshow('frame1', mask)
        cv2.imshow('frame2', mask2)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("saved.jpg", roi)
            break
        '''

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
   