import cv2
import numpy as np

imaj = cv2.imread("x://opencv//tankR.png")
gray = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
ret, threshed = cv2.threshold(gray, 131, 255, 0)

cv2.imshow("imaj", imaj)
cv2.imshow("gray", gray)
cv2.imshow("threshed", threshed)

(konturs, _) = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
kontur = max(konturs)
tank = imaj.copy()

cv2.drawContours(tank, [kontur], -1, (0, 255, 0), -1)
cv2.imshow("Tank & Kontur", tank)

M = cv2.moments(kontur)
for item in M.items():
     print(item)

m00 = M["m00"]
m10 = M["m10"]
m01 = M["m01"]
print("\nObje alanı:", m00)

# centroid koordinatı:
cx = round(m10/m00)
cy = round(m01/m00)

cv2.circle(tank, (cx, cy), 5, (0, 0, 255), -1)
cv2.imshow("Centroid: {} x {}".format(cx, cy), tank)

cv2.waitKey()
cv2.destroyAllWindows()
