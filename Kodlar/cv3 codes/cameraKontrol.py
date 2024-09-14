import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fsize = 0.5
key = ""

while cap.isOpened():
     ret, frame = cap.read()
     frame = cv2.resize(frame, None, fx=fsize, fy=fsize)

     if key == "g":
          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     c = cv2.waitKey(1)

     if c == 27: break # esc
     if c == ord("g"): key = "g"
     if c == ord("b"): key = "b"
     if c == 43: # + tuşuna basıldıysa
          fsize = fsize + 0.05
          out = cv2.resize(frame, None, fx=fsize, fy=fsize)
          c = "" # c'nin değerini değiştermezsek her döngüde frame otomatik olarak yeniden büyütülür.
     elif c == 45: # - tuşuna basıldıysa
          fsize = fsize - 0.05
          if fsize < 0.2:
               fsize = 0.2
          out = cv2.resize(frame, None, fx=fsize, fy=fsize)
          c = "" # c'nin değerini değiştermezsek her döngüde frame otomatik olarak yeniden küçültülür.
     else:
          out = frame
     cv2.imshow("WebCam", out)

cap.release()
cv2.destroyAllWindows()
