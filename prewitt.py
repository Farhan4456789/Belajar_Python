import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk deteksi tepi menggunakan metode Prewitt
def prewitt_edge_detection(image):
    # Kernel Prewitt
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])

    kernel_y = np.array([[-1, -1, -1],
                        [0, 0, 0],
                        [1, 1, 1]])

# Konvolusi gambar dengan kernel Prewitt pada setiap saluran warna
    gradient_x_r = cv2.filter2D(image[:,:,0], -1, kernel_x)
    gradient_y_r = cv2.filter2D(image[:,:,0], -1, kernel_y)

    gradient_x_g = cv2.filter2D(image[:,:,1], -1, kernel_x)
    gradient_y_g = cv2.filter2D(image[:,:,1], -1, kernel_y)

    gradient_x_b = cv2.filter2D(image[:,:,2], -1, kernel_x)
    gradient_y_b = cv2.filter2D(image[:,:,2], -1, kernel_y)

# Menghitung magnitudo gradien pada setiap saluran warna

    magnitude_r = np.sqrt(np.square(gradient_x_r) + np.square(gradient_y_r))
    magnitude_g = np.sqrt(np.square(gradient_x_g) + np.square(gradient_y_g))
    magnitude_b = np.sqrt(np.square(gradient_x_b) + np.square(gradient_y_b))

    magnitude = np.maximum.reduce([magnitude_r, magnitude_g, magnitude_b])
    magnitude *= 255.0 / magnitude.max() # Normalisasi magnitudo

    return magnitude.astype(np.uint8)

# Fungsi untuk menampilkan gambar
def show_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Baca gambar
image = cv2.imread('ufo.jpg') # Ganti dengan nama file gambar Anda

# Deteksi tepi menggunakan metode Prewitt
edges_prewitt = prewitt_edge_detection(image)

# Tampilkan gambar asli dan hasil deteksi tepi
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title( 'Original Image' )

plt.axis('off')

plt.subplot(1, 2, 2)

plt.imshow(edges_prewitt, cmap='gray')
plt.title('Edges Detected using Prewitt Method')
plt.axis('off')

plt.show()