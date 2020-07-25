import cv2
import numpy
from sklearn import svm
from joblib import load
clf = load('model.pkl')

cap = cv2.VideoCapture(0)

label = ['Paper', 'Rock', 'Scissor', 'None']

while True:

    _, frame = cap.read()

    roi = frame[100:300, 100:300]
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 5)
    
    cv2.imwrite('rock.jpg', roi)
    gg = cv2.imread('rock.jpg', 0)/255
    gg = gg.flatten()
    gg = gg.reshape(1, -1)
    gg = clf.predict(gg)
    print(label[gg[0]])
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.imwrite('rock.jpg', roi)
        break

cap.release()
cv2.destroyAllWindows()