import os
from PIL import Image

def get_image(count):
  scp_command = 'scp pi@192.168.2.5:Desktop/gregTest.jpg ' + 'images/' + str(count) + '.jpg'
  os.system(scp_command)
  return
	# os.system('scp pi@192.168.2.5:Desktop/gregTest.jpg gregTest.jpg')
  #use following to create key if needed:  https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md

def valid_image(path):
	try:
		Image.open(path)
	except IOError:
		return False
	return True
