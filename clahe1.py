# import cv2
# import numpy as np
# image = cv2.imread('cctv2.png')
# image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# final_img = clahe.apply(image_bw)

# normal_hist = cv2.equalizeHist(image_bw)  
# sharpened1 = cv2.addWeighted(final_img, 1.5,normal_hist, -.5, 0) 
  

# cv2.imshow('ordinary threshold', image)
# cv2.imshow('CLAHE', final_img)
# cv2.imshow('normal_hist', normal_hist)
# cv2.imshow('sharpened1', sharpened1)
# cv2.waitKey(0)
import cv2
import numpy as np
image = cv2.imread('cctv2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                                                                                             
cv2.imshow('gray', gray)
equalized = cv2.equalizeHist(gray)
cv2.imshow('equalized', equalized) 
clahe = cv2.createCLAHE(clipLimit=5.0)
result = clahe.apply(gray)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()                                                             