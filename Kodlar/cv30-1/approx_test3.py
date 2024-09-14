import cv2
import numpy as np

imaj = cv2.imread("x://opencv//shp6.png") # tankR.png
gray = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 50, 200)
cv2.imshow("Yuklenen imaj", imaj)
cv2.imshow("canny", canny)
kontur, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("kontur sayısı:", len(kontur))
zemin = np.ones(imaj.shape, np.uint8) * 255 # beyaz zemin

for k in kontur:
     imaj2 = imaj.copy()
     d = cv2.isContourConvex(k)
     cv2.drawContours(imaj2, [k], 0, (0,255,0), 5)
     cv2.imshow("Kontur Konvex mi?: {}".format(d), imaj2)

     hull = cv2.convexHull(k)
     d = cv2.isContourConvex(hull)
     cv2.drawContours(imaj2, [hull], 0, (0,0,255), 5)
     cv2.imshow("Hull Konvex mi?: {}".format(d), imaj2)

     cv2.drawContours(zemin, [hull], 0, (0,0,255), 5)
     cv2.imshow("Duzeltilmis imaj", zemin)

cv2.waitKey()
cv2.destroyAllWindows()

     
     
