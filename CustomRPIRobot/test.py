import cv2
import numpy as np

def color_detection(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
    block_size = 11
    constant = 2
#
    _, _, v = cv2.split(img_hsv)
    threshold_value = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
#
    cv2.imshow("Image", threshold_value)
#
    return threshold_value

# def color_detection(img):
#     img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     # Adaptive thresholding parameters
#     block_size = 5  # Size of the neighborhood for thresholding
#     constant = 2     # Constant subtracted from the mean for thresholding
#
#     # Adaptive thresholding for white color detection
#     threshold_value = cv2.adaptiveThreshold(img_hsv[:, :, 2], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
#
#     cv2.imshow("Image", threshold_value)


    return threshold_value
if __name__ == "__main__":
    cap = cv2.VideoCapture('test1.mp4')
    frame_count = 0
    while True:
        frame_count += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frame_count:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frame_count = 0
        success, img = cap.read()
        img = cv2.resize(img, (460, 340))
        color_detection(img)
        cv2.imshow("Images", img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
