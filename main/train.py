import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"images")
cascPath = "C:/Users/Andrew Cao/Desktop/test image/main/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.face.LBPHFaceRecognizer_create()
current_id = 0
label_ids = {}
x_train = []
y_labels = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("JPG") or file.endswith("jpg"):
            path = os.path.join(root, file)
            print(path)
            label = os.path.basename(root)
            print(label)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print id_
            pil_image = Image.open(path).convert("L")#grayscale
            image_array = np.array(pil_image,"uint8")
            faces = faceCascade.detectMultiScale(image_array, scaleFactor =1.5,minNeighbors=5)
            
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")