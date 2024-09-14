import cv2
import numpy as np
import sys

try:
     file1 = sys.argv[1]
     file2 = sys.argv[2]
except IndexError:
     file1 = "x://opencv//soteria1.png"
     file2 = "x://opencv//soteria2.png"

imaj1 = cv2.imread(file1)
imaj2 = cv2.imread(file2)

imaj3 = cv2.subtract(imaj1, imaj2)

cv2.imshow("file 1", imaj1)

cv2.imshow("file 2", imaj2)
#cv2.imshow("fark", imaj3) #

# farklı pikselleri kırmızı yapalım

imaj33 = np.where(imaj3>0, (0,0,255), (0,0,0))
imaj33 = imaj33.astype(np.uint8)
cv2.imshow("farklar kirmizi", imaj33) #

# kırmızı fark alanlarını imaj1'e ekleyelim
imaj333 = cv2.add(imaj1, imaj33)
#cv2.imshow("farklar imaj1e eklendi", imaj333)

# imaj1in kırmızı tonunu düşürelim
b = imaj1[:,:,0]
g = imaj1[:,:,1]
r = imaj1[:,:,2]

r = cv2.subtract(r, int(r.mean()/2))

imaj1 = cv2.merge((b,g,r))
#cv2.imshow("new file 1", imaj1)

imaj333 = cv2.add(imaj1, imaj33)
cv2.imshow("7 FARK SON", imaj333)

cv2.waitKey()
cv2.destroyAllWindows()
