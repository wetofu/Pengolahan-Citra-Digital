import cv2
import numpy as np
from matplotlib import pyplot as plt
  
  
img = cv2.imread('img.jpg')
rows, cols, ch = img.shape
  
pts1 = np.float32([[50, 50],
                   [200, 50], 
                   [50, 200]])
  
pts2 = np.float32([[10, 100],
                   [200, 50], 
                   [100, 250]])
  
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
  
img3 = cv2.hconcat([img,dst])
cv2.imshow('a2',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()