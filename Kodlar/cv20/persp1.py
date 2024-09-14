import cv2
import numpy as np

imaj = cv2.imread("x://opencv//aspirin.png")
h, w = imaj.shape[:2]
h = h-1
w = w-1
cv2.imshow("orj", imaj)

# perspektif dönüşüm:
p1 = np.float32([[0, 0], [0, h], [w,    0], [w,      h]])
p2 = np.float32([[0, 0], [0, h], [w, h//3], [w, 2*h//3]])
p3 = np.float32([[w//3, 0], [0, h], [2*w//3, 0], [w, h]])

pm = cv2.getPerspectiveTransform(p1, p2)
print("Perspektif dönüşüm matrisi:\n", pm)
persp = cv2.warpPerspective(imaj, pm, (w, h))
cv2.imshow("perspektif", persp)

pm2 = cv2.getPerspectiveTransform(p1, p3)
print("Perspektif dönüşüm matrisi:\n", pm2)
persp2 = cv2.warpPerspective(imaj, pm2, (w, h))
cv2.imshow("perspektif 2", persp2)

cv2.waitKey()
cv2.destroyAllWindows() 
