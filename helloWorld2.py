from SimpleCV import Camera, Display, Image
import time
# Initialize the Camera
# note, the 0 indicates the first camera device on your pc
# on linux use ls /dev/video* to check the numbers.
# Specifying the resolution size of the capture as a dictionary 640x480
cam = Camera(0, {"width": 640, "height": 480})

# Snap a picture using the Camera
img = cam.getImage()
# Note, to get the coordinate of points on the image and their color value, use the live() method on the image.
# click on points on the image while looking at the terminal for the values
# img.live()
# Show some text starting from the coordinate (160, 120)
img.drawText("hello world", 160, 120)

# Show the picture on the Screen
img.show()
# wait for 5 seconds before closing it
time.sleep(5)
