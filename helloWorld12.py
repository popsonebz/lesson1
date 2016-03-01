from SimpleCV import Image
import time
img = Image('ladies.jpg')
# Get the color distance of all pixels compared to (223, 82)
distance = img.colorDistance(img.getPixel(223, 82))
# Show the resulting distances
print distance
distance.show()
time.sleep(10)