import cv2
import numpy as np

# 1. imaj ve logoyu okuyoruz:
imaj = cv2.imread("monaLisa.png")
logo = cv2.imread("snake.png")

# 2. Logoyu imajın sol üst köşesine yerleştireceğiz.
#    İlgi alanımız imajın sol üst köşesi. Boyutu logo boyutu
#    İmajın sol üst köşesinden logo boyutunda parça alacağız.
#    Bu parça logonun background'u olacak:
rh, rw = logo.shape[:2]
roi = imaj[0:rh, 0:rw]

# 3. Logoyu griye çevirip maske ve ters_maskeyi oluşturuyoruz:
gri_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

ret, maske = cv2.threshold(gri_logo, 250, 255, cv2.THRESH_BINARY_INV) 
ters_maske = cv2.bitwise_not(maske)

# 4. Logo background'u roi'den al (roi:imajın logo gelecek alanı)
bg_logo = cv2.bitwise_and(roi, roi, mask=ters_maske)

# 5. Logo foregorund'u logodan al
fg_logo = cv2.bitwise_and(logo, logo, mask=maske)

# 6. Logo foreground'u logo background'a oturt
myLogo = cv2.add(bg_logo, fg_logo)

# 7. Logoyu imaja yerleştir
imaj[0:rh, 0:rw] = myLogo

cv2.imshow("imaj", imaj)

cv2.waitKey(0)
