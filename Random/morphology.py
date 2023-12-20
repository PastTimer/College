import cv2

def erode(kernel, img):
    frame = cv2.erode(img, kernel, iterations=1)
    return frame

def dilate(kernel, img):
    frame = cv2.dilate(img, kernel, iterations=1)
    return frame

def highlight(kernel, img):
    frame = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    return frame

def tophat(kernel, img):
    frame = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    return frame

def blackhat(kernel, img):
    frame = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    return frame

