import cv2
import numpy as np

imaj = cv2.imread("x://opencv//vosvos.jpg")
imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
cv2.imshow("orj", imaj)
ks = 9 # kernel size

blur = cv2.blur(imaj, (ks, ks))
cv2.imshow("Blur imaj: {}x{}".format(ks, ks), blur)

gblur = cv2.GaussianBlur(imaj, (ks, ks),0)
cv2.imshow("Gaussian Blur imaj: {}x{}".format(ks, ks), blur)

mblur = cv2.medianBlur(imaj, ks)
cv2.imshow("Median Blur imaj: {}x{}".format(ks, ks), blur)

sigmaColor=30
sigmaSpace=30
bfilter = cv2.bilateralFilter(imaj, ks, sigmaColor, sigmaSpace)
cv2.imshow("Bilateral Blur imaj: {}x{}".format(ks, ks), bfilter)
cv2.waitKey()
cv2.destroyAllWindows()
