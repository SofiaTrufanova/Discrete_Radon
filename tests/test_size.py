import numpy as np
import cv2
from skimage.transform import radon
import pytest
from discrete_radon.discrete_radon import radon_transform

def create_blank_image(width, height):
    return np.zeros((height, width), dtype=np.uint8)

def images_equal(img1, img2, tolerance=0.85):
    return np.all(np.abs(img1 - img2) <= tolerance)

def test_radon_transform_100x100_blank():
    img_blank = create_blank_image(100, 100)
    result_radon = radon_transform(img_blank, 100, 501)
    expected_radon = radon(img_blank, theta=np.linspace(-np.pi, np.pi, 501))
    assert images_equal(result_radon, expected_radon)

def test_radon_transform_256x256_blank():
    img_blank = create_blank_image(256, 256)
    result_radon = radon_transform(img_blank, 256, 501)
    expected_radon = radon(img_blank, theta=np.linspace(-np.pi, np.pi, 501))
    assert images_equal(result_radon, expected_radon)

def test_radon_transform_1000x3_blank():
    img_blank = create_blank_image(1000, 3)
    result_radon = radon_transform(img_blank, 3, 501)
    expected_radon = radon(img_blank, theta=np.linspace(-np.pi, np.pi, 501))
    assert images_equal(result_radon, expected_radon)

def test_radon_transform_255x255_blank():
    img_blank = create_blank_image(255, 255)
    result_radon = radon_transform(img_blank, 255, 501)
    expected_radon = radon(img_blank, theta=np.linspace(-np.pi, np.pi, 501))
    assert images_equal(result_radon, expected_radon)

def test_radon_transform_100x50_blank():
    img_blank = create_blank_image(100, 50)
    result_radon = radon_transform(img_blank, 50, 501)
    expected_radon = radon(img_blank, theta=np.linspace(-np.pi, np.pi, 501))
    assert images_equal(result_radon, expected_radon)