import numpy as np
import urllib.request as urllib
import cv2
import requests
import gaia.draw as draw
import json
from json import JSONDecoder
import gaia.utils as utils

url = "http://localhost:8000/face_detector/"
 
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image


image_to_read = url_to_image("https://pbs.twimg.com/profile_images/466585535272611840/sjuMzLr4_400x400.png")
tracker = {"url": "https://pbs.twimg.com/profile_images/466585535272611840/sjuMzLr4_400x400.png"}
req = requests.post(url, data=tracker).json()
print
"image3.png: {}".format(req)

for i in range(len(req["faces"])):
	user = (json.loads(req["users"][i]))
	label_text = (user['fullname'])
    #cv2.rectangle(image_to_read,(w,x), (y,z), (0, 255, 0), 2)
	draw.face(image_to_read, req["faces"][i], label_text)

cv2.imshow("image1.jpg", image_to_read)
cv2.waitKey(0)