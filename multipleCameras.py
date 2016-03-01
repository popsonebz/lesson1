from SimpleCV import Camera
# First attached camera
cam0 = Camera(0)
# Second attached camera
cam1 = Camera(1)
# Show a picture from the first camera
cam0.getImage().show()
# Show a picture from the second camera
cam1.getImage().show()