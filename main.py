import cv2
import numpy as np
import face_recognition

imgElon =face_recognition.load_image_file("ImageBasic/Elon Musk.jpg")
imgElon=cv2.cvtColor(imgElon.cv2.COLOR_BGR2RGB)

imgTest =face_recognition.load_image_file("ImageBasic/Elon test.jpg.jpg")
imgTest=cv2.cvtColor(imgTest.cv2.COLOR_BGR2RGB)


cv2.imshow("Elon Mask",imgElon)
cv2.imshow("Elon Test",imgTest)
cv2.waitkey(0)