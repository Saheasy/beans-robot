from pymata4 import pymata4
from inputs import get_gamepad

class robot:
    def map(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
        
    def __init__(self, name, hardware):
        self.name = name
        self.board = pymata4.Pymata4()
        self.hardware = {}
        HARDWARE_TYPES = {  "servo":self.board.set_pin_mode_servo,
                            "stepper":self.board.set_pin_mode_stepper,
                            "sonar":self.board.set_pin_mode_sonar, 
                            "digitalOutput":self.board.set_pin_mode_digital_output, 
                            "digitalInput":self.board.set_pin_mode_digital_input, 
                            "analogInput":self.board.set_pin_mode_analog_input, 
                            "pwmOutput":self.board.set_pin_mode_pwm_output }
        for i in hardware.keys():
            try: 
                [HARDWARE_TYPES[i](hardware[i][j]) for j in hardware[i].keys()]
                self.hardware.update({ j:0 for j in hardware[i].keys()})
            except:
                print("not in hardware")
        