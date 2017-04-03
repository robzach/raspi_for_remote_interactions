from picamera import PiCamera


cam = PiCamera()
cam.resolution = (1024, 768)
cam.start_preview(fullscreen=False,window=(40,40,320,240))
