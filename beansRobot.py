from robot_classes import robot
if __name__ == "__main__":
    #alice = robot("alice", {"servo": {"servoLeft":8, "servoRight":9} })
    beans = robot("beans", { "digitalOutput": {"in1_FR": 1, "in2_FR": 1, "in1_FL": 1,"in2_FL": 1,"in1_BR": 1,"in2_BR": 1, "in1_BL": 1,"in2_BL": 1 },
                            "pwmOutput": {"en_FR": 0, "en_FL": 0, "en_BR": 0, "en_BL":0} })
    #alice.run()