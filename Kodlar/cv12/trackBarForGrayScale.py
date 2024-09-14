import cv2
import numpy as np

def pass_it(x):
     pass

palet = np.zeros((100,700), dtype = "uint8")
cv2.namedWindow("Renk Paleti")
cv2.createTrackbar("Range", "Renk Paleti", 0, 255, pass_it)

while True:

     cv2.imshow("Renk Paleti", palet)

     g = cv2.getTrackbarPos("Range", "Renk Paleti")

     palet[:,:] = [g] # Kısaca palet[:]= g de yazabilirdik. Tüm satırlar ve tüm sütunlar anlamına gelir

     if cv2.waitKey(1) == ord("q"): # refresh olması için waitKey'e 1 değeri giriyoruz
          break

cv2.destroyAllWindows()
     
