import pyzbar.pyzbar as pyzbar
import random
from flask import Flask, render_template, Response, jsonify
from Qrcodecamera2 import VideoCamera
import json
import math
import sys
import pickle
import cv2
cascPath = "C:/Users/Andrew Cao/Desktop/test image/main/haarcascade_frontalface_default.xml"
app = Flask(__name__)
_,app.image = VideoCamera().video.read()
faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.face.LBPHFaceRecognizer_create()



def decode(im):
            a = []
            targetx = 0
            targety = 0
            decodedObjects = pyzbar.decode(im)
            if len(decodedObjects) != 2:
                a.append('0')
                a.append('0')
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
                    x = x 
                    y = y
                    a.append(robotx)
                    a.append(roboty)
                    a.append(x)
                    a.append(y)       
            return a
            

def face(im):
    recognizer.read("C:/Users/Andrew Cao/Desktop/test image/main/trainner.yml")
    labels = {'person_name' : '1'}
    with open("C:/Users/Andrew Cao/Desktop/test image/main/labels.picke", 'rb') as f:
        labels = pickle.load(f)
        labels = {v:k for k,v in labels.items()}
    a = []
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5
    )
    if len(faces) == 0:
        a.append('0')
        a.append('0')
    else:
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)
            if conf > 60 and id_ == 0:
                a.append(x)
                a.append(y)
            print(x)
            print(y)
            print(conf)
    x = a[0]
    y = a[1]
    return a
   
  

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        _,app.image = camera.video.read()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        
@app.route('/position_feed')
def position_feed():  
    robot = decode(app.image)
    rx = int(robot[2])
    ry = int(robot[3])
    vx = int(robot[0])
    vy = int(robot[1])
    user = face(app.image)
    ux = int(user[0])
    uy = int(user[1])
    if rx != 0 and ux != 0:
        vux = ux-rx 
        vuy = uy-ry
        magrobot = math.sqrt(vx*vx+vy*vy)
        maguser = math.sqrt(vux*vux+vuy*vuy)
        angle = math.acos((vx*vux+vy*vuy)/(magrobot*maguser))
        anglesin = math.asin((vx*vuy-vy*vux)/(magrobot*maguser))
        final = angle*(anglesin/math.fabs(anglesin))
        distance = maguser
        data = {"angle":final,"distance":distance}
    else:
        data = {"angle":'0',"distance":'0'}  
    return jsonify(data)
       
@app.route('/user')
def user():  
    return jsonify(face(app.image))

@app.route('/robot')
def robottt():  
    return jsonify(decode(app.image))
    
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(host='192.168.1.125',debug=True, use_reloader = False)
    

