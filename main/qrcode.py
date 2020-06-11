import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import math
global x, y, xx, yy   


cap = cv2.VideoCapture(0)
def rescale_frame(frame, percent=75):
                width = int(frame.shape[1] * percent/ 100)
                height = int(frame.shape[0] * percent/ 100)
                dim = (width, height)
                return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
while True:
            
            _, image = cap.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            for a in range(gray.shape[0]-1):
                for b in range(gray.shape[1]-1):
                    pxval = gray[a][b]
                #print pxval
                    if pxval > 180:
                        gray[a][b] = 255
                    else:
                        gray[a][b] = 0 
            im = rescale_frame(gray,percent=200)  
            b = []
            targetx = 0
            targety = 0
            decodedObjects = pyzbar.decode(im)
            if len(decodedObjects) == 0:
                print('no detect')
            else:
                if len(decodedObjects)> 0:
                    for obj in decodedObjects:
                       data = str(obj.data)
                       if data == 'Robot':
                             print(data)
                             
                            #  points = obj.polygon
                             
                            #  x1 = points[0][0]
                            #  y1 = points[0][1]
                            #  x2 = points[2][0]
                            #  y2 = points[2][1] 
                            #  x = (x1+x2)/2
                            #  y = (y1+y2)/2
                            #  x3 = points[1][0]
                            #  y3 = points[1][1]
                             
                             
                             
                            
                       if data == 'robot2':
                             print(data)
                            #  points = obj.polygon
                            #  x1 = points[0][0]
                            #  y1 = points[0][1]
                            #  x2 = points[2][0]
                            #  y2 = points[2][1]
                            #  xx = (x1+x2)/2
                            #  yy = (y1+y2)/2
                         
                       
                    # #robotx = xx-x
                    # #roboty = yy-y
                    # #userx  = targetx - x
                    # usery  = targety - y
                    # magrobot = math.sqrt(robotx*robotx+roboty*roboty)
                    # maguser = math.sqrt(userx*userx+usery*usery)
                    # angle = math.acos((userx*robotx+usery*roboty)/(maguser*magrobot))
                    # orientation= math.asin((robotx*usery-roboty*userx)/(maguser*magrobot))
                    # cv2.line(im,(x,y),(xx,yy),(255,0,0),5)
                    # cv2.line(im,(x,y),(targetx,targety),(255,0,0),5)
                    # final =  angle*(orientation/math.fabs(orientation))
                    # print(robotx)
                    # print(roboty)
                    # print(userx)
                    # print(usery)
                    # print(angle)
                    # print(orientation)
                    # print(final)
                    # b.append(final)
            cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)   
            cv2.imshow("Frame", im)

            key = cv2.waitKey(1)
            if key == 27:
                break

    
                         
