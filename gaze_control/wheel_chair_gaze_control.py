import cv2
import cvzone
import dlib
from dlib import get_frontal_face_detector
from math import hypot
import numpy as np

cap = cv2.VideoCapture(0)
detector = get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(pt1, pt2):
    return int((pt1.x + pt2.x)/2), int((pt1.y + pt2.y)/2)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        # x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
        landmarks = predictor(gray, face)

        right_eye_left = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye_right = (landmarks.part(39).x, landmarks.part(39).y)
        hor_line = cv2.line(img, right_eye_left, right_eye_right, (0, 255, 0), 2)

        right_center_top = midpoint(landmarks.part(37), landmarks.part(38))
        right_center_bottom = midpoint(landmarks.part(41), landmarks.part(40))
        ver_line = cv2.line(img, right_center_top, right_center_bottom, (0, 255, 0), 2)

        hor_line_length = hypot((right_eye_left[0] - right_eye_right[0]), (right_eye_left[1] - right_eye_right[1]))
        ver_line_length = hypot((right_center_top[0] - right_center_bottom[0]), (right_center_top[1] -
                                                                                 right_center_bottom[1]))

        ratio = hor_line_length / ver_line_length

        if ratio > 4.5:
            cv2.putText(img, "Blinking", (100, 150), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

        right_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                                     (landmarks.part(37).x, landmarks.part(37).y),
                                     (landmarks.part(38).x, landmarks.part(38).y),
                                     (landmarks.part(39).x, landmarks.part(39).y),
                                     (landmarks.part(40).x, landmarks.part(40).y),
                                     (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        # cv2.polylines(img, [right_eye_region], True, 255, 2)

        height, width, _ = img.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [right_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [right_eye_region], 255)
        right_eye = cv2.bitwise_and(gray, gray, mask=mask)

        min_x = np.min(right_eye_region[:, 0])
        max_x = np.max(right_eye_region[:, 0])
        min_y = np.min(right_eye_region[:, 1])
        max_y = np.max(right_eye_region[:, 1])

        eye_gray = right_eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(eye_gray, 150, 250, cv2.THRESH_BINARY_INV)
        eye = cv2.resize(eye_gray, None, fx=5, fy=5)
        threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
        height, width = threshold_eye.shape
        right_side_threshold = threshold_eye[0: height, 0: int(width/2)]
        left_side_threshold = threshold_eye[0: height, int(width/2): width]
        right_side_count_white = cv2.countNonZero(right_side_threshold)
        left_side_count_white = cv2.countNonZero(left_side_threshold)

        gazeRatio = right_side_count_white / left_side_count_white

        cv2.putText(img, str(gazeRatio), (50, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        if gazeRatio > 1.7:
            cv2.putText(img, "Right", (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        elif 0.95 < gazeRatio < 1.4:
            cv2.putText(img, "Center", (20, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        elif gazeRatio < 0.9:
            cv2.putText(img, "Left", (30, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

        # cv2.imshow("Mask", mask)
        cv2.imshow("rightEye", right_eye)

        cv2.imshow("Thresh", threshold_eye)
        cv2.imshow("rightThreshEye", right_side_threshold)
        cv2.imshow("leftThreshEye", left_side_threshold)

    cv2.imshow("Images", img)
    cv2.waitKey(1)
