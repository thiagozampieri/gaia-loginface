import cv2

def threshold(frame):
    (T,Thresh1) = cv2.threshold(frame, 44, 54, cv2.THRESH_TRUNC)
    (T,Thresh3) = cv2.threshold(Thresh1, 43, 44, cv2.THRESH_BINARY)
    (T,Thresh2) = cv2.threshold(Thresh3, 0 ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    (T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
    return Thresh4

def grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)