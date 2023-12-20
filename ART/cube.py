import cv2
import numpy as np

width,height = 600,600
canvas = np.zeros((height,width,3),dtype=np.uint8)

p1 = (100,200)
p2 = (100,500)
p3 = (400,500)
p4 = (400,200)
p5 = (200,100)
p6 = (200,400)
p7 = (500,400)
p8 = (500,100)

##Back Square
cv2.line(canvas,p5,p6,(50,50,50),6)
cv2.line(canvas,p6,p7,(50,50,50),6)
cv2.line(canvas,p7,p8,(50,50,50),6)
cv2.line(canvas,p8,p5,(50,50,50),6)

##Connectors
cv2.line(canvas,p1,p5,(125,125,125),6)
cv2.line(canvas,p2,p6,(125,125,125),6)
cv2.line(canvas,p3,p7,(125,125,125),6)
cv2.line(canvas,p4,p8,(125,125,125),6)

##Front Square
cv2.line(canvas,p1,p2,(255,255,255),6)
cv2.line(canvas,p2,p3,(255,255,255),6)
cv2.line(canvas,p3,p4,(255,255,255),6)
cv2.line(canvas,p4,p1,(255,255,255),6)

cv2.imshow("Cube",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()