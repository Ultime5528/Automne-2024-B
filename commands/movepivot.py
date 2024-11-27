import commands2.button

from utils.property import autoproperty
from utils.safecommand import SafeCommand
from subsystems.pivot import Pivot


class MovePivot(SafeCommand):
    convertion_rate = autoproperty(0.5)

    def __init__(
        self,
        pivot: Pivot,
        xbox_remote: commands2.button.CommandXboxController
    ):
        super().__init__()
        self.pivot = pivot
        self.xbox_remote = xbox_remote
        self.addRequirements(pivot)

    def execute(self):
        speed = self.xbox_remote.getLeftY() * self.convertion_rate
        self.pivot.move(speed)

    def isFinished(self):
        return False

    def end(self):
        self.pivot.stop()


    
