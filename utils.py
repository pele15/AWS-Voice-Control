import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def restructureImage(img, outputFileName, panels=6):
    img = Image.open(img)
    img = np.array(img)
    if (panels == 6):

        img_top = img[:int(img.shape[0] / 3) , :img.shape[1], :]
        img_middle = img[int(img.shape[0] / 3) : int(img.shape[0] / 3) * 2, :img.shape[1], :]
        img_middle = np.flip(img_middle, axis=0)
        img_middle = np.flip(img_middle, axis=1)
        img_bottom = img[int(img.shape[0] / 3) * 2 : , :img.shape[1], :]
        
        stitched_img = np.empty((img_top.shape[0], img_top.shape[1] * 3, img_top.shape[2]))
        stitched_img = np.hstack((img_top, img_middle, img_bottom))

    
    if (panels == 4):
        img_top = img[:int(img.shape[0] / 2) , :img.shape[1], :]
        img_top = np.flip(img_top, axis=0)
        img_top = np.flip(img_top, axis=1)
        img_bottom = img[int(img.shape[0] / 2) :, :img.shape[1], :]
        #img_bottom = np.flip(img_bottom, axis=0)
        img_bottom = np.flip(img_bottom, axis=1)
                
        stitched_img = np.empty((img_top.shape[0], img_top.shape[1] * 2, img_top.shape[2]))
        stitched_img = np.hstack((img_top, img_bottom))

    stitched_img = Image.fromarray(stitched_img)
    stitched_img.save(outputFileName)



restructureImage("test/twin-ignitions.png", "twin-ignitions-4.jpg", panels=4)
