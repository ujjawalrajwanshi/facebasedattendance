import cv2
import os
from datetime import datetime


def markAttendance(name,id):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{id},{name},{dtString}')


def Test():
    path = 'ImagesAttendance'
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Trained/trainer.yml')
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)
    minW = 0.1 * camera.get(3)
    minH = 0.1 * camera.get(4)

    while True:
        ret, img = camera.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 100):
                for imagePath in imagePaths:
                    if int(os.path.split(imagePath)[-1].split(".")[1]) == id:
                        name = str(os.path.split(imagePath)[-1].split(".")[0])
                confidence = "  {0}%".format(round(100 - confidence))
            markAttendance(name,id)
            cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        cv2.imshow('camera', img)


