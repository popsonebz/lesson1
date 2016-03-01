from SimpleCV import Display, Image, Color
winsize = (640,480)
# create a blank window of the size above
display = Display(winsize)
# use the blank window to create an image of same size
img = Image(winsize)
img.save(display)
while not display.isDone():
    # check if the left mouse is clicked
    if display.mouseLeft:
        # if it is clicked, draw a circle
        # the drawing layer function provides access to the circle function
        # the circle function takes the coordinates of the mouse, the desired radius of the circle, color  of circle and
        # whether or not to fill the circle with the color
        img.dl().circle((display.mouseX, display.mouseY), 4, Color.WHITE, filled=True)
        img.save(display)
        img.save("painting.png")
