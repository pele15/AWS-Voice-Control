from PIL import Image

basewidth = 128
hsize = 64
img = Image.open('C:\\Users\\Praneeth\\Desktop\\car.JPEG')
# wpercent = (basewidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))

img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_image.jpg')