from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Binarize the image so that it's a black and white image
imgBin = img.binarize()
# Show the effects of d
# Show the effects of dilate() on the image
#imgBin.show()
imgBin.dilate().show()
time.sleep(10)