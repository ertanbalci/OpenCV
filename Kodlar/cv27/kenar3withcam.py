import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while camera.isOpened():
     ret, frame = camera.read()
     if ret:
          frame = cv2.resize(frame, None, fx=.5, fy=.5)
          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          blrFrame = cv2.GaussianBlur(frame, (7,7), 0)
          lapFrame = cv2.Laplacian(blrFrame, cv2.CV_64F)
          canFrame = cv2.Canny(frame, 50, 150)
          cv2.imshow("Gray Blur Frame", blrFrame)
          cv2.imshow("Laplace Frame", lapFrame)
          cv2.imshow("Canny Frame", canFrame)

          if cv2.waitKey(1) == 27: # esc
               break

camera.release()
cv2.destroyAllWindows()
          
