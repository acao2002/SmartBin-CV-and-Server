
import cv2
import numpy as np
a = 1
b = 1
# img = cv2.imread('C:/Users/Andrew Cao/Desktop/test image/main/4.png',0)
cap = cv2.VideoCapture(0)
while True:
    _,image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,2, 10)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('image',image)
    cv2.waitKey(1) 


print(circles)

           


