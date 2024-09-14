import cv2
import numpy as np
from time import perf_counter as kronometre

imaj = "x://opencv//vosvos.jpg"
imaj = cv2.imread(imaj)
cv2.imshow("orj", imaj)
cv2.waitKey()

h, w = imaj.shape[:2]
yeni_imaj = np.zeros((h, w, 3), np.uint8)
x = int(input("İmaj yatay olarak (sağa/sola) kaç piksel kaydırılacak?   : "))
y = int(input("İmaj dikey olarak (yukarı/aşağı) kaç piksel kaydırılacak?: "))
# for döngüsü ile öteleme
start = kronometre()
for i in range(h):  # tüm satırları for döngüsüne sokuyoruz
     for j in range(w): # tüm sütunları for döngüsüne sokuyoruz
          if y+i < h and x+j < w:
               yeni_imaj[y+i, x+j] = imaj[i, j]
stop = kronometre()
sure = str(stop-start)
               
cv2.imshow("for loop translation: "+sure, yeni_imaj)
cv2.waitKey()

# warpAffine ile öteleme
start = kronometre()
tm = np.float32([[1,0,x],[0,1,y]])
#warp_imaj = cv2.warpAffine(imaj, tm, (w,h))
warp_imaj = cv2.warpAffine(imaj, tm, (w+x,h+y))
stop = kronometre()

sure = str(stop-start)

cv2.imshow("warpAffine translation: "+sure, warp_imaj)
cv2.waitKey()
cv2.destroyAllWindows()
