import cv2
import numpy as np
a = 1
b = 1
img = cv2.imread('website.JPG',0)


for a in range(510):
    for b in range(1020):
        pxval = img[a][b]
        #print pxval
        if pxval > 120:
            img[a][b] = 255
        else:
            img[a][b] = 1    
        b = b + 1
    a = a+1
cv2.imwrite('blackwhite.JPG',img)

cv2.imshow('image',img)
cv2.waitKey(0) 
           


