from SimpleCV import Image, Display
import time
img = Image('ladies.jpg')
display = Display()
img.save(display)
#img.show()
time.sleep(5)
