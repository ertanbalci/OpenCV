import cv2

imaj1 = cv2.imread("lenna.png")
imaj2 = cv2.imread("soteria.png")

cv2.imshow("1",imaj1)
cv2.imshow("2",imaj2)

# Kullanıcı ESC tuşuna basana kadar
# imaj dosyaları açık kalsın:

while True:
     k = cv2.waitKey() & 0xFF  
     
     if k == 27:
          cv2.destroyAllWindows()
          break
