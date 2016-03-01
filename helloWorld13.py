from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Scale the image by a factor of 2
bigImg = img.scale(2)
bigImg.show()
time.sleep(5)