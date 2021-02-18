#Make sure the following libraries are installed:
#   sudo pip3 install RPI.GPIO
#   sudo pip3 install adafruit-blinka
#   sudo pip3 install adafruit-circuitpython-lsm303-accel
#   For LSM303AGR:
#     sudo pip3 install adafruit-circuitpython-lis2mdl
#   For LSM303DLH:
#     sudo pip3 install adafruit-circuitpython-lsm303dlh-mag


#from Drivers.Driver import Driver
import random
"""import board
import busio
import adafruit_lsm303_accel"""
import sys

#class Accelerometer(Driver):
class Accelerometer:
  #Set up I2C link
  #i2c = busio.I2C(board.SCL, board.SDA)
  """
  def __init__(self):
    super().__init__("Accelerometer")
  """

  def read(self, t):
    #accel = adafruit_lsm303_accel.LSM303_Accel(self.i2c)
    try:
      if (t == 0):
        i = float(round(random.randint(0, 10) + random.random(), 2))
      else:
        i = int(random.randint(0, 10))
    except (sys.getsizeof(i)!=16):
      print(float(0.0))
    else:
      print(i)
    

a = Accelerometer()
a.read(0)
a.read(1)