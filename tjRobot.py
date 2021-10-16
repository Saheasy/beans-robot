from robot_classes import robot
from inputs import get_gamepad

class TrashJuniorRobot(robot):
    def run(self):
        while 1:
            print(self.values)
        
            events = get_gamepad()
            for event in events:
                if event.code == "ABS_Z":
                    self.values["servo"] = event.state
                    self.board.servo_write(self.hardware['servo'], int(event.state))
                if event.code == "ABS_RZ":
                    self.values["motor"] = event.state
                    self.board.pwm_write( self.hardware['pwm_motor'],abs(int(event.state)-127)*2 )
                    if value >= 127:
                        self.board.digital_write(self.hardware['en_motor'],1)
                    if value < 127:
                        self.board.digital_write(self.hardware['en_motor'],0)
if __name__ == "__main__":
    TJ = TrashJuniorRobot(
                 "beans", 
                 {"digitalOutput": {"en_motor": 22 }, "pwmOutput": {"pwm_motor":8},"servo": {"servo":7}}, 
                 {"motor":0, "servo":0} )
    TJ.run()
    