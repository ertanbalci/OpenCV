import cv2
import numpy as np

def pass_it(x):
     pass

palet = np.zeros((200,600,3), np.uint8)

cv2.namedWindow("Renk Paleti")

cv2.createTrackbar("Blue",  "Renk Paleti",   0, 300, pass_it)
cv2.createTrackbar("Green", "Renk Paleti", 120, 255, pass_it)
cv2.createTrackbar("Red",   "Renk Paleti",   0, 255, pass_it)

while True:
     cv2.imshow("Renk Paleti", palet)

     B = cv2.getTrackbarPos("Blue",   "Renk Paleti")
     G = cv2.getTrackbarPos("Green",  "Renk Paleti")
     R = cv2.getTrackbarPos("Red",    "Renk Paleti")

     if B > 255:
          cv2.setTrackbarPos("Blue",   "Renk Paleti", 255)
          B = 255
     palet[:] = [B, G, R]

     if cv2.waitKey(1) == ord("q"):
          break
cv2.destroyAllWindows()
