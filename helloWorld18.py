from SimpleCV import Image
import time
img = Image('ladies.jpg')
blobs = img.findBlobs()
img.crop(blobs[-1]).show()
time.sleep(10)