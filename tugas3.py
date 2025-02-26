import cv2

def rgb_to_gray(image_path):
  image = cv2.imread(image_path)

  if image is None:
    print("Gagal membaca gambar.")
    return None

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return gray_image

def main():
    image_path = 'ufo.jpg'
    original_image = cv2.imread(image_path)

    if original_image is None:
      print("Gagal membaca gambar asli.")
      return

    gray_image = rgb_to_gray(image_path)

    if gray_image is None:
      return

    cv2.imshow('CITRA ASLI', original_image)
    cv2.imshow('CITRA HASIL KONVERSI TRUE COLOR TO GRAY', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
  main()