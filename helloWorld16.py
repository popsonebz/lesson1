from SimpleCV import Image, Color
import time
img = Image('ladies.jpg')
#print img.size()
# Embiggen the image, put it on a green background, in the upper right
emb = img.embiggen((560, 400), Color.GREEN, (0, 0))
emb.show()
time.sleep(10)