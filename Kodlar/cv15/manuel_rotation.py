import cv2
import numpy as np
import math
imaj = cv2.imread("x://opencv//vosvos.jpg")
yeni_imaj = np.zeros_like(imaj)                # İmaja eş zero matris oluşturuyoruz:
h, w = imaj.shape[:2]         # imaj merkez noktası koordinatlarını hesaplıyoruz.
cw = w // 2
ch = h // 2
# imajı 45 derece döndüreceğiz. # math modülü açı hesaplarında radyan kullanıyor.
teta = (22/7) * 45 /180         # 45 dereceyi radyana dönüştürüyoruz: 180 derece = pi
costeta = math.cos(teta)
sinteta = math.sin(teta)
rm = np.float32([[costeta, -sinteta], [sinteta, costeta]]) # Döndürme matrisi 
center = np.float32([ch,cw])                               # imaj merkezi için array
for i in range(h):
     for j in range(w):
          pValue = imaj[i,j]                  # i, j noktasındaki piksel değeri
          h1w1 = np.float32([i - ch, j - cw]) # [i, j] noktasının merkezden uzaklığı
          h2w2 = np.dot(rm, h1w1) + center    # h1w1'in yeni imajdaki koordinatı 
          h2w2 = np.int_(h2w2)                # Koordinat değerlerini tamsayıya dönüştürüyoruz.
          h2, w2 = h2w2[:2]    # [h2 w2] formatında. Buradan 
          if (w > w2 > 0) and (h > h2 > 0):
               yeni_imaj[h2, w2] = pValue
cv2.imshow("Orijinal",imaj)
cv2.imshow("45 derece",yeni_imaj)
cv2.waitKey(0)
cv2.destroyAllWindows()
