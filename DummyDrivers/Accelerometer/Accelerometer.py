#Make sure the following libraries are installed:
#   sudo pip3 install RPI.GPIO
#   sudo pip3 install adafruit-blinka
#   sudo pip3 install adafruit-circuitpython-lsm303-accel
#   For LSM303AGR:
#     sudo pip3 install adafruit-circuitpython-lis2mdl
#   For LSM303DLH:
#     sudo pip3 install adafruit-circuitpython-lsm303dlh-mag


#from DummyDrivers.Driver import Driver
import random
#import board
#import busio
#import adafruit_lsm303_accel

class Accelerometer(Driver):
  #Set up I2C link
  #i2c = busio.I2C(board.SCL, board.SDA)

  def __init__(self):
    super().__init__("Accelerometer")

  def read(self):
    return (round(random.randint(0, 10) + random.random(), 2), 
            round(random.randint(0, 10) + random.random(), 2), 
            round(random.randint(0, 10) + random.random(), 2))
