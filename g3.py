import cv2 
import numpy as np

img = cv2.imread('gutters3.jpg',0)
img = cv2.resize(img,(680, 943))
_, th1 = cv2.threshold(img, 90, 253, cv2.THRESH_BINARY) #simple 
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 22) #adaptive
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 34); #adaptive

cv2.imshow("Image", img)
#cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()