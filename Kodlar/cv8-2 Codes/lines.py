import cv2
import numpy as np

# Tek kanal pano üzerine beyaz çizgi çizelim
pano1 = np.zeros((500,800), dtype="uint8")
cv2.line(pano1, (10,10),(350,375), color=255, thickness=5, lineType=cv2.LINE_4)
cv2.line(pano1, (120,10),(500,375), color=255, thickness=5, lineType=cv2.LINE_8)
cv2.line(pano1, (200,10),(650,375), color=255, thickness=5, lineType=cv2.LINE_AA)

font = 0
fscale =.5
color= 255
thickness = 1
cv2.putText(pano1, "Line 4", (360,375), font, fscale, color, thickness)
cv2.putText(pano1, "Line 8", (510,375), font, fscale, color, thickness)
cv2.putText(pano1, "Line AA", (660,375), font, fscale, color, thickness)

#cv2.imshow("pano1", pano1)

# Üç kanal pano üzerine yeşil çizgi ve ok çizelim
pano2 = np.zeros((500,800,3), dtype="uint8")
cv2.line(pano2, (10,10),(350,375), color=[0,255,0], thickness=5)
cv2.arrowedLine(pano2, (120,10),(500,375), color=255, thickness=5)

cv2.imshow("pano2", pano2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
