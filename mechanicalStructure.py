import pyfirmata
from typing import Any, Dict
from motor import model_RC_Servo_MG995
from peripheral import camera
from optimization import PID

class panTilt:
  def __init__(self, COM:str='COM0', setting_pin:Dict={}) -> None:
    self.COM = COM
    self.setting_pin = setting_pin
    
    self.board = pyfirmata.Arduino(self.COM)
    pyfirmata.util.Iterator(self.board).start()
    
    self.motor_1 = model_RC_Servo_MG995(self.board, **setting_pin['motor_1'])
    self.motor_2 = model_RC_Servo_MG995(self.board, **setting_pin['motor_2'])
    self.cam = camera(**setting_pin['camera'])
    