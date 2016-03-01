from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Dilate the image twice to fill in gaps
noPegs = img.dilate(2)
# Then erode the image twice to remove some noise
filled = noPegs.erode(2)
allThree = img.sideBySide(noPegs.sideBySide(filled))
allThree.scale(.5).show()
time.sleep(10)