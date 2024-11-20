import wpilib

from subsystems.cycler import Cycler
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Retract(SafeCommand):
    delay = autoproperty(0.3)

    def __init__(self, cycler: Cycler):
        super().__init__()
        self.cycler = cycler
        self.timer = wpilib.Timer()
        self.addRequirements(cycler)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.cycler.goBackward()

    def isFinished(self):
        return self.timer.get >= self.delay

    def end(self):
        self.cycler.stop()
