import wpilib

from subsystems.pivot import Pivot
from subsystems.turret import Turret
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Extend(SafeCommand):
    delay = autoproperty(0.3)


    def __init__(self, turret:Turret, speed:int, stick: wpilib.Joystick):
        super().__init__()
        self.turret = turret
        self.stick = stick
        self.speed = speed


    def initialize(self):
        pass


    def turn(self):
        pass



    def finished(self):
        pass

    def end(self):
        pass