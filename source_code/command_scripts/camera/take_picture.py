from picamera import PiCamera

def take_picture(picture_location):
	camera = PiCamera()
	camera.start_preview()
	camera.capture(picture_location)
	camera.stop_preview()

if __name__ == "__main__":
	take_picture("picture.jpg")
