import cv2
import numpy as np

logo = cv2.imread("x://opencv//cv2_logo.png")
#cv2.imshow("logo", logo)

rh, rw = logo.shape[:2]

gri_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
rv, maske = cv2.threshold(gri_logo, 250,255, cv2.THRESH_BINARY_INV)
ters_maske = cv2.bitwise_not(maske)
fg_logo = cv2.bitwise_and(logo, logo, mask=maske)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
     ret, frame = cap.read()

     if ret:
          roi = frame[0:rh, 0:rw]
          bg_logo = cv2.bitwise_and(roi, roi, mask=ters_maske)
          myLogo =cv2.add(bg_logo, fg_logo)
          frame[0:rh, 0:rw] = myLogo
          cv2.imshow("Video", frame)

     if cv2.waitKey(1) == ord("q"):
          break

cap.release()
cv2.destroyAllWindows()
          
