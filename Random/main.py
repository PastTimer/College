import cv2
import numpy as np
import filter as f
import morphology as m

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")


while True:
    kernel = np.ones((5, 5), np.uint8)
    ret, frame = cap.read()

    translate_choice = input("Translate? Y/N ").upper()
    if translate_choice == "Y":
        x = input("Enter width")
        y = input("Enter height")
    elif translate_choice == 'N':
        print("")
    else:
        print("Error")

    rotate_choice = input("Rotate? Y/N ").upper()
    if rotate_choice == "Y":
        degree = input("Enter degree of rotation: ")
        scale = input("Enter scale: ")
    elif rotate_choice == 'N':
        print("")
    else:
        print("Error")
    
    morpho = input("Morph? Y/N ").upper()
    if morpho == "N":
        print("")
    elif morpho == "Y":
        choice = input("""Available Transformations:
        a. Erode
        d. Dilate
        c. Highlight
        d. Top hat
        e. Black hat""").lower()
        if choice == "a":
            m.erode(kernel, frame)
        elif choice == "b":
            m.dilate(kernel, frame)
        elif choice == "c":
            m.highlight(kernel, frame)
        elif choice == "d":
            m.tophat(kernel, frame)
        elif choice == "e":
            m.blackhat(kernel, frame)
        else: 
            print("Error")
    else:
        print("Error")

    filter_choice = input("Apply filter? Y/N ").upper()
    if filter_choice == "N":
        cv2.imshow('no filter', frame)
        c = cv2.waitKey(1)
    elif filter_choice == "Y":
        filter = input("""Available filters:
        a. Grayscale
        b. YUV 
        c. HSV
        d. BGR-A
        e. RGB-A
        f. YCR
        g. HLS
        """).lower()

        if filter_choice == "a":
            f.gray(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "b":
            f.yuv(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "c":
            f.hsv(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "d":
            f.bgra(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "e":
            f.rgba(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "f":
            f.ycr(frame)
            c = cv2.waitKey(1)
        elif filter_choice == "g":
            f.hls(frame)
            c = cv2.waitKey(1)
    else:
        print("Error")
    c = cv2.waitKey(1)
    if c == 27: 
        cv2.destroyAllWindows()
        filename = input("Enter filename for photo taken:")
        cv2.imwrite(f"{filename}.png", frame)
        break

cap.release()