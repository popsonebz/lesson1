from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Crop starting at +(50, 5)+ for an area 280 pixels wide by 500 pixels tall
cropImg = img.crop(80, 5, 280, 500)
cropImg.show()
time.sleep(10)