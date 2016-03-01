from SimpleCV import VirtualCamera
# Load an existing video into the virtual camera
vir = VirtualCamera("mov.mp4", "video")
#vir.getImage().show()
vir.live()