import cv2

lena1 = cv2.imread("x:/imajlar/lenna.png")
lena2 = cv2.imread("x:/imajlar/lenna.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("BGR Imaj", lena1)
cv2.imshow("GrayScale Imaj", lena2)   

cv2.waitKey(0)
cv2.destroyAllWindows()


