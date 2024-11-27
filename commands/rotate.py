import wpilib

from subsystems.pivot import Pivot
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Extend(SafeCommand):
    delay = autoproperty(0.3)

<<<<<<< Updated upstream
    def __init__(self, pivot: Pivot):
        super().__init__()
        self.pivot = pivot
=======
    def __init__(self, turret: Turret, speed:int, stick: wpilib.Joystick):
        super().__init__()
        self.turret = turret
        self.stick = stick
        self.speed = speed
>>>>>>> Stashed changes

    def initialize(self):
        pass

<<<<<<< Updated upstream
=======
    def turn(self):
        pass

>>>>>>> Stashed changes

    def finished(self):
        pass

    def end(self):
        pass