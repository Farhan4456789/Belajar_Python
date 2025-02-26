import cv2

def adjust_brightness(image, brightness):
  brighter = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
  return brighter

def adjust_brightness(image, dark):
  darker = cv2.convertScaleAbs(image, alpha=1, beta=dark)
  return darker

image = cv2.imread("ufo.jpg")

if image is None:
  print("Error: Citra tidak dapat dimuat.")
else:
  brightness = 100
  dark = -50

  brighter = adjust_brightness(image, brightness)
  darker = adjust_brightness(image, dark)

  cv2.imshow("CITRA ASLI", image)
  cv2.imshow("HASIL LEBIH CERAH", brighter)
  cv2.imshow("HASIL LEBIH GELAP", darker)
  cv2.waitKey(0)
  cv2.destroyAllWindows()