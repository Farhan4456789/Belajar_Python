import cv2

def detect_motion(image1, image2):
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image1, contours, -1, (0, 255, 0), 2)

    resized_image = cv2.resize(image1, (800, 600))

    cv2.imshow("Motion Detection", resized_image)
    cv2.waitKey(0)  # Tunggu hingga tombol keyboard ditekan
    cv2.destroyAllWindows()

image1 = cv2.imread("det1.jpg")
image2 = cv2.imread("det2.jpg")

if image1 is not None and image2 is not None:
    detect_motion(image1, image2)
else:
    print("Gagal membaca citra.")