from connect import *
from time import sleep
class CarManeuvers(object):

  def __init__(self,connection):
    self.connection = connection

  def forward(self):
    print "executing forward"
    send_command(self.connection, "forward", "0.5")

  def right(self):
    print "executing right"
    send_command(self.connection, "right", "0.85")

  def left(self):
    print "executing left"
    send_command(self.connection, "left", "0.85")

  def wheels_left_back_up(self):
    print "executing wheels left and backing up"
    send_command(self.connection, "backward left", "0.6")
    # send_command(self.connection, "backward", "0.2")
    sleep(1)
    send_command(self.connection, "wheels right", "0.2")


  def wheels_right_back_up(self):
    print "executing wheels right and backing up"
    send_command(self.connection, "backward right", "0.6")
    # send_command(self.connection, "backward", "0.2")
    sleep(1)
    send_command(self.connection, "wheels left", "0.2")

