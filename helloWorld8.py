from SimpleCV import Image
img = Image("logo.jpg")
img.save()
# Now save as .jpg
img.save("logo.png")
# Re-saves as .jpg
img.save()