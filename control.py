from gpiozero import *
from time import sleep
import argparse

class Computer:
  def __init__(self, pin):
    self.DigitalOutputDevice(pin)
    
  def boot(self):
    self.on()
    sleep(0.5)
    self.off()
    
  def shutoff(self):
    self.on()
    sleep(15)
    self.off()

parser = argparse.ArgumentParser(description='Turn on/off computers.')
parser.add_argument('computer', help='Computer to turn on/off.')
parser.add_argument('state', type=int, help='Use 1 for on and 0 for off')
args = parser.parse_args()
