import SimpleCV as scv
from SimpleCV import Image
import cv2
import time
from start_camera import start_camera
import threading

def take_50_pictures():
  camera_thread = threading.Thread(target=start_camera)
  camera_thread.start()
  from get_images_from_pi import get_image, valid_image
  time.sleep(2)
  count = 0
  while (count < 50):
    get_image(count)
    count += 1

def detect_stop_sign(image):
  reds = image.hueDistance(color=scv.Color.RED)
  stretched_image = reds.stretch(20,21)
  inverted_image = stretched_image.invert()
  blobs = inverted_image.findBlobs(minsize=3500)
  if blobs:
    return True #means there is an obstruction
  return False

# image = Image('images/0.jpg')
x = 18
# while (x < 20):
  # print x
  # image = Image('images/'+ str(x) + '.jpg')
image = Image('images/stop5.jpg')
# segmented_black_white = image.stretch(180,181)
# black_white_blobs = segmented_black_white.findBlobs(minsize=100)
reds = image.hueDistance(color=scv.Color.RED)
red_stretched_image = reds.stretch(20,21)
red_inverted_image = red_stretched_image.invert()
red_blobs = red_inverted_image.findBlobs(minsize=3500)
# print red_blobs
# if red_blobs:
#     for blob in red_blobs:
#         blob.draw(color=(128,0,0))
# if red_blobs:
red_inverted_image.show()
red_inverted_image.show()
time.sleep(10)
x +=1

exit()





