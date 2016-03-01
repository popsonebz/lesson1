from SimpleCV import Image
import time
img = Image('ladies.jpg')
imgBin = img.binarize()
# Like the previous example, but erode()
imgBin.erode().show()
time.sleep(10)