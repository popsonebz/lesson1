from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Rotate the image counter-clockwise 45 degrees
# Rotate the image clockwise -45 degrees
rot = img.rotate(45)
rot.show()
time.sleep(10)