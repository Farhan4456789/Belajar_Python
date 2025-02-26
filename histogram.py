import cv2
import matplotlib.pylot as plt

# Membaca gambar dalam mode warna asli (BGR)
image = cv2.imread('ufo.jpg')

# Mengubah BGR menjadi RGB (untuk matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Membuat histogram
hist_r = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])
hist_b = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Citra Asli')
plt.axis('off')

