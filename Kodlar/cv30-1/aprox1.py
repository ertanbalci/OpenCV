import cv2
import numpy as np

imaj = cv2.imread("x://opencv//tankR.png")
gray = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY) 
canny = cv2.Canny(gray, 50, 200)

cv2.imshow("imaj", imaj)
cv2.imshow("gray", gray)
cv2.imshow("canny", canny)

(konturs, _) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

tank = imaj.copy()
zemin = np.zeros(imaj.shape, np.uint8)

for k in konturs:
     alan = cv2.contourArea(k)
     cevre = cv2.arcLength(k, True)

     epsilon = 0.002 * cevre
     approx = cv2.approxPolyDP(k, epsilon, True)
     print(approx)
     cv2.drawContours(zemin, [approx], 0, (255,255,255), 2)

     winname="Area: {} Perimeter: {}".format(alan, cevre)
     cv2.imshow(winname, zemin)
     cv2.waitKey()
cv2.destroyAllWindows()
