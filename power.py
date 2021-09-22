import numpy as np
import cv2

img = cv2.imread('img.jpg')

gamma = [0.1, 0.5, 1.2, 2.2]

r1 = np.array(255*(img/255)**gamma[0],dtype='uint8')
r2 = np.array(255*(img/255)**gamma[1],dtype='uint8')
r3 = np.array(255*(img/255)**gamma[2],dtype='uint8')
r4 = np.array(255*(img/255)**gamma[3],dtype='uint8')

img3 = cv2.hconcat([img, r1, r2, r3, r4])

cv2.imwrite("gamma.jpg",img3)