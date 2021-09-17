#from numpy import interp
from pymata4 import pymata4
from inputs import get_gamepad

class robot:
    def map(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def __init__(self):
        self.servoLeft = 8
        self.servoRight = 9

        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_servo(self.servoLeft)
        self.board.set_pin_mode_servo(self.servoRight)

    def drive(self):
        self.board.servo_write(self.servoLeft, int(self.map(self.left, 0, 255, 175, 0)))
        self.board.servo_write(self.servoRight, int(self.map(self.right, 0, 255, 0, 179)))

    def run(self):
        self.left, self.right = 87,89
        while 1:
            events = get_gamepad() #values 0-255 0 == max UP, 0 == max RIGHT
            for event in events:
                if event.code == "ABS_Y":
                    self.left = event.state
                if event.code == "ABS_RZ":
                    self.right = event.state
               
            self.drive()

if __name__ == "__main__":
    jerke = robot()
    jerke.run()