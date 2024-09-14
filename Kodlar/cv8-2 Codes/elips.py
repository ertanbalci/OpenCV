import cv2
import numpy as np

# Yeşil pano üzerine elipsler çizelim
pano = np.full((500,800,3), [0,255,0], dtype="uint8")

h, w = pano.shape[:2]
r = int(min(h, w)/2)

cv2.ellipse(pano, (int(w/2-50), int(h/2-50)), (int(r/2), int(r/6)), 45, 0, 360, (0,0,250), -1)
cv2.ellipse(pano, (int(w/2+50), int(h/2+100)), (int(r/2), int(r/6)), 0, 0, 360, (255,0,0), 5)
cv2.ellipse(pano, (int(w/2-250), int(h/2+100)), (int(r/2), int(r/6)), 120, 0, 180, (0,0,0), -1)

cv2.imshow("pano", pano)

cv2.waitKey(0)
cv2.destroyAllWindows()
