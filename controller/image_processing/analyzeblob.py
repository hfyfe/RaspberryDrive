import SimpleCV
import cv2
import time

class AnalyzeBlob(object):

	def __init__(self,img,blob):
		self.vertical_boundary = 0.7
		self.width_boundary = 0.4
		self.img = img
		self.blob = blob
		self.angle_to_turn = 40

	def isBlobBlocking(self):
		if (self.__heightBelowThreshold() and self.__widthSufficientToBlock()):
				return True

	def isBlobDetectedOnLeft(self):
		if (self.__anglingFromLeft() and self.__largeObjectStartingNearLeft()):
			return True
		if (self.__nearLineOnLeft()):
			return True
		if (self.__veryNearBlobOnLeft()):
			return True

	def isBlobDetectedOnRight(self):
		if (self.__anglingFromRight() and self.__largeObjectStartingNearRight()):
			return True
		if self.__nearLineOnRight():
			return True
		if self.__veryNearBlobOnRight():
			return True

	def __nearLineOnRight(self):
		return (self.blob.height() > self.img.size()[1] * 0.90) and (self.blob.minX() > self.img.size()[0] * 0.6)

	def __nearLineOnLeft(self):
		return (self.blob.height() > self.img.size()[1] * 0.90) and (self.blob.maxX() < self.img.size()[0] * 0.4)

	def __veryNearBlobOnRight(self):
		return (self.blob.height() > self.img.size()[1] * 0.40) and (self.blob.minX() > self.img.size()[0] * 0.5) and (self.blob.maxY() > self.img.size()[0] * 0.8)

	def __veryNearBlobOnLeft(self):
		return (self.blob.height() > self.img.size()[1] * 0.40) and (self.blob.maxX() < self.img.size()[0] * 0.5) and (self.blob.height() > self.img.size()[0] * 0.8)

	def __anglingFromRight(self):
		return self.blob.angle() < self.angle_to_turn

	def __largeObjectStartingNearRight(self):
		return (self.blob.maxX() > self.img.size()[0] * 0.80) and (self.blob.width() > self.img.size()[0] * 0.5) and (self.blob.maxY() < self.img.size()[1] * 0.8)

	def isPocketOnRight(self):
		return (self.blob.width() > self.img.size()[0] * 0.8 ) and (self.blob.height() > self.img.size()[0] * 0.8) and (self.blob.maxY() > self.img.size()[1] * 0.5)

	def isPocketOnLeft(self):
		return (self.blob.width() > self.img.size()[0] * 0.8 ) and (self.blob.height() > self.img.size()[0] * 0.8) and (self.blob.maxY() < self.img.size()[1] * 0.5)

	def isBlobBlockingMoreRight(self):
		return self.blob.angle() > 0

	def __anglingFromLeft(self):
		return self.blob.angle() > -1* self.angle_to_turn

	def __largeObjectStartingNearLeft(self):
		return (self.blob.minX() < self.img.size()[0] * 0.20) and (self.blob.width() > self.img.size()[0] * 0.5) and (self.blob.maxY() > self.img.size()[1] * 0.2)

	def __heightBelowThreshold(self):
		return self.blob.maxY() > self.img.size()[1] * self.vertical_boundary

	def __widthSufficientToBlock(self):
		return self.blob.width() > self.img.size()[0] * self.width_boundary


