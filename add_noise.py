import numpy as np
import cv2
import os
from PIL import Image as im

i = 0
dir = "dir_to_add_noise"

# I didn't have much data so I had to add Gaussian noise to expand my dataset
for f in os.listdir(dir):
    img = cv2.imread(dir + f"/{f}")
    img = cv2.resize(img, (224, 224))
    mean = 0
    var = 10
    sigma = var**0.5
    gaussian = np.random.normal(
        mean, sigma, (224, 224)
    )  

    noisy_image = np.zeros(img.shape, np.float32)

    if len(img.shape) == 2:
        noisy_image = img + gaussian
    else:
        noisy_image[:, :, 0] = img[:, :, 0] + gaussian
        noisy_image[:, :, 1] = img[:, :, 1] + gaussian
        noisy_image[:, :, 2] = img[:, :, 2] + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    i += 1
    pic = im.fromarray(noisy_image)
    pic.save(f"noisy_pics/{i}.jpg")
