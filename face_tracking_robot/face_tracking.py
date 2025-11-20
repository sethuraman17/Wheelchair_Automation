import cv2
import numpy as np

# Motor Control Setup
# You will need to replace these with the actual motor control code for your robot
def move_forward():
    print("Moving Forward")

def move_backward():
    print("Moving Backward")

def turn_left():
    print("Turning Left")

def turn_right():
    print("Turning Right")

# Face Detection and Tracking Setup
w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0.01]
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

    # Proportional control for left-right movement
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    # Proportional control for forward-backward movement
    fb_error = area - (fbRange[0] + fbRange[1]) / 2  # Using average of fbRange as desired area
    fb_speed = int(pid[2] * fb_error)

    # Combine left-right and forward-backward movements
    left_speed = speed - fb_speed
    right_speed = speed + fb_speed

    # Limit the speed range and direction
    left_speed = min(max(-100, left_speed), 100)
    right_speed = min(max(-100, right_speed), 100)

    return error

# Main Loop
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)

    # Motor Control based on Face Tracking
    if info[1] != 0:
        pError = trackFace(info, w, pid, pError)

        if info[0][0] < w // 2:
            turn_right()
        else:
            turn_left()

        if info[1] > fbRange[1]:
            move_backward()
        elif info[1] < fbRange[0]:
            move_forward()

    cv2.imshow("Images", img)
    cv2.waitKey(1)
