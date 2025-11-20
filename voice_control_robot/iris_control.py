import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from math import hypot
import numpy as np
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1, minDetectionCon=0.8)

keyboard = np.zeros((600, 1000, 3), np.uint8)
board = np.zeros((500, 500, 3), np.uint8)

keys_set = {0: "I", 1: "Don't", 2: "ok!", 3: "Yes", 4: "No",
            5: "car", 6: "want", 7: "Help", 8: "Come", 9: "Water",
            10: "am", 11: "Go", 12: "ok!", 13: "need", 14: "Fine"}

def letter(letter_index, text, letter_light):
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 200
        y = 0
    elif letter_index == 2:
        x = 400
        y = 0
    elif letter_index == 3:
        x = 600
        y = 0
    elif letter_index == 4:
        x = 800
        y = 0
    elif letter_index == 5:
        x = 0
        y = 200
    elif letter_index == 6:
        x = 200
        y = 200
    elif letter_index == 7:
        x = 400
        y = 200
    elif letter_index == 8:
        x = 600
        y = 200
    elif letter_index == 9:
        x = 800
        y = 200
    elif letter_index == 10:
        x = 0
        y = 400
    elif letter_index == 11:
        x = 200
        y = 400
    elif letter_index == 12:
        x = 400
        y = 400
    elif letter_index == 13:
        x = 600
        y = 400
    elif letter_index == 14:
        x = 800
        y = 400


    width = 200
    height = 200
    th = 3
    if letter_light == True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 0, 0), th)

    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 3
    font_thick = 3
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_thick)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_thick)


frames = 0
letter_index = 0
blinking_frames = 0
text = ""

while True:
    success, img = cap.read()
    keyboard[:] = (0, 0, 0)
    frames += 1
    active_letter = keys_set[letter_index]
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]

        left_right = face[243]
        left_left = face[130]
        left_up = face[27]
        left_down = face[23]

        cv2.circle(img, left_left, 2, (255, 0, 255), 2)
        cv2.circle(img, left_right, 2, (255, 0, 255), 2)
        cv2.circle(img, left_up, 2, (255, 0, 255), 2)
        cv2.circle(img, left_down, 2, (255, 0, 255), 2)

        hor_line = cv2.line(img, left_left, left_right, (0, 255, 0), 2)
        ver_line = cv2.line(img, left_up, left_down, (0, 255, 0), 2)

        hor_line_length = hypot((left_left[0] - left_right[0]), (left_left[1] - left_right[1]))
        ver_line_length = hypot((left_up[0] - left_down[0]), (left_up[1] - left_down[1]))

        ratio = hor_line_length / ver_line_length

        if ratio > 2.8:
            cv2.putText(img, "Blinking", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            blinking_frames += 1
            frames -= 1
            text += active_letter
            time.sleep(1)
        else:
            blinking_frames = 0

        # right_left = face[463]
        # right_right = face[359]
        # right_up = face[257]
        # right_down = face[253]
        #
        # cv2.circle(img, right_left, 2, (255, 0, 255), 2)
        # cv2.circle(img, right_right, 2, (255, 0, 255), 2)
        # cv2.circle(img, right_up, 2, (255, 0, 255), 2)
        # cv2.circle(img, right_down, 2, (255, 0, 255), 2)
        #
        # cv2.line(img, right_left, right_right, (0, 255, 0), 2)
        # cv2.line(img, right_up, right_down, (0, 255, 0), 2)

        if frames == 20:
            letter_index += 1
            frames = 0
        if letter_index == 14:
            letter_index = 0

        for i in range(15):
            if i == letter_index:
                light = True
            else:
                light = False
            letter(i, keys_set[i], light)

        cv2.putText(board, text, (20, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))

    cv2.imshow("virtual", keyboard)
    cv2.imshow("text", board)
    cv2.imshow("Images", img)
    cv2.waitKey(1)
