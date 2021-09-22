import cv2
import numpy as np
import matplotlib.pyplot as plt
   
img = cv2.imread('img.jpg')
   
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))
   
# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)
   
# Display both images
img3 = cv2.hconcat([img,log_image])
cv2.imshow('a2',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()