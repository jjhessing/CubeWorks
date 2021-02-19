"""
#Make sure the following libraries are installed:
#   sudo pip3 install RPI.GPIO
#   sudo pip3 install adafruit-blinka
#   sudo pip3 install adafruit-circuitpython-lsm303-accel
#   For LSM303AGR:
#     sudo pip3 install adafruit-circuitpython-lis2mdl
#   For LSM303DLH:
#     sudo pip3 install adafruit-circuitpython-lsm303dlh-mag

Warning: dummy driver is currently set to only run by itself.
It will not be able to run in flight logic without modification

Single line comments  are original driver code commented out for the sake of the
dummy driver. String literals are comments explaining code function
"""

#from Drivers.Driver import Driver
#import board
#import busio
#import adafruit_lsm303_accel

import sys
import random

#class Accelerometer(Driver):
class Accelerometer:
  #Set up I2C link
  #i2c = busio.I2C(board.SCL, board.SDA)
  
  #def __init__(self):
    #super().__init__("Accelerometer")"""
  
  def read(self, t):
    """
    Function that reads and returns accelerometer data
      Dummy driver has been modified to simulate three situations:
      normal values (0), accelerometer crashes and returns nothing (1),
      and incorrect size (2).
      Run using Accelerometer.read(<sitation type>)
    """
    try:
      #accel = adafruit_lsm303_accel.LSM303_Accel(self.i2c)
      if (t == 0):
        accel = float(round(random.randint(1, 10) + random.random(), 2))
      elif (t == 1):
        accel = i
      else:
        if sys.getsizeof(accel[0]) != sys.getsizeof(float(-1.0)):
          raise byteSize
        else:
          accel = int(random.randint(1, 10))
    except:
      print(float(0.0))
      return(float(0.0))
    else:
      print(accel)
      return(accel)

class byteSize(Exception):
  pass