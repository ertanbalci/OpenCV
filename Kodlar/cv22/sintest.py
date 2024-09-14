import cv2
import numpy as np
import argparse
import math

ps = argparse.ArgumentParser()
ps.add_argument("-i", "--imaj", required=True, help="imaj dosyası")
ps.add_argument("-a", "--amplitude", required=True, help="Sinüs genlik/amplitude değeri")
ps.add_argument("-b", "--periyot", required=True, help="2pi/periyot değeri")
ps.add_argument("-w", "--dalgayonu", required=True,help="Dalga yönü, x, y veya xy girin")

args = vars(ps.parse_args())

file = args["imaj"]
a = int(args["amplitude"])
b = float(args["periyot"])

if "x" in args["dalgayonu"] or "y" in args["dalgayonu"]:
     w = args["dalgayonu"]
else:
     w = "xy"

imaj = cv2.imread(file)
cv2.imshow("imaj", imaj)

ht, wt = imaj.shape[:2]

imaj2 = np.zeros(imaj.shape, dtype=imaj.dtype)
imaj3 = np.zeros(imaj.shape, dtype=imaj.dtype)

for i in range(ht):
     for j in range(wt):
          if "y" in w:
               i2 = int(a * math.sin(b * math.radians(i)))
          else:
               i2 = 0
          if "x" in w:
               j2 = int(a * math.sin(b * math.radians(j)))
          else:
               j2 = 0

          if i+i2 < ht and j+j2 < wt:
               imaj2[i,j] = imaj[i+i2, j+j2]
          else:
               imaj2[i,j] = imaj[ht-1, wt-1]

          if i+j2 < ht and j+i2 < wt:
               imaj3[i,j] = imaj[i+j2, j+i2]
          else:
               imaj3[i,j] = imaj[ht-1, wt-1]
               
cv2.imshow("sin wave 1", imaj2)
cv2.imshow("sin wave 2", imaj3)

cv2.waitKey()
cv2.destroyAllWindows()

          
               

