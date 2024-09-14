import cv2
import numpy as np

s = float(input("Eğme katsayısı? : "))
eksen = input("eğme ekseni x veya y girin:" ) #xX

imaj = cv2.imread("vosvos.jpg")
height, width =imaj.shape[:2]
cv2.imshow("orijinal", imaj)

yeni_imaj = np.zeros_like(imaj) 

for i in range(height):
     for j in range(width):
          pValue = imaj[i, j]
          
          if eksen in "xX":
               j2 = int(j + s * i) #sütun
               i2 = i              #satır
          else:
               j2 = j              #sütun
               i2 = int(i + s * j) #satır

          if height>i2>0 and width>j2>0:
               yeni_imaj[i2, j2] = pValue

cv2.imshow("shear imaj", yeni_imaj)
cv2.waitKey(0)
cv2.destroyAllWindows()
