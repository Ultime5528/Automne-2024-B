import wpilib

import ports
from utils.property import autoproperty
from utils.safesubsystem import SafeSubsystem


class Shooter(SafeSubsystem):
    speed = autoproperty(1)

    def __init__(self):
        super().__init__()

        self.left_motor = wpilib.VictorSP(ports.shooter_motor_left)

        self.right_motor = wpilib.VictorSP(ports.shooter_motor_right)

        self.right_motor.setInverted(isInverted=True)

        self.left_motor.addFollower(self.right_motor)

        is_running = False

    def shoot(self):
        is_running = True
        self.left_motor.set(self.speed)

    def stop(self):
        is_running = False
        self.left_motor.stopMotor()
