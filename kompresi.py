import cv2 
import os  
import matplotlib.pyplot as plt

# Baca citra
image = cv2.imread('ufo.jpg')

# Simpan citra asli 
cv2.imwrite('original.jpg', image)

# Dapatkan ukuran file citra asli dalam byte
original_size_bytes = os.path.getsize('original.jpg')
# Konversi ukuran dari byte ke kilobyte
original_size_kb = original_size_bytes / 1024

#simpan citra dalam form JPEG (kompresi dengan kehilangan)
cv2.imwrite('compressed_image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

# Dapatkan ukuran file citra setelah kompresi dalam byte
compressed_size_bytes = os.path.getsize('compressed_image.jpg')
#konversi ukuran dari byte ke kilobyte
compressed_size_kb = compressed_size_bytes / 1024

# Buat sebuah figure
plt.figure(figsize=(10,5))

# Tampilkan citra asli
plt.subplot(1, 2, 1)
plt.title('Citra Asli \nSize: {:.2f} KB'.format(original_size_kb))

# Tampilkan citra hasil kompresi
compressed_image = cv2.imread('compressed_image.jpg')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB))
plt.title('Hasil Kompresi Citra\nSize: {:.2f} KB'.format(compressed_size_kb))
plt.exis('off')

# Tampilkan figure
plt.tight_layout()
plt.show()