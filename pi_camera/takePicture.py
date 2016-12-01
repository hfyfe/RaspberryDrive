import picamera as p
import os
import time

os.chdir('/home/pi/Desktop')

cam = p.PiCamera()
cam.resolution = (320,240)
cam.hflip = True
cam.vflip = True

x = 0
while x < 700:
	img = cam.capture('tempGregTest.jpg')
	os.unlink('gregTest.jpg')
	os.rename('tempGregTest.jpg','gregTest.jpg')
	time.sleep(.15)
	x +=1

exit()
