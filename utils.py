import numpy as np
from PIL import Image

def resizeImage(img, panels=6):
    if (panels == 6):
        img = Image.open(img)