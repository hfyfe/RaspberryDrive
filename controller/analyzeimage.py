import SimpleCV
import cv2
import time
from analyzeblob import *
from car_maneuvers import *
from PIL import Image

class AnalyzeImage(object):

  def __init__(self, image_path,connection):
    self.default_command = "stop"
    self.scvImg = SimpleCV.Image(image_path)
    #adding in stop sign logic to check if speed slows down.
    self.reds = self.scvImg.hueDistance(color=SimpleCV.Color.RED)
    self.red_stretched_image = self.reds.stretch(20,21)
    self.red_inverted_image = self.red_stretched_image.invert()
    self.red_blobs = self.red_inverted_image.findBlobs(minsize=4500, maxsize=10000)
    #directional blob logic
    self.segmented_black_white = self.scvImg.stretch(180,181)
    self.black_white_blobs = self.segmented_black_white.findBlobs(minsize=100)
    self.car = CarManeuvers(connection)

  def stopSign(self):
    if ((self.red_blobs) and (len(self.red_blobs) > 0)):
      return True
    else:
      return False

  def runBlobFinder(self):
    if self.stopSign():
      print "STOP SIGN"
      time.sleep(4)
      return
    if ((self.black_white_blobs) and (len(self.black_white_blobs) > 0)):
      self.analyzeBlobs()
    else:
      self.car.forward()
  # print x
	# print blob

  def analyzeBlobs(self):
    blobs = self.scvImg.findBlobs(minsize = 100)
    # if blobs:
    #   for blob in blobs:
    #     if blob.area() > 100:
    #       blob.draw(color=(128,0,0))
    #   self.scvImg.show()
    #   self.scvImg.show()
    #   time.sleep(2)
    #check if blocked
    for blob in self.black_white_blobs:
      print blob
      analyzed_blob = AnalyzeBlob(self.scvImg,blob)

      if analyzed_blob.isBlobBlocking():
        print "Blob blocks path"
        if analyzed_blob.isPocketOnLeft():
          print "Pocket Left"
          self.car.wheels_left_back_up()
          self.car.right()
        elif analyzed_blob.isPocketOnRight():
          print "Pocket right"
          self.car.wheels_right_back_up()
          self.car.left()
        elif analyzed_blob.isBlobBlockingMoreRight():
          print "On Right"
          self.car.wheels_right_back_up()
        else:
          print "On Left"
          self.car.wheels_left_back_up()
        return

      elif analyzed_blob.isBlobDetectedOnLeft():
        print "Small blob on left"
        self.car.right()
        return
      elif analyzed_blob.isBlobDetectedOnRight():
        print "Small blob on right"
        # if analyzed_blob.blockedOnRight():
        self.car.left()
        return
    print "No Blobs in way"
    #otherwise go forward
    self.car.forward()

#  detect blobs
#  if blobs
#    check left and check rightt
#     is blocking?
#         back up
#       else
#         turn (in correct direction)
