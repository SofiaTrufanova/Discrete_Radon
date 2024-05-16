import click.testing
import numpy as np
import pytest
from skimage.draw import line
from skimage.transform import radon
from src.radon_sofia.discrete_radon import radon_transform


# Blank image
def create_blank_image(width, height):
    return np.zeros((height, width), dtype=np.uint8)


# Random positive line
def create_positive_slope_line_image(width, height):
    img = create_blank_image(width, height)
    rr, cc = line(10, 10, 90, 50)
    img[rr, cc] = 255
    return img


# Random negative line
def create_negative_slope_line_image(width, height):
    img = create_blank_image(width, height)
    rr, cc = line(90, 10, 10, 50)
    img[rr, cc] = 255
    return img


# Vert line
def create_vertical_line_image(width, height):
    img = create_blank_image(width, height)
    rr, cc = line(10, 10, 10, 90)
    img[rr, cc] = 255
    return img


# Hor line
def create_horizontal_line_image(width, height):
    img = create_blank_image(width, height)
    rr, cc = line(10, 50, 90, 50)
    img[rr, cc] = 255
    return img


# 2 intercept
def create_intersecting_lines_image(width, height):
    img = create_blank_image(width, height)
    rr1, cc1 = line(10, 10, 90, 50)
    rr2, cc2 = line(90, 10, 10, 50)
    img[rr1, cc1] = 255
    img[rr2, cc2] = 255
    return img


# 3 lines from 1 point
def create_three_lines_from_one_point_image(width, height):
    img = create_blank_image(width, height)
    rr1, cc1 = line(10, 10, 90, 50)
    rr2, cc2 = line(10, 10, 10, 90)
    rr3, cc3 = line(10, 10, 50, 90)
    img[rr1, cc1] = 255
    img[rr2, cc2] = 255
    img[rr3, cc3] = 255
    return img


# 2 parallel lines
def create_parallel_lines_image(width, height):
    img = create_blank_image(width, height)
    rr1, cc1 = line(10, 10, 90, 10)
    rr2, cc2 = line(10, 50, 90, 50)
    img[rr1, cc1] = 255
    img[rr2, cc2] = 255
    return img


# Test for random lines
@pytest.mark.parametrize(
    "create_line_image",
    [
        create_positive_slope_line_image,
        create_negative_slope_line_image,
        create_vertical_line_image,
        create_horizontal_line_image,
        create_intersecting_lines_image,
        create_three_lines_from_one_point_image,
        create_parallel_lines_image,
    ],
)
def test_radon_transform_line(create_line_image):
    img = create_line_image(100, 100)
    result_radon = radon_transform(img, 100, 501)
    expected_radon = radon(img, theta=np.linspace(-np.pi, np.pi, 501))
    assert np.allclose(result_radon, expected_radon)
