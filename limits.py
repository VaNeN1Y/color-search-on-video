import cv2
import numpy as np


def get_ranges(color, tol=10, s_min=50, v_min=50):
    """
    Возвращает HSV-диапазоны для поиска заданного цвета.

    color: BGR цвет (массив)
    tol: разброс по оттенку (± hue)
    s_min: минимальная насыщенность (0-255)
    v_min: минимальная яркость (0-255)

    return: массив (lower, upper) диапазонов
    """
    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsv[0][0][0]

    ranges = []

    if hue <= 10 or hue >= 170:  # Отдельно для красного, ведь его оттенки находятся в начале и в конце
        ranges.append((np.array([0, s_min, v_min]),
                       np.array([hue + tol, 255, 255])))
        ranges.append((np.array([hue - tol, s_min, v_min]),
                       np.array([179, 255, 255])))

    else:
        lower = np.array([max(hue - tol, 0), s_min, v_min],
                         dtype=np.uint8)  # OpenCV ждёт uint8, НЕ int64 (не менять)
        upper = np.array([min(hue + tol, 179), 255, 255],
                         dtype=np.uint8)
        ranges.append((lower, upper))

    return ranges
