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

//initialize computers to GPIO pins
compA = Computer(10)
compB = Computer(11)
    
//arg parser
//TODO allow multiple computers to be turned on/off
parser = argparse.ArgumentParser(description = 'Turn on/off computers.')
parser.add_argument('computer', help = 'Computer(s) to turn on/off.')
parser.add_argument('state', type = int, help = 'Use 1 for on and 0 for off')
args = parser.parse_args()

if(state == 0)
  if(computer.find('101') != -1) compA.shutoff()
  if(computer.find('102') != -1) compB.shutoff()
if(state == 1)
  if(computer.find('101') != -1) compA.boot()
  if(computer.find('102') != -1) compB.boot()
  
