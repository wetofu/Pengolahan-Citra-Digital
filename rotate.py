from PIL import Image
import cv2
import numpy as np

img = cv2.imread('img.jpg')
  
rotated90 = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
rotated270 = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated180 = cv2.rotate(img, cv2.cv2.ROTATE_180)

img2 = cv2.hconcat([img,rotated90])
img3 = cv2.hconcat([img,rotated270])
img4 = cv2.hconcat([img,rotated180])

# cv2.imshow('a2',img3)

cv2.imwrite("rotasi90.jpg", img2)
cv2.imwrite("rotasi270.jpg", img3)
cv2.imwrite("rotasi180.jpg", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()