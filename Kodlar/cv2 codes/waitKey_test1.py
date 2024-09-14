import cv2

lena1 = cv2.imread("x://opencv//lenna.png")
lena2 = cv2.imread("x://opencv//lenna.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("BGR Imaj", lena1)
cv2.imshow("Gri Imaj", lena2)

# Örnek 1: 0 ms  -  cv2.destroyAllWindows() kullanMIYORUZ. 
# bir tuşa bastığımızda
#pencereler açık halde iken program sonlanır:
#cv2.waitKey(0)

# Örnek 2: 2000 ms - cv2.destroyAllWindows() kullanMIYORUZ. 
# 2000 ms sonra veya bir tuşa bastığımızda
# pencereler açık halde iken program sonlanır:
#cv2.waitKey(2000)

# Örnek 3: 0 ms + cv2.destroyAllWindows() kullanıyoruz. 
# bir tuşa bastığımızda tüm pencereler kapanır:
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Örnek 4: 2000 ms + cv2.destroyAllWindows() kullanıyoruz. 
# 2000 ms sonra veya bir tuşa bastığımızda tüm pencereler kapanır:
cv2.waitKey(2000)
cv2.destroyAllWindows()
