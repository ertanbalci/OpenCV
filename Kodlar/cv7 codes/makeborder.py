import cv2

imaj  = cv2.imread('x://opencv//kardesler.png')
imaj  = cv2.resize(imaj, None, fx=.75, fy=.75)

#imaj2 = cv2.copyMakeBorder(imaj, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
#imaj2 = cv2.copyMakeBorder(imaj, 20, 20, 20, 20, cv2.BORDER_REFLECT)
#imaj2 = cv2.copyMakeBorder(imaj, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)

#imaj2 = cv2.copyMakeBorder(imaj, 20, 20, 20, 20, cv2.BORDER_WRAP)

sarı = [0, 255, 255 ]
imaj2 = cv2.copyMakeBorder(imaj, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=sarı)

print("Orijinal imaj shape  :", imaj.shape)
print("Kenarlıklı imaj shape:", imaj2.shape)

cv2.imshow("Orijinal imaj", imaj)
cv2.imshow("Kenarlikli imaj", imaj2) 




#reflect = cv2.copyMakeBorder(img1,3,3,3,3,cv2.BORDER_REFLECT)
#reflect101 = cv2.copyMakeBorder(img1,3,3,3,3,cv2.BORDER_REFLECT_101)
#wrap = cv2.copyMakeBorder(img1,3,3,3,3,cv2.BORDER_WRAP)
#constant= cv2.copyMakeBorder(img1,25,25,25,25,cv2.BORDER_CONSTANT,value=BEYAZ)
"""
print(img1.shape)
print("replicate", replicate.shape)
print("reflect", reflect.shape)
print("reflect101", reflect101.shape)
print("wrap", wrap.shape)
print("constant", constant.shape)
#test(img1, "imaj")
print()
#test(constant, "constant")

BEYAZ = [0, 255, 255]

def test(imaj, etiket):
     h, w = imaj.shape
     print(etiket)
     print()
     for i in range(h):
          for j in range(w):
               print("  ", imaj[i,j], end="")
          print()
imaj  = cv2.resize(imaj, None, fx=.75, fy=.75)

"""
