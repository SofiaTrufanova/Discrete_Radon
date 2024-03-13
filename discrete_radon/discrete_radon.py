import cv2
import numpy as np


def radon_transform(img, K = 501, H = 501):
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
    img = np.ones(img.shape) * 255 - img
    N = img.shape[1]  # y
    M = img.shape[0]  # x
    delta_x, delta_y = 2 / (M - 1), 2 / (N - 1)
    x_min, y_min = -1, -1
    p_min, tau_min = np.pi, 10
    p = np.linspace(-p_min, p_min, K)
    tau = np.linspace(-tau_min, tau_min, H)

    img_radon = np.zeros((K, H))

    for k in range(K):
        for h in range(H):
            alpha = p[k] * delta_x / delta_y
            beta = (p[k] * x_min + tau[h] - y_min) / delta_y
            m_min = 0
            m_max = M - 1
            if alpha > 0:
                m_min = int(max(0, np.ceil((- beta - 0.5) / alpha)))
                m_max = int(min(M - 1, np.floor((N - 0.5 - beta) / alpha)))
            if alpha < 0:
                m_min = int(max(0, np.ceil((N - 0.5 - beta) / alpha)))
                m_max = int(min(M - 1, np.floor((- beta - 0.5) / alpha)))
            summa = 0
            for m in range(m_min, m_max + 1):
                n = round(alpha * m + beta)
                if (n >= 0) & (n < N):
                    summa += img[m, n]
            img_radon[k, h] = delta_x * summa
    return img_radon
