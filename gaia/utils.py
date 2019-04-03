import re
import cv2
import gaia.config as cfg
from json import JSONEncoder

def natural_sort_key(s):
    _nsre = re.compile('([0-9]+)')
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]   

def get_options (code):
    opt = cfg.options()
    return opt[code]

def face_recognizer():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    return face_recognizer

def isset(nameVar):
    return nameVar in globals()

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__   