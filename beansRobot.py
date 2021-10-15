#from numpy import interp
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
                self.hardware.update(hardware[i])
            except:
                print("not in hardware")
    
    def run(self):
        self.left, self.right, self.gripper = 87,89, 0
        while 1:
            events = get_gamepad() #values 0-255 0 == max UP, 0 == max RIGHT
            for event in events:
                if event.code == "ABS_Y":
                    self.left = event.state
                if event.code == "ABS_RZ":
                    self.right = event.state
                
            self.board.servo_write(self.servoLeft, int(self.map(self.left, 0, 255, 175, 0)))
            self.board.servo_write(self.servoRight, int(self.map(self.right, 0, 255, 0, 179)))
            self.board.servo_write(self.servoGripper, int(self.map(self.gripper, 0, 255, 0, 180)))

if __name__ == "__main__":
    alice = robot("alice", {"servo": {"servoLeft":8, "servoRight":9} })
    beans = robot("beans", { "digitalOutput": {"in1_FR": 0, "in2_FR": 0, "in1_FL": 0,"in2_FL": 0,"in1_BR": 0,"in2_BR": 0, "in1_BL": 0,"in2_BL": 0 },
                            "pwmOutput": {"en_FR": 0, "en_FL": 0, "en_BR": 0, "en_BL":0} })
    #alice.run()