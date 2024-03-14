from pyfirmata import Arduino
from tools import delay_microseconds

class model_RC_Servo_MG995:
    def __init__(self, board:Arduino, pin:int, name=None):
        self.board = board
        self.pin = pin
        self.name = name
        self.servo = board.get_pin(f'd:{pin}:s')
        self.angle_current = 0
        
    def step(self, angle, delay_ms=0):
        self.servo.write(angle)
        delay_microseconds(delay_ms)
        self.angle_current += angle
        return self.angle_current