import cv2
from matplotlib import pyplot as plt

im = "x://imajlar//vosvos.jpg"

imaj = cv2.imread(im)

cv2.imshow("cv2", imaj) 

imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2RGB)
plt.axis("off")
plt.imshow(imaj)
plt.show()
