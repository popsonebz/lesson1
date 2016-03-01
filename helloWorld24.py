from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Flip the image along the horizontal axis, and then display the results
flip = img.flipHorizontal()
flip.show()
time.sleep(10)