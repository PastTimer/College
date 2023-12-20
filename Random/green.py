import cv2
import numpy as np

width,height = 1080, 1080
canvas = np.zeros((height,width,3),dtype=np.uint8)

#Background
cv2.rectangle(canvas, (0, 0), (1080, 540), (9, 73, 0), -1)
cv2.rectangle(canvas, (0, 540), (1080, 1080), (169, 219, 157), -1)
cv2.circle(canvas, (540, 540), 222, (15, 141, 225), -1)

#Right side
cv2.line(canvas, (221, 207), (221, 445), (0, 0, 0), 6)
cv2.line(canvas, (221, 207), (540, 386), (0, 0, 0), 6)
cv2.line(canvas, (221, 207), (170, 235), (0, 0, 0), 6)
cv2.line(canvas, (170, 476), (170, 235), (0, 0, 0), 6) # inter
cv2.line(canvas, (170, 476), (326, 565), (0, 0, 0), 6)
cv2.line(canvas, (225, 632), (326, 565), (0, 0, 0), 6) # inter 2
cv2.line(canvas, (225, 632), (225, 753), (0, 0, 0), 6)
cv2.line(canvas, (540, 571), (225, 753), (0, 0, 0), 6)
cv2.line(canvas, (274, 536), (170, 602), (0, 0, 0), 6)
cv2.line(canvas, (170, 844), (170, 602), (0, 0, 0), 6)
cv2.line(canvas, (170, 844), (222, 873), (0, 0, 0), 6)
cv2.line(canvas, (540, 694), (222, 873), (0, 0, 0), 6)
cv2.line(canvas, (170, 844), (540, 632), (0, 0, 0), 6)
cv2.line(canvas, (540, 444), (277, 300), (0, 0, 0), 6)
cv2.line(canvas, (277, 417), (277, 300), (0, 0, 0), 6)
cv2.line(canvas, (277, 417), (435, 511), (0, 0, 0), 6)
cv2.line(canvas, (435, 570), (435, 511), (0, 0, 0), 6)
cv2.line(canvas, (435, 570), (275, 662), (0, 0, 0), 6)
cv2.line(canvas, (225, 632), (275, 662), (0, 0, 0), 6)
cv2.line(canvas, (275, 720), (275, 662), (0, 0, 0), 6)
cv2.line(canvas, (275, 360), (540, 512), (0, 0, 0), 6)
#Left side
cv2.line(canvas, (540, 444), (801, 300), (0, 0, 0), 6)
cv2.line(canvas, (801, 417), (801, 300), (0, 0, 0), 6)
cv2.line(canvas, (801, 417), (647, 511), (0, 0, 0), 6)
cv2.line(canvas, (647, 570), (647, 511), (0, 0, 0), 6)
cv2.line(canvas, (647, 570), (801, 662), (0, 0, 0), 6)
cv2.line(canvas, (853, 632), (801, 662), (0, 0, 0), 6)
cv2.line(canvas, (801, 720), (801, 662), (0, 0, 0), 6)
cv2.line(canvas, (801, 360), (540, 512), (0, 0, 0), 6)
cv2.line(canvas, (855, 207), (855, 445), (0, 0, 0), 6)
cv2.line(canvas, (855, 207), (540, 386), (0, 0, 0), 6)
cv2.line(canvas, (855, 207), (907, 235), (0, 0, 0), 6)
cv2.line(canvas, (907, 476), (907, 235), (0, 0, 0), 6) # inter
cv2.line(canvas, (907, 476), (753, 565), (0, 0, 0), 6)
cv2.line(canvas, (853, 632), (753, 565), (0, 0, 0), 6) # inter 2
cv2.line(canvas, (853, 632), (853, 753), (0, 0, 0), 6)
cv2.line(canvas, (540, 571), (853, 753), (0, 0, 0), 6)
cv2.line(canvas, (805, 536), (907, 602), (0, 0, 0), 6)
cv2.line(canvas, (907, 844), (907, 602), (0, 0, 0), 6)
cv2.line(canvas, (907, 844), (853, 873), (0, 0, 0), 6)
cv2.line(canvas, (540, 694), (853, 873), (0, 0, 0), 6)
cv2.line(canvas, (907, 844), (540, 632), (0, 0, 0), 6)

#Lines
cv2.line(canvas, (540, 571), (540, 632), (0, 0, 0), 6)
cv2.line(canvas, (540, 386), (540, 444), (0, 0, 0), 6)
cv2.line(canvas, (907, 476), (856, 450), (0, 0, 0), 6)
cv2.line(canvas, (170, 476), (222, 446), (0, 0, 0), 6)
cv2.line(canvas, (647, 570), (856, 450), (0, 0, 0), 6)
cv2.line(canvas, (435, 570), (222, 446), (0, 0, 0), 6)

canvas = cv2.resize(canvas, None, fx=1/2, fy=1/2)
cv2.imshow("2nd", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()