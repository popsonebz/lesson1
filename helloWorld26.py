from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Using Otsu's method
otsu = img.binarize()
# Specify a low value
low = img.binarize(75)
# Specify a high value
high = img.binarize(125)
img = img.resize(int(img.width*.5), int(img.height*.5))
otsu = otsu.resize(int(otsu.width*.5), int(otsu.height*.5))
low = low.resize(int(low.width*.5), int(low.height*.5))
high = high.resize(int(high.width*.5), int(high.height*.5))

top = img.sideBySide(otsu)
bottom = low.sideBySide(high)
combined = top.sideBySide(bottom, side="bottom")

combined.show()
time.sleep(20)