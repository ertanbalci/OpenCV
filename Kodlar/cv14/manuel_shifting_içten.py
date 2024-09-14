import cv2
import numpy as np
import argparse

ps = argparse.ArgumentParser()

ps.add_argument("-i", "--imaj", required=True, help="İmaj dosyası yolu ve adı")
ps.add_argument("-e", "--eksen", help="Ayna dikey eksene konacaksa -> d, yatay eksene konacaksa -> y girin")
ps.add_argument("-%", "--yüzde", type=int, help="Ayna konumu % 1 - 99 arasında olacak")

params=vars(ps.parse_args())

imaj = cv2.imread(params["imaj"])

if params["eksen"] == "y":
     ayna = "yatay"
else:
     ayna = "dikey"

if not params["yüzde"]:
     ayna_konum = 50
else:
     ayna_konum = params["yüzde"]
print("ayna_konum",type(ayna_konum))
h, w = imaj.shape[:2]

if ayna == "dikey":
     ayna_konum = int(w * ayna_konum / 100)  # aynanın yüzde konumunu pixele çevirdik
     orijinal_alan = imaj[::, :ayna_konum]
     yansıyan_alan = np.flip(orijinal_alan, 1)
     yeni_imaj = np.hstack((orijinal_alan, yansıyan_alan))
     
else:
     ayna_konum = int(h * ayna_konum / 100)  # aynanın yüzde konumunu pixele çevirdik
     orijinal_alan = imaj[:ayna_konum,::]
     yansıyan_alan = np.flip(orijinal_alan, 0)
     yeni_imaj = np.vstack((orijinal_alan, yansıyan_alan))

print("ayna=",ayna)
print("ayna_konum",ayna_konum)
print("ayna",orijinal_alan.shape)
print("yeni shape",yeni_imaj.shape)

cv2.imshow("", yeni_imaj)
cv2.waitKey(0)
