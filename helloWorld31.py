from SimpleCV import Camera, Display
import time
cam = Camera()
display = Display()
# This variable saves the last rotation, and is used
# in the while loop to increment the rotation
rotate = 0
while display.isNotDone():
    rotate = rotate + 5
    cam.getImage().rotate(rotate).save(display)
    time.sleep(5)
