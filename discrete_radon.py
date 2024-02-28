import cv2


def radon_transform(img):
    pass


img1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('4.jpg', cv2.IMREAD_GRAYSCALE)

img1_radon = cv2.imwrite('radon_1.jpg', radon_transform(img1))
img2_radon = cv2.imwrite('radon_2.jpg', radon_transform(img2))
img3_radon = cv2.imwrite('radon_3.jpg', radon_transform(img3))
img4_radon = cv2.imwrite('radon_4.jpg', radon_transform(img4))
