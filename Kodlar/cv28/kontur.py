import cv2
import numpy as np

imaj = cv2.imread("x://opencv//coins.png")
gray = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (15,15),0) # sigmaX=0
ret, threshed = cv2.threshold(blurred, 131, 255, 0) # 

kontur, _ = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Bulunan kontur sayısı:", len(kontur))

tempImaj = imaj.copy()
outlines = cv2.drawContours(tempImaj, kontur, -1, (0,0,255), 2)

frames = [imaj, gray, blurred, threshed, outlines]
fnames = ["imaj", "gray", "blurred", "threshed", "outlines"]

for i in range(len(frames)):
     cv2.imshow(fnames[i], frames[i])

for i in range(len(kontur)):
     tempImaj = imaj.copy()
     outlines = cv2.drawContours(tempImaj, [kontur[i]], 0, (0,0,255), 2)
     cv2.imshow("Outline: "+str(i), outlines)
     
cv2.waitKey()
cv2.destroyAllWindows()

