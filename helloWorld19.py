from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Cropped image that is 200 pixels wide and 200 pixels tall starting at (50, 5).
cropImg = img[50:250,5:205]
cropImg.show()
time.sleep(10)