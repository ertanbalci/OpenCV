import cv2

ılgaz     = cv2.imread("x:/imajlar/Ilgaz.png")
gri_ılgaz = cv2.cvtColor(ılgaz, cv2.COLOR_BGR2GRAY)
yuv_ılgaz = cv2.cvtColor(ılgaz, cv2.COLOR_BGR2YUV)
hsv_ılgaz = cv2.cvtColor(ılgaz, cv2.COLOR_BGR2HSV)

cv2.imshow("BGR Ilgaz", ılgaz)
cv2.imshow("GRi Ilgaz", gri_ılgaz)
cv2.imshow("YUV Ilgaz", yuv_ılgaz)
cv2.imshow("HSV Ilgaz", hsv_ılgaz)
cv2.waitKey()

# BGR renk kanalları:
cv2.imshow("BGR B kanali", ılgaz[:,:,0])
cv2.imshow("BGR G kanali", ılgaz[:,:,1])
cv2.imshow("BGR R kanali", ılgaz[:,:,2])
cv2.waitKey()

#HSV renk kanalları:
cv2.imshow("HSV H kanali", hsv_ılgaz[:,:,0])
cv2.imshow("HSV S kanali", hsv_ılgaz[:,:,1])
cv2.imshow("HSV V kanali", hsv_ılgaz[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()

#L*a*b renk kanalları:
cv2.imshow("LAB L kanali", lab_ılgaz[:,:,0])
cv2.imshow("LAB a kanali", lab_ılgaz[:,:,1])
cv2.imshow("LAB b kanali", lab_ılgaz[:,:,2])
cv2.waitKey()


