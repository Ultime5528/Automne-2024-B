import wpilib

from subsystems.pivot import Pivot
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Extend(SafeCommand):
    delay = autoproperty(0.3)

    def __init__(self, pivot: Pivot):
        super().__init__()
        self.pivot = pivot

    def initialize(self):
        pass


    def isFinished(self):
        pass

    def end(self):
        pass