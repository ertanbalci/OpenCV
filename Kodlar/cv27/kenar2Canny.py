import cv2
import numpy as np

imaj = cv2.imread("x://opencv//lenna.png", 0)
canny = cv2.Canny(imaj, 100, 200) # küçük ve büyük eşikler

cv2.imshow("canny", canny)

cv2.waitKey()
cv2.destroyAllWindows()
