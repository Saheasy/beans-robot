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
                        self.board.digital_write(self.hardware['en_right_motor'],0)
                    if event.state < 127:
                        self.board.digital_write(self.hardware['en_right_motor'],1)
                if event.code == "ABS_Y":
                    self.values["left_motor"] = event.state
                    self.board.pwm_write( self.hardware['pwm_left_motor'],abs(int(event.state)-127)*2 )
                    if event.state >= 127:
                        self.board.digital_write(self.hardware['en_left_motor'],0)
                    if event.state < 127:
                        self.board.digital_write(self.hardware['en_left_motor'],1)
if __name__ == "__main__":
    TJ = TrashJuniorRobot(
                 "beans", 
                 {"digitalOutput": {"en_left_motor": 22,"en_right_motor": 23 }, "pwmOutput": {"pwm_left_motor":7,"pwm_right_motor":8 }}, 
                 {"left_motor":0, "right_motor":0} )
    TJ.run()
    