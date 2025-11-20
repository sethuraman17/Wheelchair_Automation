import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1, detectionCon=0.8)

while True:
    success, img = cap.read()
    hands, img = detect.findHands(img)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        bbox = hand["bbox"]
        fingers = detect.fingersUp(hand)
        if fingers == [1, 1, 1, 1, 1]:
            print("Move Forward")
        if fingers == [0, 0, 0, 0, 0]:
            print("Move Backward")
        elif fingers == [1, 0, 0, 0, 0]:
            print("Turn Left")
        elif fingers == [0, 0, 0, 0, 1]:
            print("Turn Right")
    cv2.imshow("Images", img)
    cv2.waitKey(1)
