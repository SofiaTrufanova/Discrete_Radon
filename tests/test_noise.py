import numpy as np
import pytest
import cv2
from skimage.transform import radon
from discrete_radon.discrete_radon import radon_transform

# Pic with line
def create_line_image(width, height, thickness):
    img = np.zeros((height, width), dtype=np.uint8)
    cv2.line(img, (10, 10), (90, 90), 255, thickness)
    return img

# Funk to apply noise on pic
def add_noise_to_image(image, noise_level):
    noise = np.random.normal(scale=noise_level, size=image.shape)
    noisy_image = image.astype(np.float32) + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

# Tests for noise
@pytest.mark.parametrize("noise_level", [0, 20, 50, 100])
def test_radon_transform_with_noise(noise_level):
    img_line = create_line_image(100, 100, 2)  
    img_noisy = add_noise_to_image(img_line, noise_level)  

    result_radon_noisy = radon_transform(img_noisy, 100, 501)  
    expected_radon = radon(img_line, theta=np.linspace(-np.pi, np.pi, 501)) 

    assert np.allclose(result_radon_noisy, expected_radon, atol=50) 