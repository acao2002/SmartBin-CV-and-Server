import pyzbar.pyzbar as pyzbar
import random
from flask import Flask, render_template, Response, jsonify
from QRcodecamera import VideoCamera
import json

app = Flask(__name__)

 
  

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:      
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def generate(camera):
 
        value = camera.get_im()
        x = value[0]
        data = { 'angle' : x }
        js = json.dumps(data)
        return js
        
@app.route('/position_feed')
def position_feed():
    
    return Response(generate(VideoCamera()), status=200,
                    mimetype='application/json')
    
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)
    

