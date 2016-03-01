from SimpleCV import Camera, Display, Image
import time
# Initialize the Camera
cam = Camera()

# Initialize the Display
display = Display()

# Snap a picture using the Camera
img = cam.getImage()
# Show some text
img.drawText("hello world")

# Show the picture on the Screen
img.save(display)
#img.show()
time.sleep(5)
# note the easier way to capture and display image from camera is
# cam.getImage().show()
#
#
# 
