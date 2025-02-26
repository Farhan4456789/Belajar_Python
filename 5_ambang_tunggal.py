import cv2

image = cv2.imread('ufo.jpg')
image2 = cv2.resize(image, (300, 200))
image3 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(image3, 120, 255, 0)

cv2.imshow('citra ASLI (Resize)', image2)
cv2.imshow('citra RBG to Gray', image3)
cv2.imshow("Citra Biner", thresh)

if cv2.waitKey() == 0:
  cv2.destroyAllWindows()