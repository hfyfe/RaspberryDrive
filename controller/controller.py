import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
import analyzeblob
import analyzeimage
from analyzeimage import *
from analyzeblob import *
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation,send_end_connection
from start_camera import start_camera
from start_server import start_server
import threading

def start_server_thread():
	server_thread = threading.Thread(target=start_server)
	server_thread.start()

def start_camera_thread():
	camera_thread = threading.Thread(target=start_camera)
	camera_thread.start()

def start_all():
  start_server_thread()
  start_camera_thread()
  sleep(7)
  s = new_connection()
  return s
  #start the server listening on contr pi
  #start the camera taking pictures on camera pi
  # Sleep to make sure server connects
  #start the server connection on this current server

def end_all(server):
  send_end_connection(server)
  server.close()
  #End-all
  #Camera exits automatically automatically
  #Close the Server Connection on the Pi-Controller End
  #Kill the server listening process

def run(server):
  count = 0
  while (count < 200):
    print count
    #retrieve image.
    get_image(count)
    image_path = os.getcwd() + "/images/" + str(count) + ".jpg"
    if valid_image(image_path):
      #Blog Detection
      analyzed_image = AnalyzeImage(image_path, server)
      analyzed_image.runBlobFinder()
      sleep(0.7)
    count += 1

server = start_all()
run(server)
end_all(server)
#exit out of controller
exit()
