import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('text.jpg',0)
img = cv2.resize(img, (100, 100))
edges = cv2.Canny(img,100,200)

zero = np.argwhere(edges == 0)
ones = np.argwhere(edges == 255)

arr = np.empty((edges.shape[0], edges.shape[1]), dtype='str')
arr[:] = ' '

for elem in ones:
    arr[elem[0]][elem[1]] = '*'

np.savetxt('text.txt', arr, delimiter='', header='', comments='', fmt='%s')
