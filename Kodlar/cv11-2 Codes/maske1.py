import cv2
import numpy as np
import argparse

ap =argparse.ArgumentParser()

ap.add_argument("-i", "--imaj", required=True, help="İmaj dosyası yolu ve adı?")
ap.add_argument("-m", "--masketipi", help="Dairesel maske için d, kare maske için k girin")
ap.add_argument("-b", "--maskeboyu", help="Maskenin merkezden uzaklığı (yarıçap veya kenar / 2 )")
ap.add_argument("-c", "--center", help="Maske Merkezi:50x50 formatında girin")

args = vars(ap.parse_args())

#Orijinal imajı göster:
imaj = cv2.imread(args["imaj"])
y, g = imaj.shape[:2]
cv2.imshow("Orj imaj", imaj)

mtipi = args["masketipi"]
mboyu = args["maskeboyu"]
mcntr = args["center"]

maske = np.zeros(imaj.shape[:2], dtype="uint8") # İmajla aynı boyutta maske zemini oluşturduk

if not mboyu:
     mboyu = g//4
else:
     mboyu = int(mboyu)

if mcntr:
     cX, cY = mcntr.split("x") # Okunan değerler string
     cX = int(cX)
     cY = int(cY)
else:
     (cX, cY) = (g//2, y//2) # CLI'den maske merkezi girilmemişse imaj merkezini maske merkezi yapıyoruz

if mtipi == "k":
     cv2.rectangle(maske, (cX-mboyu, cY-mboyu), (cX+mboyu, cY+mboyu), 255, -1)
else:
     cv2.circle(maske, (cX,cY), mboyu, 255, -1)

cv2.imshow("maske", maske)

yeni_imaj = cv2.bitwise_and(imaj, imaj, mask=maske)
cv2.imshow("MASKELI IMAJ", yeni_imaj)

cv2.waitKey()
cv2.destroyAllWindows()
