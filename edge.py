import cv2
import numpy as np

img = cv2.imread('website.JPG',1)

subimg = img[400:700, 800:1000]
cv2.imshow('image', subimg)
cv2.waitKey(0);





