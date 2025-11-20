import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)

roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200

while True:
    success, img = cap.read()

    cvzone.cornerRect(img, (roi_x, roi_y, roi_width, roi_height))

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        cx, cy = hand["center"]

        if roi_x < cx < roi_x + roi_width and roi_y < cy < roi_y + roi_height:
            print(fingers)
        else:
            pass

    cv2.imshow("Images", img)
    cv2.waitKey(1)
