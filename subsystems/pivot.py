import wpilib

from utils.property import autoproperty
from utils.switch import Switch

import ports
from utils.safesubsystem import SafeSubsystem


class Pivot(SafeSubsystem):
    joystick_threshold = autoproperty(0.015)

    def __init__(self):
        super().__init__()

        self.motor = wpilib.VictorSP(ports.pivot_motor)

        self.switch = Switch(Switch.Type.NormallyClosed, ports.pivot_switch)

    def move(self, speed):
        if abs(speed) >= self.joystick_threshold:
            if speed >= 0.0 or not self.switch.isPressed():
                self.motor.set(speed)

        else:
            self.motor.set(0.0)

    def isSwitchPressed(self):
        self.switch.isPressed()

    def stop(self):
        self.motor.stopMotor()

