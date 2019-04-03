import cv2

def options():
    return {
        "classificator": "data/xml/haarcascade_frontalface_alt.xml",
        "scaleFactor": 1.2,
        "minNeighbors": 5,
        "size": 30,
        "resize": 640,
        "filled": 2,
        "color": (255, 255, 0),
       "interpolation": cv2.INTER_CUBIC,
    }