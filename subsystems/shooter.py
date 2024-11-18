import wpilib

import ports
from utils.safesubsystem import SafeSubsystem


class Shooter(SafeSubsystem):
    def __init__(self):
        super().__init__()

        self.left_motor = wpilib.VictorSP(ports.shooter_motor_left)



        self.right_motor = wpilib.VictorSP(ports.shooter_motor_right)

        self.right_motor.setInverted(isInverted=True)

        self.left_motor.adFollower(self.right_motor)




    def shoot(self, speed):
        self.left_motor.set(speed)


    def stop(self):
        self.left_motor.stopMotor()

