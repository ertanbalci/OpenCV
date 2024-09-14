import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def imajı_göster(ax1, imaj):     
     ax1.imshow(imaj)
     ax1.set_axis_off()
     
def histogram_çiz(ax2, hist, renk, etiket):
     ax2.plot(hist, color=renk, label=etiket)
     ax2.set_xticks(np.arange(0,256,15))
     ax2.set_xlim(0,256)
     ax2.grid()
     ax2.legend()
     
try:
     file = sys.argv[1]
except:
     file = "monaLisa.png"

imaj = cv2.imread(file)
imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2RGB)# matplotlib için

fig = plt.figure(figsize=(12,7))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

imajı_göster(ax1, imaj)
Bhist = cv2.calcHist([imaj], [0], None, [256], [0,256])
Ghist = cv2.calcHist([imaj], [1], None, [256], [0,256])
Rhist = cv2.calcHist([imaj], [2], None, [256], [0,256])

histogram_çiz(ax2, Bhist, "b", "Mavi")
histogram_çiz(ax2, Ghist, "g", "Yeşil")
histogram_çiz(ax2, Rhist, "r", "Kırmızı")

plt.tight_layout()
plt.show()
