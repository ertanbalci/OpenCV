import cv2
import numpy as np

imaj = cv2.imread("x://opencv//lenna.png")
imaj = cv2.resize(imaj, None, fx=.6, fy=.6)
cv2.imshow("imaj", imaj)

blurKernel = np.ones((3, 3)) / 9
blurred1 = cv2.filter2D(imaj, -1, blurKernel)
cv2.imshow("blurred1", blurred1)

blurKernel = np.ones((7, 7)) / 49
blurred2 = cv2.filter2D(imaj, -1, blurKernel)
cv2.imshow("blurred2", blurred2)

for ks in [3,5,7]:
     kernel = np.ones((ks, ks)) * (-1)
     center = int((ks-1)/2)
     kernel[center, center] = ks * ks
     print(kernel,"\n")
     winname= "Kernel Size {}x{}".format(ks, ks)
     imaj2 = cv2.filter2D(blurred1, -1, kernel)
     cv2.imshow(winname, imaj2) 
     



     
cv2.waitKey()
cv2.destroyAllWindows()


