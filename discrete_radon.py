import cv2
import numpy as np


def radon_transform(img):
    """
        Источник - 8 страница книжки из README
        ---
        Координаты исходного изображения - [x, y].
        Координаты преобразованного изображения - [p, tau], где y = px + tau
        Введём обозначения:
        x_m = x_min + m * delta_x
        y_n = y_min + n * delta_y
        p_k = p_min + k * delta_p
        tau_h = tau_min + h * delta_tau
        ---
        Тут используется - Nearest neighbour interpolation, которая выражает n:
        n = round((p_k * x_m + tau_h - y_min) / delta_y)
    """

    p_min = -50  # пробегаюсь по прямым с коэффициентами от -50 до 50, чтобы было с запасом :)
    delta_p = 0.02
    K = 5001

    def p(k):
        return p_min + k * delta_p

    tau_min = 0
    delta_tau = 1
    H = 512  # тоже с запасом беру прямые

    def tau(h):
        return tau_min + h * delta_tau

    x_min = y_min = 0
    M = img.shape[1]
    N = img.shape[0]
    delta_x = delta_y = 1

    img_radon[k, h] = []

    for k in range(K):
        for h in range(H):
            alpha = p(k) * delta_x / delta_y
            beta = (p(k) * x_min + tau(h0) - y_min) / Delta_y
            summa = 0
            for m in range(M):
                n = round(alpha * m + beta)
                if (n >= 0) & (n <= N):
                    summa += img[m, n]
            img_radon[k, h] = Delta_x * summa
    return img_radon

# считаем картинки

img1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('4.jpg', cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread('5.jpg', cv2.IMREAD_GRAYSCALE)

# загрузим новые - результат преобразования Радона

img1_radon = cv2.imwrite('radon_1.jpg', radon_transform(img1))
img2_radon = cv2.imwrite('radon_2.jpg', radon_transform(img2))
img3_radon = cv2.imwrite('radon_3.jpg', radon_transform(img3))
img4_radon = cv2.imwrite('radon_4.jpg', radon_transform(img4))
img5_radon = cv2.imwrite('radon_5.jpg', radon_transform(img5))
