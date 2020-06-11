import cv2
import numpy as np

img = np.uint8([[[0,255,0]]]);
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print hsv_img
img2 = cv2.imread('tesst.png',1);
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
minmau = np.array([30, 255, 255])
maxmau = np.array([70,255,255])
mask = cv2.inRange(hsv_img2,minmau,maxmau)
final = cv2.bitwise_and(img2,img2, mask= mask)
cv2.imshow('okk',img2)
cv2.imshow('ok',final)
cv2.waitKey(0)
