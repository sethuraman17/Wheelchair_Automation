import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 94, 140])
    upper_yellow = np.array([48, 255, 255])
    mask = cv2.inRange(hsvImg, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contours = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contours)

        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            if cx < img.shape[1] / 2:
                print("Turn Left")
            else:
                print("Turn Right")

            print("Move Forward")

    else:
        print("Stop")

    cv2.imshow("Images", img)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)
