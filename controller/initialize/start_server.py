import os
from time import sleep

def start_server():
  os.system('ssh pi@192.168.2.4 python python-libs/RaspberryDrive/pi_remote_control/driving_server.py &')
  exit()
  # count = 0
  # while count < 2:
  #   send_ssh_server_start(count)
  #   count +=1
  # exit()

def send_ssh_server_start(count):
  try:
    os.system('ssh pi@192.168.2.4 python python-libs/RaspberryDrive/pi_remote_control/driving_server.py &')
    return
  except:
    sleep(count + 1)

