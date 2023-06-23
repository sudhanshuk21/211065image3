import cv2
import numpy as np
image = cv2.imread('cctv4.png')
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


clahe = cv2.createCLAHE(clipLimit=15.0,  )
final_img = clahe.apply(image_bw)

normal_hist = cv2.equalizeHist(image_bw)  
sharpened1 = cv2.addWeighted(final_img, 1.5,normal_hist, -.5, 0)              
cv2.imshow('ordinary threshold', image)
cv2.imshow('CLAHE', final_img)
cv2.imshow('normal_hist', normal_hist)
cv2.imshow('sharpened1', sharpened1)
cv2.waitKey(0)