from SimpleCV import Image
import time
# Load the image
img = Image('ladies.jpg')
# Resize the image, but use the +adaptiveScale()+ function to maintain
# the proportions of the original image
#rather than wrecking the proportions of the original image,it will add padding
adaptImg = img.adaptiveScale((img.width * 2, img.height))
adaptImg.show()
time.sleep(5)