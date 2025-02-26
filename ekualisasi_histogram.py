import cv2
import numpy as np
import matplotlib.pyplot as plt

#gambar asli
gambar_asli = cv2.imread("ufo.jpg")

#konversi ke format rgb
gambar_asli_rgb = cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB)

#memisahkan gambar ke saluran warna rgb
r, g, b = cv2.split(gambar_asli_rgb)

#melakukan ekualisasi untuk setiap saluran
r_equalized = cv2.equalizeHist(r)
g_equalized = cv2.equalizeHist(g)
b_equalized = cv2.equalizeHist(b)

#menggabungkan saluran yang sudah diekualisasi 
gambar_equalized_rgb = cv2.merge((r_equalized, g_equalized, b_equalized))

#plotting
plt.figure(figsize=(12, 8))

#menampilkan gambar asli
plt.subplot(2, 3, 1)
plt.imshow(gambar_asli_rgb)
plt.title('Gambar Asli')
plt.axis('off')

#menampilkan histogram untuk seluruh saluran warna
plt.subplot(2, 3, 4)
plt.hist(r.ravel(), bins=256, color='r', alpha=0.5, label='Merah')
plt.hist(g.ravel(), bins=256, color='g', alpha=0.5, label='Hijau')
plt.hist(b.ravel(), bins=256, color='b', alpha=0.5, label='Biru')
plt.title('Histogram gambar asli')
plt.xlabel('Intensitas piksel')
plt.ylabel('Frekuensi')
plt.legend()

#menampilkan gambar sebelum ekualisasi histogram
plt.subplot(2, 3, 2)
plt.imshow(gambar_asli_rgb)
plt.title('Sebelum ekualisasi histogram')
plt.axis('off')

#menampilkan histogram setiap warna
plt.subplot(2, 3, 5)
plt.hist(r.ravel(), bins=256, color='r', alpha=0.5, label='Merah')
plt.hist(g.ravel(), bins=256, color='g', alpha=0.5, label='Hijau')
plt.hist(b.ravel(), bins=256, color='b', alpha=0.5, label='Biru')
plt.title('Histogram sebelum ekualisasi histogram')
plt.xlabel('Intensitas piksel')
plt.ylabel('Frekuensi')
plt.legend()

#menampilkan gambar setelah equalisasi
plt.subplot(2, 3, 3)
plt.imshow(gambar_equalized_rgb)
plt.title('Setelah equalisasi histogram')
plt.axis('off')

#menampilkan histogram untuk setiap warna setelah equalisasi
plt.subplot(2, 3, 6)
plt.hist(r_equalized.ravel(), bins=256, color='r', alpha=0.5, label='Merah')
plt.hist(g_equalized.ravel(), bins=256, color='g', alpha=0.5, label='Hijau')
plt.hist(b_equalized.ravel(), bins=256, color='b', alpha=0.5, label='Biru')
plt.title('Histogram setelah ekualisasi histogram')
plt.xlabel('Intensitas piksel')
plt.ylabel('Frekuensi')
plt.legend()

plt.tight_layout()
plt.show()