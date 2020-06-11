import pyzbar.pyzbar as pyzbar
import cv2
import math 
global image

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(2)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    def get_frame(self):
        success, imag = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', imag)
        return jpeg.tobytes()
    def get_im(self):
            _,im = self.video.read()
            a = []
            targetx = 0
            targety = 0
            decodedObjects = pyzbar.decode(im)
            if len(decodedObjects) != 2:
                a.append('0')
                a.append('0')
            else:
                if len(decodedObjects) == 2:
                    for obj in decodedObjects:
                       data = str(obj.data)
                       if data == 'Robot':
                             points = obj.polygon
                             x1 = points[0][0]
                             y1 = points[0][1]
                             x2 = points[2][0]
                             y2 = points[2][1]            
                             x = (x1+x2)/2
                             y = (y1+y2)/2
                            
                             x3 = points[1][0]
                             y3 = points[1][1]
                             
                             
                             
                            
                       if data == 'robot2':
                             points = obj.polygon
                             x1 = points[0][0]
                             y1 = points[0][1]
                             x2 = points[2][0]
                             y2 = points[2][1]
                             xx = (x1+x2)/2
                             yy = (y1+y2)/2
                    robotx = xx-x
                    roboty = yy-y
                    userx  = targetx - x
                    usery  = targety - y
                    magrobot = math.sqrt(robotx*robotx+roboty*roboty)
                    maguser = math.sqrt(userx*userx+usery*usery)
                    angle = ((userx*robotx+usery*roboty)/(maguser*magrobot))
                    cv2.line(im,(x,y),(xx,yy),(255,0,0),5)
                    cv2.line(im,(x,y),(targetx,targety),(255,0,0),5)
                    print(robotx)
                    print(roboty)
                    print(userx)
                    print(usery)
                    print(angle)

                    a.append(angle)
            return a
  
    
   
