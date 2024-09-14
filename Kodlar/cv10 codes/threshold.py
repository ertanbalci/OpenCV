
import cv2
import numpy as np

imaj = cv2.imread("x://opencv//lenna.jpg", 0)
cv2.imshow("", imaj)

algoritmalar = [(cv2.THRESH_BINARY,"BINARY"),
                (cv2.THRESH_BINARY_INV,"BINARY_INV"),
                (cv2.THRESH_TRUNC,"TRUNC"),
                (cv2.THRESH_TOZERO,"TOZERO"),
                (cv2.THRESH_TOZERO_INV,"TOZERO_INV"),
                (cv2.THRESH_OTSU,"OTSU"),
                (cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,"BINARY_INV+OTSU"),
                (cv2.THRESH_TRIANGLE,"TRIANGLE"),
                (cv2.THRESH_TRIANGLE+cv2.THRESH_BINARY_INV ,"TRIANGLE+BINARY_INV")]

for i in range(len(algoritmalar)):
     ret, thrs = cv2.threshold(imaj, 100, 230, algoritmalar[i][0])
     wname = "t={} {}".format(int(ret), algoritmalar[i][1])
     cv2.imshow(wname, thrs)







# Adaptive eşikleme

t1 = cv2.adaptiveThreshold(imaj, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
t2 = cv2.adaptiveThreshold(imaj, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
t3 = cv2.adaptiveThreshold(imaj, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 5)
t4 = cv2.adaptiveThreshold(imaj, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 5)

cv2.imshow("Mean 5 3", t1)
cv2.imshow("Gaus 5 3", t2)
cv2.imshow("Gaus 7 5", t3)
cv2.imshow("Gaus 15 5", t4)

cv2.waitKey(0)
cv2.destroyAllWindows()
