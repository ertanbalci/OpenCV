import cv2
import numpy as np

s1 = float(input("Yatay eksen ölçeği: "))
s2 = float(input("Dikey eksen ölçeği: "))

if not s2: s2 = s1

imaj = cv2.imread("lenna.png")
cv2.imshow("lenna", imaj)

w = imaj.shape[1]
h = imaj.shape[0]

rs = np.float32([[s1,0,0],[0,s2,0]])

nw = int(w * s1)
nh = int(w * s2)

yeni_imaj = cv2.warpAffine(imaj, rs, (nw, nh))

cv2.imshow("Scale: {} x {}".format(s1, s2), yeni_imaj)
cv2.waitKey()
cv2.destroyAllWindows()
