from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Resize the image, keeping the original height,
# but doubling the width
bigImg = img.resize(img.width * 2, img.height)
bigImg.show()
time.sleep(5)