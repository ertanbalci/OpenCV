import cv2
import numpy as np
import sys

def add_alfa(x):
     cv2.setTrackbarPos("beta", "imajlar", 10-x)
     alfa = x/10
     beta = 1-alfa
     imaj = cv2.addWeighted(imaj1, alfa, imaj2, beta, 0)
     cv2.imshow("imajlar", imaj)

def add_beta(x):
     cv2.setTrackbarPos("alfa", "imajlar", 10-x)
     beta = x/10
     alfa = 1-beta
     imaj = cv2.addWeighted(imaj1, alfa, imaj2, beta, 0)
     cv2.imshow("imajlar", imaj)
     

imaj1 = "x://opencv//soteria.jpg" #sys.argv[1]
imaj2 = "x://opencv//lenna.jpg"   #sys.argv[2]

imaj1 = cv2.imread(imaj1)
imaj2 = cv2.imread(imaj2)

h1, w1 = imaj1.shape[:2]
h2, w2 = imaj2.shape[:2]
h = int((h1+h2)/2)
w = int((w1+w2)/2)

imaj1 = cv2.resize(imaj1,(w, h))
imaj2 = cv2.resize(imaj2,(w, h))

cv2.namedWindow("imajlar")

cv2.createTrackbar("alfa", "imajlar", 0, 10, add_alfa)
cv2.createTrackbar("beta", "imajlar", 0, 10, add_beta)

add_alfa(5) # başlangıç değeri

cv2.waitKey(0)

cv2.destroyAllWindows()
