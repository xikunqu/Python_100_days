from PIL import Image,ImageFilter

image=Image.open("E:\study\Python_100_days\D1-15\Day15\\1c623da59b6b4827a2f354ea234fffce.jpg")
#print(image.format,image.size,image.mode)

#rect=80,20,310,360
#image.crop(rect)

# size=128,128
# image.thumbnail(size)

# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()
#image.show()

# for x in range(80,310):
#     for y in range(20,360):
#         image.putpixel((x,y),(128,128,128))
#
# image.show()

image.filter(ImageFilter.CONTOUR).show()