import cv2
import gaia.utils as cfg

def scale(frame):
    alt = int(frame.shape[0]/frame.shape[1]*cfg.get_options('resize'))
    return image(frame, cfg.get_options('resize'), alt)

def image(gray, width, height):
    return cv2.resize(gray, (width, height), interpolation = cfg.get_options('interpolation')) 

def compare(gray, rect):
    factor = cfg.get_options('size')
    (x, y, w, h) = rect
    gray = image(gray[y:y+h,x:x+w], factor, factor)    
    return gray