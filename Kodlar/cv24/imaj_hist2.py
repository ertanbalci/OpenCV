import cv2
import numpy as np
from matplotlib import pyplot as plt

def imaj_göster(ax, im, başlık):
     ax.imshow(im)
     ax.set_title(başlık)
     ax.set_axis_off()

def rgb_hist(imaj, cla):
     r,g,b = cv2.split(imaj)
     eqR = cla.apply(r)
     eqG = cla.apply(g)
     eqB = cla.apply(b)
     eqRGB = cv2.merge([eqR, eqG, eqB])
     return eqRGB

def hsv_hist(imaj, cla):
     imaj = cv2.cvtColor(imaj, cv2.COLOR_RGB2HSV)
     H,S,V = cv2.split(imaj)
     eqV = cla.apply(V)
     eqHSV = cv2.merge([H, S, eqV])
     eqHSV = cv2.cvtColor(eqHSV, cv2.COLOR_HSV2RGB)
     return eqHSV

def yuv_hist(imaj, cla):
     imaj = cv2.cvtColor(imaj, cv2.COLOR_RGB2YUV)
     Y,U,V = cv2.split(imaj)
     eqY = cla.apply(Y)
     eqYUV = cv2.merge([eqY, U, V])
     eqYUV = cv2.cvtColor(eqYUV, cv2.COLOR_YUV2RGB)
     return eqYUV
fig = plt.figure(figsize=(12,7))
ax1 = fig.add_subplot(141)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(144)
imaj = cv2.imread("x://opencv//monaLisa.png")
imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2RGB) # matplotlib için
cla = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(3,3))
eqRGB = rgb_hist(imaj, cla)
eqHSV = hsv_hist(imaj, cla)
eqYUV = yuv_hist(imaj, cla)
imaj_göster(ax1, imaj,  "Orijinal imaj")
imaj_göster(ax2, eqRGB, "RGB CLAHE")
imaj_göster(ax3, eqHSV, "HSV: V CLAHE")
imaj_göster(ax4, eqYUV, "YUV: Y CLAHE")
plt.tight_layout()
plt.show()   





