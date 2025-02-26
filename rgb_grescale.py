import cv2

# Load citra warna
image_path = 'ufo.jpg'
original_image = cv2.imread(image_path)


# Terapkan operasi thresholding pada seluruh citra warna
_,thresholded_image = cv2.threshold(original_image, 127, 255, cv2.THRESH_BINARY) 

# Tampilkan citra asli dan hasil thresholding
cv2.imshow('Citra Asli', original_image)
cv2.imshow('hasil peengambangan citra RGB', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()