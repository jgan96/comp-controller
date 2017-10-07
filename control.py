from gpiozero import *
from time import sleep

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

