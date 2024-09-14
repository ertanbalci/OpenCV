import cv2
import numpy as np

# Sarı dörtgen çizelim
pano = np.zeros((500,800,3), dtype="uint8")

cv2.rectangle(pano, (100,100), (600,480), [0,255,255], 5)
cv2.rectangle(pano, (300,30), (400,350), [255,0,255], -1)
cv2.imshow("pano", pano)
cv2.waitKey(0)
cv2.destroyAllWindows()
