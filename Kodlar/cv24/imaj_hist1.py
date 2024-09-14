import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

def drawHist(hist, x, y, grafNo, grafRenk):
     ax = plt.subplot(2, 1, grafNo)
     plt.plot(x, y, color=grafRenk, linestyle="--", label="Parlaklık Ortalaması") # ortalama doğrusu
     plt.plot(hist, color=grafRenk, label="Frekans Eğrisi")                       # histogram
     plt.grid()                              # ızgara görünümü
     plt.legend()                            # grafik isimleri köşede göster
     plt.xlabel("Parlaklık Seviyesi")        # x ekseni etiketi
     plt.ylabel("Frekans")                   # y ekseni etiketi
     plt.xticks(np.arange(0, 256,15))        # x ekseni tikleri

try:
     imaj = cv2.imread(sys.argv[1])
     parlat = int(sys.argv[2])
except:
     imaj = cv2.imread("x://opencv//monaLisa.png")
     parlat = 15

gimaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
pimaj = cv2.add(gimaj, parlat)

cv2.imshow("Gray Image Brightness {}".format(int(gimaj.mean())), gimaj)
cv2.imshow("Bright Gray Im.Brightness {}".format(int(pimaj.mean())), pimaj)

kanal = [0]
maske = None
grupSayısı = [256]
aralık = [0, 256]

hist_gimaj = cv2.calcHist([gimaj], kanal, maske, grupSayısı, aralık)
hist_pimaj = cv2.calcHist([pimaj], kanal, maske, grupSayısı, aralık)

plt.figure(figsize=(12,7))
plt.xlim([0, 256])

# gimaj renk tonları ortalaması doğrusu
x1 = [gimaj.mean(), gimaj.mean()]     # x ekseni değerleri
y1 = [0,            hist_gimaj.max()] # y ekseni değerleri

# pimaj renk tonları ortalaması doğrusu
x2 = [pimaj.mean(), pimaj.mean()]     # x ekseni değerleri
y2 = [0,            hist_pimaj.max()] # y ekseni değerleri

grafNo   = 1
grafRenk = "b"
drawHist(hist_gimaj, x1, y1, grafNo, grafRenk)

grafNo   = 2
grafRenk = "r"
drawHist(hist_pimaj, x2, y2, grafNo, grafRenk)

plt.show()
cv2.waitKey()  
