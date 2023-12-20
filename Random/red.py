import cv2
import numpy as np

width,height = 1080, 1080
canvas = np.zeros((height,width,3),dtype=np.uint8)

#Background
cv2.rectangle(canvas, (0, 0), (540, 540), (87, 87, 255), -1)
cv2.rectangle(canvas, (540, 540), (1080, 1080), (87, 87, 255), -1)
cv2.rectangle(canvas, (540, 0), (1080, 540), (49, 49, 255), -1)
cv2.rectangle(canvas, (0, 540), (540, 1080), (49, 49, 255), -1)

#First Triangle
cv2.line(canvas, (328, 217), (146, 539), (0, 0, 0), 6)
cv2.line(canvas, (328, 217), (411, 217), (0, 0, 0), 6)
cv2.line(canvas, (536, 417), (411, 217), (0, 0, 0), 6)
cv2.line(canvas, (328, 217), (495, 491), (0, 0, 0), 6)
cv2.line(canvas, (192, 615), (146, 539), (0, 0, 0), 6)
cv2.line(canvas, (192, 615), (427, 615), (0, 0, 0), 6)
cv2.line(canvas, (192, 615), (328, 370), (0, 0, 0), 6)
cv2.line(canvas, (328, 370), (450, 570), (0, 0, 0), 6)
cv2.line(canvas, (429, 536), (327, 536), (0, 0, 0), 6)
cv2.line(canvas, (372, 444), (327, 536), (0, 0, 0), 6)
cv2.line(canvas, (384, 465), (362, 465), (0, 0, 0), 6)

#Second Triangle
cv2.line(canvas, (653, 608), (885, 603), (0, 0, 0), 6)
cv2.line(canvas, (930, 523), (885, 603), (0, 0, 0), 6)
cv2.line(canvas, (930, 523), (650, 530), (0, 0, 0), 6)
cv2.line(canvas, (930, 523), (742, 209), (0, 0, 0), 6)
cv2.line(canvas, (654, 209), (742, 209), (0, 0, 0), 6)
cv2.line(canvas, (654, 209), (800, 453), (0, 0, 0), 6)
cv2.line(canvas, (693, 456), (800, 453), (0, 0, 0), 6)
cv2.line(canvas, (711, 450), (658, 365), (0, 0, 0), 6)
cv2.line(canvas, (654, 209), (315, 822), (0, 0, 0), 6) #1st
cv2.line(canvas, (363, 896), (658, 365), (0, 0, 0), 6) #2nd
cv2.line(canvas, (701, 433), (493, 816), (0, 0, 0), 6) #3rd

#Third Triangle
cv2.line(canvas, (315, 822), (363, 896), (0, 0, 0), 6)
cv2.line(canvas, (731, 892), (363, 896), (0, 0, 0), 6)
cv2.line(canvas, (731, 892), (772, 815), (0, 0, 0), 6)
cv2.line(canvas, (493, 816), (772, 815), (0, 0, 0), 6)
cv2.line(canvas, (628, 569), (772, 815), (0, 0, 0), 6)
cv2.line(canvas, (587, 646), (643, 739), (0, 0, 0), 6)
cv2.line(canvas, (535, 740), (643, 739), (0, 0, 0), 6)
cv2.line(canvas, (546, 717), (560, 740), (0, 0, 0), 6)

canvas = cv2.resize(canvas, None, fx=1/2, fy=1/2)
cv2.imshow("1st", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()