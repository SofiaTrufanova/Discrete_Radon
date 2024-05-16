"""Realization of radon transform"""

import numpy as np
from skimage.color import rgb2gray


def min_and_max_m(
    number_of_rows: int, number_of_columns: int, alpha: int, beta: int
) -> tuple:
    """
    Считает min_m, max_m
    ----

    Arg:
        number_of_rows : int
            Число строк в исходном изображении.
        number_of_columns : int
            Число столбцов в исходном изображении.
        alpha : int
            Коэффициент наклона предполагаемой прямой.
        beta: int
            Коэффициент сдвига предполагаемой кривой.

    Returns:
        (m_min, m_max) : tuple
            Минимальное и максимальное m.
    """
    m_min = 0
    m_max = number_of_rows - 1
    if alpha > 0:
        m_min = int(max(0, np.ceil((-beta - 0.5) / alpha)))
        m_max = int(
            min(number_of_rows - 1, np.floor((number_of_columns - 0.5 - beta) / alpha))
        )
    if alpha < 0:
        m_min = int(max(0, np.ceil((number_of_columns - 0.5 - beta) / alpha)))
        m_max = int(min(number_of_rows - 1, np.floor((-beta - 0.5) / alpha)))
    return (m_min, m_max)


def radon_transform(img: np.ndarray, K: int = 501, H: int = 501) -> np.ndarray:
    """
    Источник - 8 страница книжки из README
    ---

    Координаты исходного изображения - [x, y].
    Координаты преобразованного изображения - [p, tau], где y = px + tau
    Введём обозначения:
    x_m = x_min + m * delta_x
    y_n = y_min + n * delta_y
    p_k = p_min + k * delta_k
    tau_h = tau_min + h * delta_tau
    ---
    Тут используется - Nearest neighbour interpolation, которая выражает n:
    n = round((p_k * x_m + tau_h - y_min) / delta_y)

    Args:
        img : np.ndarray()
            Изображение
        K: int
            Один из размеров img_radon (img_radon.shape[0])
        H: int
            Один из размеров img_radon (img_radon.shape[1])

    Returns:
        img_radon : np.ndarray(shape=(K, H))
            Дискретное преобразование Радона для изображения img
    """
    if img.ndim == 3:
        img = rgb2gray(img)

    number_of_rows = img.shape[0]
    number_of_columns = img.shape[1]

    x_min = -1
    y_min = -1

    delta_y = -2 * y_min / (number_of_rows - 1)
    delta_x = -2 * x_min / (number_of_columns - 1)

    p_min = 1
    tau_min = number_of_rows

    p = np.linspace(-p_min, p_min, K)
    tau = np.linspace(-tau_min, tau_min, H)

    img_radon = np.zeros((K, H))

    for k in range(K):
        alpha = p[k] * delta_x / delta_y

        for h in range(H):
            beta = (p[k] * x_min + tau[h] - y_min) / delta_y

            m_min, m_max = min_and_max_m(number_of_rows, number_of_columns, alpha, beta)

            summa = 0

            for m in range(m_min, m_max + 1):
                n = round(alpha * m + beta)
                if (n >= 0) & (n < number_of_columns):
                    summa += img[m, n]

            img_radon[k, h] = summa * delta_x
    return img_radon
