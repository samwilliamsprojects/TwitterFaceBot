from PIL import Image
import os, sys
import cv2
from PIL import Image as im

# Tensorflow model needs size of 224 x 224; this resizes pics in a directory
path = "valid/notRyan"
dirs = os.listdir(path)

i = 0
for item in os.listdir(path):
    try:
        img = cv2.imread(f"valid/notRyan/{item}")
        img = cv2.resize(img, (224, 224))
        img = im.fromarray(img)
        img.save(f"valid/notRyan1/{item}")
    except:
        i += 1
        pass
print(i)
