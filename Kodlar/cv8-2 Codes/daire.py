import cv2
import numpy as np

# Sarı pano üzerine mavi çember çizelim
pano = np.zeros((500,800,3), dtype="uint8")
sarı = np.array([0,255,255], dtype="uint8")
spano = pano + sarı

h, w = spano.shape[:2]

r = int(min(h, w)/2)

cv2.circle(spano, (int(w/2), int(h/2)), r, (255,0,0), 5)

cv2.imshow("pano", spano)

cv2.waitKey(0)

cv2.circle(spano, (int(w/2), int(h/2)), r, (0,0,0), -1)
cv2.imshow("pano", spano)

cv2.waitKey(0)
cv2.destroyAllWindows()
