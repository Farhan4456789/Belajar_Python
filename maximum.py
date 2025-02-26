import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menambahkan noise periodic 
def periodic_noise(image, amplitude):
  x = np.arange(image.shape[1])
  y = np.arange(image.shape[0])
  X, Y = np.meshgrid(x, y)
  noise = amplitude * np.sin(X / 5) + amplitude * np.sin(Y / 5)
  noisy_image = image + noise[:, :, np.newaxis]
  noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
  return noisy_image

  # Fungsi untuk mereduksi noise dengan filter maksimum
  def reduce_noise_maximum(image, kernel_size):
    return cv2.dilate(image, np.ones((kernel_size, kernel_size), np.uint8))

  # Load citra asli 
  image = cv2.imread('ufo.jpg')

  # Menambahkan noise periodic ke citra asli 
  periodic_noisy = periodic_noise(image, amplitude=20)

  # Mereduksi noise dengan filter maksimum 
  kernel_size = 5 # Ukuran kernel filter maksimum
  reduce_image = reduce_noise_maximum(periodic_noisy, kernel_size)

  # Menampilkan citra asli, citra dengan noise periodic, dan hasil reduksi noise dengan filter maksimum
  plt.figure(figsize=(15, 5))

  # Citra asli 
  plt.subplot(1, 3, 1)
  plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.title('Citra Asli')
  plt.axis('off')

  # Citra dengan noise periodic 
  plt.subplot(1, 3, 2)
  plt.imshow(cv2.cvtColor(periodic_noisy, cv2.COLOR_BGR2RGB))
  plt.title('Citra dengan Periodic Noise')
  plt.axis('off')

  # Hasil reduksi noise dengan filter maksimum
  plt.subplot(1, 3, 3)
  plt.imshow(cv2.cvtColor(reduced_image, cv2.COLOR_BGR2RGB))
  plt.title('Citra Hasil Reduksi Noise (Maximum Filter)')
  plt.axis('off')

  plt.tight_layout()
  plt.show()


