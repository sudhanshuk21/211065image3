import cv2
import numpy as np

#reading a image from computer and taking dimensions
img = cv2.imread('cctv3.png')
rows, cols = img.shape[:2]

 

#Boxfilter and blur function blurring
output_blur = cv2.blur(img, (25,25))
output_box = cv2.boxFilter(img, -1, (3,3), normalize=False)

 

 
cv2.imshow('Box filter', output_box)
 
cv2.imshow('Original', img)
cv2.waitKey(0)