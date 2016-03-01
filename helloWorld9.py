from SimpleCV import Camera, ImageSet
import time
cam = Camera()
camImages = ImageSet()
# Set to a maximum of 10 images saved
# Feel free to increase, but bewared running out of space
maxImages = 10
for counter in range(maxImages):
    # Capture a new image and add to set
    img = cam.getImage()
    camImages.append(img)
    # Show the image and wait before capturing another
    img.show()
    time.sleep(6)
camImages.save(verbose=True)
