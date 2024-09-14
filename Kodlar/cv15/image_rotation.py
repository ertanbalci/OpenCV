import cv2
import numpy as np
import argparse

ps =argparse.ArgumentParser()
ps.add_argument("-i", "--imaj", required=True, help="İmaj path ve name")
ps.add_argument("-t", "--teta", type=int, help="Döndürme açısı")
ps.add_argument("-x", "--rotatex", type=int, help="Döndürme noktası satırı")
ps.add_argument("-y", "--rotatey", type=int, help="Döndürme noktası sütunu")
ps.add_argument("-s", "--scale", type=int, help="Yeniden boyutlandırma anahtarı")
params = vars(ps.parse_args())

imaj = cv2.imread(params["imaj"])
cv2.imshow("imaj", imaj)

h, w = imaj.shape[:2]

teta = params["teta"]
rx   = params["rotatex"]
ry   = params["rotatey"]
scale= params["scale"]

if not teta: teta = 45
if not rx: rx = w // 2
if not ry: ry = h // 2
if not scale: scale= 1.0

rotation_point = (rx, ry)

rm = cv2.getRotationMatrix2D(rotation_point, teta, scale)

print("Rotation Matrix:\n", rm)

yeni_imaj = cv2.warpAffine(imaj, rm, (w,h))
info ="Image rotated {} degrees at points ({},{})".format(teta, rx, ry)
cv2.imshow(info, yeni_imaj)

cv2.waitKey()
cv2.destroyAllWindows()
