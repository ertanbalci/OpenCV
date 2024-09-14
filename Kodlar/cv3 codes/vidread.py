import cv2
import numpy as np

cap = cv2.VideoCapture("out.mp4")
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while (cap.isOpened()):
     
     ret, frame = cap.read()

     if ret:
          cv2.imshow("video",frame)
     
     if cv2.waitKey(25) & 0xFF == ord("q"):
          break

cap.release()
cv2.destroyAllWindows() 
     
