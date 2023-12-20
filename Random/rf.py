import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")


def yuv(img):
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("YUV", yuv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('Y channel', yuv[:, :, 0])
        elif choice == "Y":
            cv2.imshow('U channel', yuv[:, :, 1])
        elif choice == "V":
            cv2.imshow('V channel', yuv[:, :, 2])


def hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("HSV", hsv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('H channel', hsv[:, :, 0])
        elif choice == "Y":
            cv2.imshow('S channel', hsv[:, :, 1])
        elif choice == "V":
            cv2.imshow('V channel', hsv[:, :, 2])


def rotation(image, rot_degree, scaling):
    img1 = image
    rows, col = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((col / 2, rows / 2), rot_degree, scaling)
    img_rotation = cv2.warpAffine(img1, rotation_matrix, (col, rows))
    return img_rotation


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


def yuv(img):
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("YUV", yuv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('Y channel', yuv[:, :, 0])
        elif choice == "Y":
            cv2.imshow('U channel', yuv[:, :, 1])
        elif choice == "V":
            cv2.imshow('V channel', yuv[:, :, 2])


def hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("HSV", hsv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('H channel', hsv[:, :, 0])
        elif choice == "Y":
            cv2.imshow('S channel', hsv[:, :, 1])
        elif choice == "V":
            cv2.imshow('V channel', hsv[:, :, 2])


def hls(img):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


while True:
    kernel = np.ones((5, 5), np.uint8)
    ret, frame = cap.read()

    morph_selection = input("Morph? (Y/N): ").upper()
    if morph_selection == 'N':
        print("")
    elif morph_selection == 'Y':
        print("Morph selections available.")
        print("[1]Erode\n[2]Dilate\n[3]Highlight\n[4]Top Hat\n[5]Black Hat\n[Other]Pass")
        morph_apply = int(input("Select one morph effect: "))
        if morph_apply == 1:
            frame = cv2.erode(frame, kernel, iterations=1)

        elif morph_apply == 2:
            frame = cv2.dilate(frame, kernel, iterations=1)

        elif morph_apply == 3:
            frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)

        elif morph_apply == 4:
            frame = cv2.morphologyEx(frame, cv2.MORPH_TOPHAT, kernel)

        elif morph_apply == 5:
            frame = cv2.morphologyEx(frame, cv2.MORPH_BLACKHAT, kernel)

        elif morph_apply == 6:
            pass
    filter_selection = input("Filter? (Y/N): ").upper()
    print("Available Filters")
    print("[1]Grayscale\n[2]YUV\n[3]HSV\n[4]HLS")
    if filter_selection == "Y":
        filter_apply = int(input("Select one filter effect: "))
        if filter_apply == 1:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Image', gray_frame)

        elif filter_apply == 2:
            frame = yuv(frame)
            cv2.imshow("Image", frame)
            cv2.waitKey(1)

        elif filter_apply == 3:
            frame = hsv(frame)
            cv2.imshow("Image", frame)
            cv2.waitKey(1)

        elif filter_apply == 4:
            frame = hls(frame)
            cv2.imshow("Image", frame)
            cv2.waitKey(1)
        else:
            print("Invalid input.")
    elif filter_selection == "N":
        cv2.imshow("Image", frame)
        cv2.waitKey(1)
    else:
        print("Invalid input.")

    cv2.imshow("Image", frame)
    cv2.waitKey(1)

    c = cv2.waitKey(1)
    if c == 27:
        cv2.destroyAllWindows()
        filename = input("Enter filename for photo taken:")
        cv2.imwrite(f"{filename}.png", frame)
        break

cap.release()