import cv2 as cv
import numpy as np

def nothing(x):
    pass

# Create a window
cv.namedWindow('Testing 2')

# Create trackbars for each filter
cv.createTrackbar('Grayscale', 'Testing 2', 0, 1, nothing)
cv.createTrackbar('HSV Channel (0-H, 1-S, 2-V)', 'Testing 2', 0, 4, nothing)
cv.createTrackbar('Blur', 'Testing 2', 0, 10, nothing)
cv.createTrackbar('Canny Edge', 'Testing 2', 0, 1, nothing)

camera = cv.VideoCapture(0)  # Use the default camera (index 0)

if not camera.isOpened():
    raise IOError("Camera not accessed.")

while True:
    grayscale = cv.getTrackbarPos('Grayscale', 'Testing 2')
    channel = cv.getTrackbarPos('HSV Channel (0-H, 1-S, 2-V)', 'Testing 2')
    blur = cv.getTrackbarPos('Blur', 'Testing 2')
    edge = cv.getTrackbarPos('Canny Edge', 'Testing 2')
    
    ret, frame = camera.read()
    key = cv.waitKey(1)

    # Apply filters based on trackbar settings
    if grayscale == 1:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if channel != 0:
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        if channel == 1:
            frame = hsv_frame[:, :, 0]  
        elif channel == 2:
            frame = hsv_frame[:, :, 1]  
        elif channel == 3:
            frame = hsv_frame[:, :, 2]
        elif channel == 4:
            frame = hsv_frame
    if blur > 0:
        frame = cv.GaussianBlur(frame, (2 * blur + 1, 2 * blur_level + 1), 0)
    if edge == 1:
        frame = cv.Canny(frame, 100, 200)

    cv.imshow("Image", frame)
    
    if key == 27:
        break

camera.release()
cv.destroyAllWindows()