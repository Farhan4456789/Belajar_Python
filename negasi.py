import cv2

#membaca gambar yang akan dimodif
image = cv2.imread('ufo.jpg')

# operasi negasi warna citra negatif
img_neg = cv2.bitwise_not(image)

#menampilkan citra asli
cv2.imshow('Citra asli', image)

#menampilkan citra hasil negasi 
cv2.imshow('Hasil Citra Negatif',img_neg)

if cv2.waitKey() == 0:
  cv2.destroyAllWindows()