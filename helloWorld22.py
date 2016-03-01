from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Rotate the image counter-clockwise 45 degrees
# Rotate the image around the coordinates +(16, 16)+
# Rotate the image, and then resize it so the content isn't cropped
rot = img.rotate(45,point=(16, 16),fixed=False)
rot.show()
time.sleep(10)