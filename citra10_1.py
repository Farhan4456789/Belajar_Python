import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk deteksi tepi menggunakan metode Roberts
def roberts_edge_detection(image):

# Konversi gambar ke skala abu-abu
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Kernel Roberts
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])

# Konvolusi gambar dengan kernel Roberts
    gradient_x = cv2.filter2D(gray_image, -1, kernel_x)
    gradient_y = cv2.filter2D(gray_image, -1, kernel_y)

# Menghitung magnitudo gradien
    magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    magnitude *= 255.0 / magnitude.max() # Normalisasi magnitudo

    return magnitude.astype(np.uint8)

# Fungsi untuk menampilkan gambar
def show_image(image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


# Baca gambar
image = cv2.imread('ufo.jpg') # Ganti dengan nama file gambar Anda

# Deteksi tepi menggunakan metode Roberts
edges_roberts = roberts_edge_detection(image)

# Tampilkan gambar asli dan hasil deteksi tepi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor (image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)

plt.imshow(edges_roberts, cmap='gray')
plt.title('Hasil Deteksi tepi metode Roberts')
plt.axis('off')

plt.show()