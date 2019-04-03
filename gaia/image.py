import numpy as np
import urllib
import cv2
import os

def read(path=None, stream=None, url=None):
    if path is not None:
        image = cv2.imread(path)
    else:
        if url is not None:
            response = urllib.request.urlopen(url)
            data_temp = response.read()

        elif stream is not None:
            data_temp = stream.read()
        image = np.asarray(bytearray(data_temp), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image