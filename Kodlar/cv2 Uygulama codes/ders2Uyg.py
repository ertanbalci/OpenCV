import cv2
import numpy as np
import argparse

pars = argparse.ArgumentParser()

pars.add_argument("-i", "--input", required=True, help="Okunacak dosya yolu ve adı")
pars.add_argument("-o", "--output", help="Okunacak dosya yolu ve adı")

files = vars(pars.parse_args())

imaj = cv2.imread(files["input"], 0) # -i ile girilen imajı gri tonlu okuyoruz

if not isinstance(imaj, np.ndarray):
     print("\nDosya bulunamadı")
else:
     cv2.imshow("imaj", imaj)
     k =cv2.waitKey(0)

     if k == 27: # esc
          cv2.destroyAllWindows()
     elif k == ord("s"):
          cv2.imwrite(files["output"], imaj)
          print("Dosya kaydedildi.")
          cv2.destroyAllWindows()
