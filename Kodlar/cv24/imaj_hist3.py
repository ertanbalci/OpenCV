import cv2
import numpy as np
from matplotlib import pyplot as plt

def imaj_göster(ax, imaj, başlık):
     ax.imshow(imaj, cmap="gray")
     ax.set_title(başlık)
     ax.set_axis_off()

def hist_çiz(ax, imaj, kanal, renk, etiket):
     hist = cv2.calcHist([imaj], [kanal], None, [256], [0,256])
     ax.plot(hist, color=renk, label=etiket)
     ax.legend()

imaj = cv2.imread("x://opencv//monaLisa.png")
gimaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)

gimaj_equ = cv2.equalizeHist(gimaj)

cla = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(12,12))
gri_cla = cla.apply(gimaj)

fig1 = plt.figure(figsize=(12,7))
fig2 = plt.figure(figsize=(10,5))
ax1=fig1.add_subplot(131)
ax3=fig1.add_subplot(132)
ax5=fig1.add_subplot(133)

ax2=fig2.add_subplot(311)
ax4=fig2.add_subplot(312)
ax6=fig2.add_subplot(313)

imaj_göster(ax1, gimaj, "Orijinal İmaj")
imaj_göster(ax3, gimaj_equ, "Hist.EQ uygulandı:")
imaj_göster(ax5, gri_cla, "Clahe uygulandı:")

hist_çiz(ax2, gimaj,     0, "b", "Histogram")
hist_çiz(ax4, gimaj_equ, 0, "g", "Hist.EQ")
hist_çiz(ax6, gri_cla,   0, "r", "CLAHE")

plt.tight_layout()
plt.show()   

