import os

def start_camera():
  os.system('ssh pi@192.168.2.5 python RaspberryDrive/pi_camera/takePicture.py &')
  return

