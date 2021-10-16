from robot_classes import robot
from inputs import get_gamepad

class BeansRobot(robot):
    def tankDrive(self, in1, in2, en, value):
        if value >= 127:
            in1 = 1
            in2 = 0
        if value < 127:
            in1 = 0
            in2 = 1
        en = abs(value - 127) * 2
        return (value - 127)*2
        
    def run(self):
        while 1:
            print(self.values)
        
            events = get_gamepad()
            for event in events:
                if event.code == "ABS_Y":
                    self.values["FL"] = self.tankDrive(self.hardware["in1_FL"], self.hardware["in2_FL"], self.hardware["en_FL"], event.state)
                    self.values["BL"] = self.tankDrive(self.hardware["in1_BL"], self.hardware["in2_BL"], self.hardware["en_BL"], event.state)
                if event.code == "ABS_RZ":
                    self.values["FR"] = self.tankDrive(self.hardware["in1_FR"], self.hardware["in2_FR"], self.hardware["en_FR"], -event.state)
                    self.values["BR"] = self.tankDrive(self.hardware["in1_BR"], self.hardware["in2_BR"], self.hardware["en_BR"], -event.state)
if __name__ == "__main__":
    beans = BeansRobot("beans", 
                 {"digitalOutput": {
                    "in1_FR": 1, "in2_FR": 1, 
                    "in1_FL": 1,"in2_FL": 1,
                    "in1_BR": 1,"in2_BR": 1, 
                    "in1_BL": 1,"in2_BL": 1 },
                  "pwmOutput": {
                    "en_FR": 0, 
                    "en_FL": 0, 
                    "en_BR": 0, 
                    "en_BL":0}},
                  {"FR":0, "FL":0, "BR":0, "BL":0})
    beans.run()
    