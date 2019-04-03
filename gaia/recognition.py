
import cv2
import gaia.resize as resize
import gaia.utils as cfg
import gaia.filter as filter

def face_recognizer():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    return face_recognizer

def face_cascade():
    return cv2.CascadeClassifier(cfg.get_options('classificator'))

def recognition(frame):
    cascade = face_cascade()
    
    frame = filter.grayscale(frame)

    minSize = (cfg.get_options('size'), cfg.get_options('size'))
    
    faces = cascade.detectMultiScale(
        frame, 
        scaleFactor = cfg.get_options('scaleFactor'), 
        minNeighbors = cfg.get_options('minNeighbors'), 
        minSize = minSize, 
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    return frame, faces

def detect_face(frame):
    (gray, faces) = recognition(frame)
    if (len(faces) == 0):
        return None, None

    gray = resize.compare(gray, faces[0])    
    return gray, faces[0]