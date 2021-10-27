import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def restructureImage(img, outputFileName, panels=6):
    if (panels == 6):
        img = Image.open(img)
        img = np.array(img)
        img_top = img[:int(img.shape[0] / 3) , :img.shape[1], :]
        img_middle = img[int(img.shape[0] / 3) : int(img.shape[0] / 3) * 2, :img.shape[1], :]
        img_middle = np.flip(img_middle, axis=1)
        img_bottom = img[int(img.shape[0] / 3) * 2 : , :img.shape[1], :]
        
        stitched_img = np.empty((img_top.shape[0], img_top.shape[1] * 3, img_top.shape[2]))
        stitched_img = np.hstack((img_top, img_middle, img_bottom))
        stitched_img = Image.fromarray(stitched_img)
        stitched_img.save(outputFileName)



restructureImage("test/twin-ignitions.png", "twin-ignitions.jpg")
