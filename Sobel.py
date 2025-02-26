import cv2
import numpy as np
import matplotlib.pyplot as plt 

#fungsi deteksi
def sobel_edge_detection(image, kernel):
    #konklusi
    sobel_x_r = cv2.filter2D(image[:,:,0], -1, kernel)
    sobel_x_r = cv2.filter2D(image[:,:,0], -1, np.flip(kernel.T, axis=0))

    sobel_x_g = cv2.filter2D(image[:,:,1], -1, kernel)
    sobel_x_g = cv2.filter2D(image[:,:,1], -1, np.flip(kernel.T, axis=0))

    sobel_x_b = cv2.filter2D(image[:,:,2], -1, kernel)
    sobel_x_b = cv2.filter2D(image[:,:,2], -1, np.flip(kernel.T, axis=0))

    #menghitung gradi
    magnitude_r = np.sqrt(np.square(sobel_x_r) + np.square(sobel_x_r))
    magnitude_g = np.sqrt(np.square(sobel_x_g) + np.square(sobel_x_g))
    magnitude_b = np.sqrt(np.square(sobel_x_b) + np.square(sobel_x_b))

    #menggabungkan
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
sobel_kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

#deteksi tepi
edges_sobel = sobel_edge_detection(image, sobel_kernel)
# Tampilkan gambar asli dan hasil deteksi tepi
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title( 'Original Image' )
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Edges Detected menggunakan sobel')
plt.axis('off')
plt.show()