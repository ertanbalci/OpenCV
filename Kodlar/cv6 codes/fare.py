import cv2
import numpy as np
import sys

def panom():
     try:
          pano = cv2.imread(sys.argv[1])
     except:
          pano = np.zeros((470,640,3), dtype="uint8")
     return pano

def mouse_click(events, x, y, flags, param):
     global pano, x11, x22, y22, y11, x1, y1
     if events == cv2.EVENT_LBUTTONDOWN:
          BGR = pano[y, x]
          fc = (0,0,255) # yazı rengi kırmızı
          text = "[{}, {}]: {}".format(x, y, BGR)
          cv2.putText(pano, text, (x,y), cv2.FONT_ITALIC, .5, fc)
     elif events == cv2.EVENT_RBUTTONDOWN:
          x1 = x
          y1 = y
     elif events == cv2.EVENT_RBUTTONUP:
          x2 = x
          y2 = y
          cv2.rectangle(pano, (x1, y1), (x2, y2), (0,255,255), 2)
     elif events == cv2.EVENT_MBUTTONDOWN:
          # doğrunun başlangıç noktası önceki koordinatlar x11, y11 (önceki event)
          # doğrunun bitiş noktası son koordinatlar x22, y22 (son event)
          x11 = x22
          y11 = y22
          x22 = x
          y22 = y
          if x11 > -1:
               cv2.line(pano, (x11, y11), (x22, y22), (255, 0,0), 3)
     elif events == cv2.EVENT_LBUTTONDBLCLK:
          pano = panom()
     cv2.imshow("pano", pano) 

x11 = y11 = x22 = y22 = -1
       
pano = panom()

cv2.namedWindow("pano")
cv2.setMouseCallback("pano", mouse_click)

cv2.imshow("pano", pano)

k = cv2.waitKey()
if k ==27: # esc
     cv2.destroyAllWindows()
     
cv2.destroyAllWindows()  
