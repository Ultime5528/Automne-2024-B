import wpilib

import ports
from utils.safesubsystem import SafeSubsystem
from utils.sparkmaxutils import configureLeader, configureFollower


class Shooter(SafeSubsystem):
    def __init__(self):
        super().__init__()

        self.left_motor = wpilib.VictorSP(ports.shooter_motor_left)

        configureLeader(self.left_motor, mode="coast")

        self.right_motor = wpilib.VictorSP(ports.shooter_motor_right)

        configureFollower(self.right_motor, self.left_motor,mode="coast", inverted=True)

    def shoot(self, speed):
        self.left_motor.set(speed)


    def stop(self):
        self.left_motor.stopMotor()