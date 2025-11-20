import cv2
import numpy as np

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def findFace(img):
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImg, 1.1, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        cv2.circle(img, (cx, cy), 4, (0, 255, 0), cv2.FILLED)
        area = w * h
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(info, w, pid, pError):

    area = info[1]
    x, y = info[0]
    fb = 0

    error = x - w//2
    speed = pid[0] * error + pid[1] * (error-pError)
    speed = int(np.clip(speed, -100, 100))

    # fb_error = area - (fbRange[0] + fbRange[1]) / 2
    # fb_speed = int(pid[2] * fb_error)

    # left_speed = speed - fb_speed
    # right_speed = speed + fb_speed

    # left_speed = min(max(-100, left_speed), 100)
    # right_speed = min(max(-100, right_speed), 100)

    if area == 0:
        print("Stop")
    elif area > fbRange[1]:
        print("Backward")
    elif area < fbRange[0]:
        print("Forward")

    if speed == 0:
        print("stop")
    elif speed > 0:
        print("Left")
    elif speed < 0:
        print("Right")

    # if x == 0:
    #     speed = 0
    #     error = 0
    print(speed, fb)
    return error

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)
    pError = trackFace(info, w, pid, pError)
    # print("Center", info[0], "Area", info[1])
    cv2.imshow("Images", img)
    cv2.waitKey(1)
