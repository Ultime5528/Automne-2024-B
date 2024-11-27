import wpilib

from subsystems.turret import Turret
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Rotate(SafeCommand):
    delay = autoproperty(0.3)

    def __init__(self, turret: Turret, speed:int):
        super().__init__()
        self.turret = turret

    def initialize(self):
        pass

    def E(self):
        pass


    def isFinished(self):
        pass

    def end(self):
        pass