import cv2
import sys
import pickle

font = cv2.FONT_HERSHEY_PLAIN
frame = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {'person_name' : '1'}
with open("labels.picke", 'rb') as f:
    labels = pickle.load(f)
    labels = {v:k for k,v in labels.items()}
while True:
    _,image = frame.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5
    )

 

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id_, conf = recognizer.predict(roi_gray)
        print(id_)
        print(labels[id_])
        print(conf)
        cv2.putText(image,labels[id_],(x-1,200), font, 5,(0,255,0))

    cv2.imshow("Faces found", image)
    cv2.waitKey(1)
