import cv2

# membaca citra 
image_path = 'ufo.jpg' # Ganti dengan path citra Anda 
original_image = cv2.imread(image_path)

# Tentukan faktor kontras
contrast_factor = 2 # Ubah sesuai kebutuhan Anda

# Modifikasi kontras
modified_image = cv2.convertScaleAbs(original_image, alpha=contrast_factor, beta=0)

# Tampilkan citra asli dan citra yang dimodifikasi
cv2.imshow('Citra ASLI', original_image)
cv2.imshow('Hasil peningkatan kontras', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()