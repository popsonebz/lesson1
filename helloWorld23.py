from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Rotate the image 90 degrees and make it half the size
rot = img.rotate(90, scale=.5)
rot.show()
time.sleep(10)