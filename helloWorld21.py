from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Rotate the image counter-clockwise 45 degrees
# Rotate the image around the coordinates +(16, 16)+
rot = img.rotate(45,point=(16, 16))
rot.show()
time.sleep(10)