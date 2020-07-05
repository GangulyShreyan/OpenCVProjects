import cv2
import time

def fps():
    cap = cv2.VideoCapture(1)
    frames = 0
    start = time.time()

    while True:
        _, frame = cap.read()
        frames = frames + 1
        cv2.imshow('frame', frame)
        if int(end-start) == 1 & cv2.waitKey(1) :     
            return(int(frames/(end-start)))
            break

    cap.release()
    cv2.destroyAllWindows()

