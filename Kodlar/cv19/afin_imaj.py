import cv2
import numpy as np

imaj = cv2.imread("x://opencv//aspirin.png")
h = imaj.shape[0]-1
w = imaj.shape[1]-1

cv2.imshow("orj", imaj)

sp = np.float32([[0,0],[w,0],   [0,h]]) # kaynak imajdaki 3 nokta
#dp = np.float32([[0,0],[w//2,0],[w//2,h]]) # hedef imajdaki 3 nokta
dp = np.float32([[50,20],[w//2,10],[w//2+20,h-50]]) # hedef imajdaki 3 nokta

affm = cv2.getAffineTransform(sp, dp)
print("Afin matrisi:\n", affm)

afin_imaj = cv2.warpAffine(imaj, affm, (w,h))
cv2.imshow("afin_imaj", afin_imaj)

cv2.waitKey()
cv2.destroyAllWindows()
