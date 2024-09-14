import cv2
import numpy as np

# Beyaz pano üzerine poligon çizelim
pano = np.zeros((400,400,3), dtype="uint8") + 255

pts = np.array([[200,50],[300,150],[100,150]], np.int32)

#pts= pts.reshape(-1,1,2)

cv2.polylines(pano, [pts], True, (0,0,255), 7)

cv2.polylines(pano, [pts], False, (0,255,255), 7)

pts = np.array([[200,20],[350,100],[300,200], [100,200], [50,100]], np.int32)
#pts = pts.reshape(-1,1,2)

cv2.polylines(pano, [pts], False, (255,0,255), 7)
cv2.imshow("pano", pano)

cv2.waitKey(0)
cv2.destroyAllWindows()
