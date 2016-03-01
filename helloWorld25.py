from SimpleCV import Camera, Display
cam = Camera()
# The image captured is just used to match Display size with the Camera size
disp = Display( (cam.getProperty('width'), cam.getProperty('height')) )
while disp.isNotDone():
    cam.getImage().flipHorizontal().save(disp)