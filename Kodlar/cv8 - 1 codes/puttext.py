import cv2
import numpy as np

pano = np.zeros((400,400,3), np.uint8)

#font = cv2.FONT_HERSHEY_SIMPLEX
x = y = 30
text = "OpenCV Text"
fscale = 1
kalınlık =1
renk = (255,255,255)
çizgitipi = cv2.LINE_AA

for i in range(8):
     font = i
     cv2.putText(pano, text, (x,y), font, fscale, renk, kalınlık, çizgitipi)
     y = y + 40

cv2.imshow("Kara Tahta", pano)

cv2.waitKey()
cv2.destroyAllWindows()
