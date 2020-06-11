import pyzbar.pyzbar as pyzbar
import random
from flask import Flask, render_template, Response, jsonify
from Qrcodecamera2 import VideoCamera
import json
import math

app = Flask(__name__)
_,app.image = VideoCamera().video.read()


def decode(im):
            global xx
            global yy
            global x
            global y
            a = []
            decodedObjects = pyzbar.decode(im)
            if len(decodedObjects) == 0:
                a.append('0')
                a.append('0')
                a.append('0')
                a.append('0')
            else:
                if len(decodedObjects) == 1:
                    a.append('0')
                    a.append('0')
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
                            a.append('x')
                            a.append('y')
                        else:    
                            if data == 'robot2':
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
            xvalro = a[0]
            yvalro = a[1]
            locax = a[2]
            locay = a[3]
            data = { 'vectorrobotx' : xvalro, 'vectorroboty': yvalro,'locax':locax, 'locay':locay }
            return data
            
   
  

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
    return jsonify(decode(app.image))
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)
    

