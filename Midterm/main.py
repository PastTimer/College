import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot proceed")

current_filter = None
current_morph = None
x = 1000
y = 1000
xi = 0
yi = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (x, y))
    key = cv2.waitKey(1)
    kernel = None
    trans = np.float32([[1, 0, xi], [0, 1, yi]])

    if key == ord('0'):
        filename = input("Enter name: ")
        cv2.imwrite(f"{filename}.png", frame)
        break
    elif key == ord('o'):
        x += 10
        y += 10
    elif key == ord('p'):
        x -= 10
        y -= 10
    elif key == ord('d'):
        xi += 10
    elif key == ord('a'):
        xi -= 10
    elif key == ord('w'):
        yi += 10
    elif key == ord('s'):
        yi -= 10
    elif key == ord('1'):
        current_morph = cv2.MORPH_GRADIENT
        kernel = np.ones((5, 5), np.uint8)
    elif key == ord('2'):
        current_morph = cv2.MORPH_BLACKHAT
        kernel = np.ones((5, 5), np.uint8)
    elif key == ord('3'):
        current_morph = cv2.MORPH_CLOSE
        kernel = np.ones((5, 5), np.uint8)
    elif key == ord('4'):
        current_morph = cv2.MORPH_CROSS
        kernel = np.ones((5, 5), np.uint8)
    elif key == ord('5'):
        current_morph = cv2.MORPH_ERODE
        kernel = np.ones((5, 5), np.uint8)
    elif key == ord('j'):
        current_filter = cv2.COLOR_BGR2LUV
    elif key == ord('b'):
        current_filter = cv2.COLOR_BGR2GRAY
    elif key == ord('c'):
        current_filter = cv2.COLOR_BGR2HSV
    elif key == ord('k'):
        current_filter = cv2.COLOR_BGR2YUV
    elif key == ord('e'):
        current_filter = cv2.COLOR_BGR2RGB
    elif key == ord('f'):
        current_filter = cv2.COLOR_BGR2HLS
    elif key == ord('g'):
        current_filter = cv2.COLOR_BGR2LAB
    elif key == ord('h'):
        current_filter = cv2.COLOR_BGR2XYZ
    elif key == ord('i'):
        current_filter = None
        current_morph = None
    elif key == 27:
        break

    frame = cv2.resize(frame, (x, y))
    frame = cv2.warpAffine(frame, trans, (1000, 1000))
    frame = cv2.cvtColor(frame, current_filter)
    frame = cv2.morphologyEx(frame, current_morph, kernel)

    cv2.imshow("Image", frame)

cap.release()
cv2.destroyAllWindows()
