import cv2
import numpy as np

im = cv2.imread("x://opencv//tankL.png")
im = cv2.resize(im, None, fx=.5, fy=.5)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 50, 200)
cv2.imshow("Orj imaj", im)
cv2.imshow("canny", canny)

konturs, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("kontur sayısı:", len(konturs))
zemin = np.ones(im.shape, np.uint8) * 255

for k in konturs:
     imKont = cv2.drawContours(im, [k], 0, (0,255,0), 2)
     cv2.imshow("Kontur", imKont)

     x, y, w, h = cv2.boundingRect(k)
     imaj = imKont.copy()
     cv2.rectangle(imaj, (x, y), (x+w, y+h), (0,0,255), 4)
     cv2.imshow("Straight Box", imaj)

     objeAlanı = cv2.contourArea(k)
     dortgenAlanı = w * h
     print("obje alanı:", objeAlanı, "dörtgen alanı:", dortgenAlanı, "Doluluk Oranı:", float(objeAlanı/dortgenAlanı))

     # minarea
     rect = cv2.minAreaRect(k)
     print("rect\n",rect)
     box = cv2.boxPoints(rect)
     print("box\n",box)
     box = np.int32(box)
     print("box\n",box)

     w = rect[1][0]
     h = rect[1][1]
     rotArea = w * h
     print("dörtgen alanı:", rotArea, "Doluluk Oranı:", float(objeAlanı/rotArea))

     imaj = imKont.copy()
     cv2.drawContours(imaj, [box], 0, (255,0,0), 4)
     cv2.imshow("Rotated Box", imaj)

     # min circle
     imaj = imKont.copy()
     (x, y), yarıçap = cv2.minEnclosingCircle(k)
     merkez = (int(x), int(y))
     yarıçap = int(yarıçap)
     cv2.circle(imaj, merkez, yarıçap, (0,0,255), 4)
     cv2.imshow("Circle", imaj)

     # elips
     elips = cv2.fitEllipse(k)
     print("Elips verileri", elips)
     imaj = imKont.copy()
     cv2.ellipse(imaj, elips, (0,0,255), 4)
     cv2.imshow("Elips", imaj)
     
     cv2.waitKey()

cv2.destroyAllWindows()
     
     
     
     
