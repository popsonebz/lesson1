from SimpleCV import Image
import time
img = Image('ladies.jpg')
imgBin = img.binarize()
# +morphOpen()+ erodes and then dilates the image
imgBin.morphOpen().show()
time.sleep(10)