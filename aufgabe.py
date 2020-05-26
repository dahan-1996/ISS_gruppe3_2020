import numpy as np
import urllib
import cv2
image=cv2.imread("apple1.jpg")
img_encode=cv2.imencode(".jpg",image)[1]
print(type(img_encode))
data_encode = np.array(img_encode)
print(type(data_encode))
str_encode = data_encode.tostring()
print(type(str_encode))

with open('img_encode.txt','w') as f:
    f.write(str_encode)
    f.flush()

with open('img_encode.txt','r') as f:
    str_encode=f.read()


nparr = np.fromstring(str_encode, np.uint8)
img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imshow("img_decode", img_decode)
cv2.waitKey()
