import numpy as np
from PIL import Image

def resizeImage(img, panels=6):
    min_height = int(64 * (panels / 2))
    min_width = int(32 * 2)
    img = np.asarray(Image.open(img))
    if (img.shape[0] < min_height) or (img.shape[1] < min_width):
        raise Exception('Image dimensions are not correct. Please ensure that the image is atleast {1} x {2} '.format(min_height, min_width) )
    if (panels == 6):
        pass


resizeImage("test.jpg")

