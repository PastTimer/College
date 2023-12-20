import cv2

def gray(img):
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def yuv(img):
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("YUV", yuv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('Y channel', yuv[:,:,0])
        elif choice == "Y":
            cv2.imshow('U channel', yuv[:,:,1])
        elif choice == "V":
            cv2.imshow('V channel', yuv[:,:,2])

def hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plain = input("Display specific channel? Y/N").upper()
    if plain == "N":
        cv2.imshow("HSV", hsv)
    elif plain == "Y":
        choice = input("Enter channel no. ")
        if choice == "Y":
            cv2.imshow('H channel', hsv[:,:,0])
        elif choice == "Y":
            cv2.imshow('S channel', hsv[:,:,1])
        elif choice == "V":
            cv2.imshow('V channel', hsv[:,:,2])

def bgra(img):
    bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    cv2.imshow("BGR-A", bgra)

def rgba(img):
    rgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    cv2.imshow("RGB-A", rgba)

def ycr(img):
    ycr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("BGR2YCrCb", ycr)

def hls(img):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    cv2.imshow("HLS", hls)