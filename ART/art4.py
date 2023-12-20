import cv2
import numpy as np

width,height = 1080, 1080
canvas = np.zeros((height,width,3),dtype=np.uint8)

#Background
cv2.rectangle(canvas, (0, 0), (1080, 1080), (255, 82, 140), -1)
cv2.rectangle(canvas, (0, 0), (366, 366), (235, 23, 94), -1)
cv2.rectangle(canvas, (714, 0), (1080, 366), (235, 23, 94), -1)
cv2.rectangle(canvas, (0, 714), (366, 1080), (235, 23, 94), -1)
cv2.rectangle(canvas, (714, 714), (1080, 1080), (235, 23, 94), -1)
cv2.circle(canvas, (180, 180), 165, (255, 82, 140), -1)
cv2.circle(canvas, (180, 894), 165, (255, 82, 140), -1)
cv2.circle(canvas, (894, 183), 165, (255, 82, 140), -1)
cv2.circle(canvas, (894, 894), 165, (255, 82, 140), -1)

#Square Outer
cv2.line(canvas, (775, 636), (540, 770), (0, 0, 0), 6)
cv2.line(canvas, (106, 516), (540, 770), (0, 0, 0), 6)
cv2.line(canvas, (540, 810), (540, 770), (0, 0, 0), 6)
cv2.line(canvas, (106, 516), (540, 269), (0, 0, 0), 6) 
cv2.line(canvas, (980, 516), (540, 269), (0, 0, 0), 6) 
cv2.line(canvas, (980, 516), (980, 558), (0, 0, 0), 6)
cv2.line(canvas, (844, 637), (980, 558), (0, 0, 0), 6) 
cv2.line(canvas, (980, 516), (844, 596), (0, 0, 0), 6) #connect 3 y
cv2.line(canvas, (844, 637), (844, 596), (0, 0, 0), 6) 
cv2.line(canvas, (775, 636), (775, 677), (0, 0, 0), 6) #connect 2 x
cv2.line(canvas, (540, 810), (775, 677), (0, 0, 0), 6)
cv2.line(canvas, (540, 810), (103, 559), (0, 0, 0), 6)
cv2.line(canvas, (103, 516), (103, 559), (0, 0, 0), 6)

cv2.line(canvas, (708, 635), (540, 731), (0, 0, 0), 6) #connect 1 x
cv2.line(canvas, (176, 516), (540, 731), (0, 0, 0), 6)
cv2.line(canvas, (176, 516), (540, 305), (0, 0, 0), 6)
cv2.line(canvas, (913, 516), (540, 305), (0, 0, 0), 6)
cv2.line(canvas, (913, 516), (843, 557), (0, 0, 0), 6) #connect 4 y
cv2.line(canvas, (540, 345), (874, 539), (0, 0, 0), 6)
cv2.line(canvas, (540, 345), (212, 537), (0, 0, 0), 6)
cv2.line(canvas, (540, 345), (540, 305), (0, 0, 0), 6)

#Square Inner
cv2.line(canvas, (843, 557), (540, 384), (0, 0, 0), 6)
cv2.line(canvas, (540, 384), (306, 517), (0, 0, 0), 6)
cv2.line(canvas, (507, 633), (306, 517), (0, 0, 0), 6)
cv2.line(canvas, (507, 633), (507, 522), (0, 0, 0), 6)
cv2.line(canvas, (708, 635), (507, 522), (0, 0, 0), 6)

cv2.line(canvas, (677, 654), (540, 577), (0, 0, 0), 6)
cv2.line(canvas, (540, 688), (540, 577), (0, 0, 0), 6)
cv2.line(canvas, (577, 675), (540, 688), (0, 0, 0), 6)
cv2.line(canvas, (577, 675), (577, 597), (0, 0, 0), 6)
cv2.line(canvas, (305, 557), (540, 688), (0, 0, 0), 6)
cv2.line(canvas, (305, 557), (305, 517), (0, 0, 0), 6)

cv2.line(canvas, (540, 424), (844, 596), (0, 0, 0), 6)
cv2.line(canvas, (540, 424), (377, 517), (0, 0, 0), 6)
cv2.line(canvas, (507, 595), (377, 517), (0, 0, 0), 6)
cv2.line(canvas, (775, 636), (540, 500), (0, 0, 0), 6)
cv2.line(canvas, (509, 519), (540, 500), (0, 0, 0), 6)
cv2.line(canvas, (540, 424), (540, 462), (0, 0, 0), 6)
cv2.line(canvas, (415, 537), (540, 462), (0, 0, 0), 6)
cv2.line(canvas, (844, 635), (540, 462), (0, 0, 0), 6)


canvas = cv2.resize(canvas, None, fx=1/2, fy=1/2)
cv2.imshow("3rd", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()