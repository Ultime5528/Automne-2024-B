import wpilib

from subsystems.cycler import Cycler
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class Extend(SafeCommand):
    delay = autoproperty(2)

    def __init__(self, cycler: Cycler):
        super().__init__()
        self.cycler = cycler
        self.timer = wpilib.Timer()
        self.addRequirements(cycler)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.cycler.goForward()

    def isFinished(self):
        return self.timer.get() >= self.delay

    def end(self, interrupted: bool):
        self.cycler.stop()
