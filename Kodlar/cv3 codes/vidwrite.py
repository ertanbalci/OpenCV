import cv2
import numpy as np
# https://www.fourcc.org/codecs.php
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if camera.isOpened():
     w = int(camera.get(3)) # float döndürür. # camera.get(cv2.CAP_PROP_FRAME_WIDTH)
     h = int(camera.get(4)) # float döndürür. # camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
else: print("Kamera açılamadı!")

fourcc = cv2.VideoWriter_fourcc('X','2','6','4') #(*'FMP4')
out = cv2.VideoWriter("out.mp4",fourcc, 30.0, (w, h), False)

while camera.isOpened():
     ret, frame = camera.read()
     if ret:
          cv2.imshow("video",frame)
          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
          out.write(frame)
     else:print("Frame okunmadı!")
     
     if cv2.waitKey(1) & 0xFF == ord("q"): break
     
camera.release()
out.release()
cv2.destroyAllWindows()
