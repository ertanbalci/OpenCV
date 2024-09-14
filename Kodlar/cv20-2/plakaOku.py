import cv2
import numpy as np

def mouse_click(event, x, y, flags, param):
     global pts
     if event == cv2.EVENT_RBUTTONDOWN:
          # seçilen noktaları listeye ekleyeceğiz
          pts.append([x, y])
          print("{}: ({}, {}) seçildi.".format(len(pts), x, y))
          
     if event == cv2.EVENT_MBUTTONDOWN:
          # nokta sayısı en az dört ise son 4 noktayı alacağız
          # hangi noktanın hangi köşeyi temsil ettiğini belirleyeceğiz
          # plaka düzleştirme fonksiyonunu çağıracağız
          if len(pts) > 3:
               dps = pts[-4:] # pts listesinin son dört elemanını alıyoruz
               pts = []       # pts listesini boşaltıyoruz.
               dps.sort()     # dps listesini sütun no.larına göre sıralıyoruz. Sol ve sağ köşeleri ayırmak için
               if dps[0][1] < dps[1][1]:     # plakanın solundaki noktalardan hangisi üstte hangisi altta?
                    c1 = dps[0]
                    c2 = dps[1]
               else:
                    c2 = dps[0]
                    c1 = dps[1]

               if dps[2][1] < dps[3][1]:    # plakanın sağındaki noktalardan hangisi üstte hangisi altta?
                    c3 = dps[2]
                    c4 = dps[3]
               else:
                    c4 = dps[2]
                    c3 = dps[3]
               plakaDüzleştir(c1, c2, c3, c4)
          else:
               print("HATA: En az dört nokta seçmelisiniz!")

def plakaDüzleştir(c1, c2, c3, c4):
     # plaka düzleştirme yapılacak
     yuk = c2[1] - c1[1]
     gen = c3[0] - c1[0]
     d1 = [0, 0]        # yeni imajdaki sol üst nokta
     d2 = [0, yuk]      # yeni imajdaki sol alt nokta
     d3 = [gen, 0]      # yeni imajdaki sağ üst nokta
     d4 = [gen, yuk]    # yeni imajdaki sağ alt nokta

     p1 = np.float32([c1, c2, c3, c4])
     p2 = np.float32([d1, d2, d3, d4])
     pM = cv2.getPerspectiveTransform(p1, p2)
     plaka = cv2.warpPerspective(imaj, pM, (gen, yuk))
     # plaka gösterilecek
     cv2.imshow("Plaka", plaka)

# nokta seçimi için boş liste oluştur
pts = []  # global olacak

# imajı oku
imaj = cv2.imread("x://opencv//plaka.png")

# fare kontrolünü set et
cv2.namedWindow("Arac")
cv2.imshow("Arac", imaj)
cv2.setMouseCallback("Arac", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()


