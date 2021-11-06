from robot_classes import robot
from inputs import get_gamepad

class TrashJuniorRobot(robot):
    def run(self):
        while 1:
            print(self.values)
        
            events = get_gamepad()
            for event in events:
                if event.code == "ABS_RZ":
                    self.values["right_motor"] = event.state
                    self.board.pwm_write( self.hardware['pwm_right_motor'],abs(int(event.state)-127)*2 )
                    if event.state >= 127:
                        self.board.digital_write(self.hardware['in1_right_motor'],0)
                        self.board.digital_write(self.hardware['in2_right_motor'],1)
                    if event.state < 127:
                        self.board.digital_write(self.hardware['in1_right_motor'],1)
                        self.board.digital_write(self.hardware['in2_right_motor'],0)
                if event.code == "ABS_Y":
                    self.values["left_motor"] = event.state
                    self.board.pwm_write( self.hardware['pwm_left_motor'],abs(int(event.state)-127)*2 )
                    if event.state >= 127:
                        self.board.digital_write(self.hardware['in1_left_motor'],0)
                        self.board.digital_write(self.hardware['in2_left_motor'],1)
                    if event.state < 127:
                        self.board.digital_write(self.hardware['in1_left_motor'],1)
                        self.board.digital_write(self.hardware['in2_left_motor'],0)
if __name__ == "__main__":
    TJ = TrashJuniorRobot(
                 "beans", 
                 {
                    "digitalOutput": {
                        "in1_left_motor": 22,
                        "in1_right_motor": 23, 
                        "in2_left_motor": 24,
                        "in2_right_motor": 25 }, 
                    "pwmOutput": {
                        "pwm_left_motor":7,
                        "pwm_right_motor":8 } }, 
                 {"left_motor":0, "right_motor":0} )
    TJ.run()
    