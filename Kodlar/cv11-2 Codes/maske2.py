import cv2
import numpy as np
import sys

def mouse_click(event, x, y, flags, param):
     global maske, r
     if event == cv2.EVENT_LBUTTONDOWN:
          cv2.circle(maske, (x, y), r, 255, -1)
          masking = cv2.bitwise_and(imaj, imaj, mask=maske)
          cv2.imshow("imaj", masking)
     if event == cv2.EVENT_RBUTTONDOWN:
          maske = np.zeros(imaj.shape[:2], np.uint8)
          cv2.imshow("imaj", imaj)

     
cv2.namedWindow("imaj")
cv2.setMouseCallback("imaj", mouse_click)

try:
     imaj = cv2.imread(sys.argv[1])
except:
     imaj = cv2.imread("x://foto//orman.png")


maske = np.zeros(imaj.shape[:2], np.uint8)

h, w = imaj.shape[:2]

r = int(w/10)

cv2.imshow("imaj", imaj)

cv2.waitKey()
cv2.destroyAllWindows()
