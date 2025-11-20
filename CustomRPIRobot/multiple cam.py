import cv2

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(0)

while True:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()

    if (ret1):
        cv2.imshow("Images1", img1)

    if (ret2):
        cv2.imshow("Images2", img2)

    if(ret3):
        cv2.imshow("Images3", img3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
