import cv2
import numpy as np

imaj = cv2.imread("x://opencv//edge4.png", 0) # gri tona dönüştürerek okuyoruz
imaj = cv2.resize(imaj, None, fx=.6, fy=.6)
cv2.imshow("orj", imaj)

# X ekseni yönünde kenar tespiti yapıyoruz:
sx5 = cv2.Sobel(imaj, cv2.CV_8U, 1, 0, ksize=5) # veritipine dikkat
#cv2.imshow("sx5 CV 8U", sx5)

# X ekseni yönünde kenar tespiti yapıyoruz: veri tipini değiştireceğiz
sx564 = cv2.Sobel(imaj, cv2.CV_64F, 1, 0, ksize=5) # veritipi 64 bit
sx564 = np.absolute(sx564)
sx564 = np.uint8(sx564)
#cv2.imshow("sx564 CV 64F", sx564)

# Y ekseni yönünde kenar tespiti yapıyoruz: 
sy564 = cv2.Sobel(imaj, cv2.CV_64F, 0, 1, ksize=5) # veritipi 64 bit
sy564 = np.absolute(sy564)
sy564 = np.uint8(sy564)
#cv2.imshow("sy564 CV 64F", sy564)

# X ve Y ekseni kenar tespitlerini birleştiriyoruz:
sxy = cv2.bitwise_or(sx564, sy564)  # addweighted .5 ağrlığı ile de kullanılabilir
cv2.imshow("Sobel sxy",sxy)

# Sobel de Scharr filtresi kullanarak kenar tespiti yapalım:
shx = cv2.Sobel(imaj, cv2.CV_64F, 1, 0, ksize=-1) # ksize=-1  --> scharr filtresi
shy = cv2.Sobel(imaj, cv2.CV_64F, 0, 1, ksize=-1) # ksize=-1  --> scharr filtresi
shxy = cv2.bitwise_or(shx, shy)
shxy = np.absolute(shxy)
shxy = np.uint8(shxy)
cv2.imshow("Sobel Scharr", shxy)

# Laplace
imaj2 = cv2.GaussianBlur(imaj, (3, 3), 0)
cv2.imshow("Bulanik imaj", imaj2)

lap = cv2.Laplacian(imaj2, cv2.CV_64F) # varsayılan kernel kullanıyoruz
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplace 1", lap)

lap2 = cv2.Laplacian(imaj2, cv2.CV_64F, ksize=3)
lap2 = np.uint8(np.absolute(lap2))
cv2.imshow("Laplace 2 ksize:3", lap2)


cv2.waitKey()
cv2.destroyAllWindows()
