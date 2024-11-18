import wpilib

from utils.switch import Switch

import ports
from utils.safesubsystem import SafeSubsystem

class Pivot(SafeSubsystem):

    def __init__(self):
        super().__init__()

        self.motor=wpilib.VictorSP(ports.pivot_motor)


        self.switch = Switch(Switch.Type.NormallyOpen, ports.pivot_switch)


    def move(self, speed):
        self.motor.set(speed)

    def isSwitchpressed(self):
        self.switch.isPressed()

    def stop(self):
        self.motor.set(0)



#END
#*roll credits*