import numpy as np
import cv2
from skimage.transform import radon
import pytest
from discrete_radon.discrete_radon import radon_transform

# Three lines with different colors
def create_color_lines_image(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.line(img, (50, 10), (150, 10), (255, 0, 0), 1)  # Blue линия
    cv2.line(img, (50, 30), (150, 30), (0, 255, 0), 1)  # Green линия
    cv2.line(img, (50, 50), (150, 50), (0, 0, 255), 1)  # Red линия
    return img

# To grayscale
def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Test for three lines
def test_radon_transform_color_lines():
    img_color = create_color_lines_image(200, 100)
    img_gray = to_grayscale(img_color)

    # Check for rgb
    result_radon_color = radon_transform(img_color)
    expected_radon_color = radon(img_color, theta=np.linspace(-np.pi, np.pi, 501))
    assert np.allclose(result_radon_color, expected_radon_color)

    # Check for grayscale
    result_radon_gray = radon_transform(img_gray)
    expected_radon_gray = radon(img_gray, theta=np.linspace(-np.pi, np.pi, 501))
    assert np.allclose(result_radon_gray, expected_radon_gray)