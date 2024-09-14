import cv2
import numpy as np
import random

liste = ["sh1.png","sh2.png","sh3.png","sh4.png","sh5.png","sh6.png","sh7.png"]
random.shuffle(liste)

for i in liste:
     imaj =cv2.imread(i)
     gray = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
     canny = cv2.Canny(gray, 50, 200)
     cv2.imshow("Yuklenen imaj", imaj)

     (konturs, _) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

     orj_imaj = imaj.copy()

     zemin = np.zeros(imaj.shape, np.uint8)
     k = konturs[0]
     acc =  0.01 * cv2.arcLength(k, True)
     approx = cv2.approxPolyDP(k, acc, True)
   
     if len(approx) == 10: winname = "Star"
     elif len(approx) > 10 and len(approx) <15: winname = "Elips"
     elif len(approx) > 14: winname = "Daire"
     else: winname = str(len(approx))+"GEN"
     winname2 ="Bu imaj "+winname                                  
     cv2.drawContours(zemin, [approx], 0, (255, 255, 255), 2)
     cv2.imshow(winname, zemin)
     cv2.imshow(winname2, imaj)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
