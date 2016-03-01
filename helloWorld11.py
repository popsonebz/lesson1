from SimpleCV import Image
import time
img = Image('ladies.jpg')
#img.live()
# Gets the information for the pixel located at
# x coordinate = 120, and y coordinate = 150
pixel = img[120, 150]
# or
pixelll = img.getPixel(120, 150)
print pixel
print pixelll
print img.getGrayPixel(120, 150)

print img.height
print img.width

# Retrieve the RGB triplet from (120, 150)
(red, green, blue) = img.getPixel(223, 82)
# Change the color of the pixel+
img[215:230, 82:85] = (0, 0, 0)
# Resize the image so it is 5 times bigger then it's original size
bigImg = img.resize(img.width*1, img.height*1)
bigImg.show()
#img.show()
time.sleep(10)