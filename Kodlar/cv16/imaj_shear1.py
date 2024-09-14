import cv2
import numpy as np

s = float(input("Eğme katsayısı? : "))
eksen = input("eğme ekseni x veya y girin:" )

# read image
#imaj = cv2.imread("vosvos.jpg")
imaj = cv2.imread("lenna.jpg")

height, width =imaj.shape[:2]
cv2.imshow("orijinal", imaj)

if eksen in "xX":
     sm =np.float32([[1, s, 0],[0, 1, 0]])
else:
     sm =np.float32([[1, 0, 0],[s, 1, 0]])
     
yeni_imaj = cv2.warpAffine(imaj, sm, (width, height))

cv2.imshow("shear imaj", yeni_imaj)
cv2.waitKey(0)
cv2.destroyAllWindows()

