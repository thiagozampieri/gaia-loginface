import cv2
import gaia.utils as cfg
import gaia.resize as resize

def rectangle(frame, rect):
    color = cfg.get_options('color')
    (x, y, w, h) = rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, cfg.get_options('filled'))

def text(frame, text, rect):
    (x, y, w, h) = rect   
    cv2.rectangle(frame, (x - 1, y - 25), (x + 2 + w, y), cfg.get_options('color'), cv2.FILLED)
    cv2.putText(frame, text, (x + 6, y - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), cfg.get_options('filled'))

def face(frame, rect, label_text):
    #if (label[1] / threshold) > 0.9:
    rectangle(frame, rect)
    if label_text != '':
        text(frame, label_text, rect)

def faces(frame, faces):
    for rect in faces:
        face(frame, rect, '')

    frame = resize.scale(frame)
    return frame, faces