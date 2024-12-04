import commands2.button

from subsystems.turret import Turret
from utils.property import autoproperty
from utils.safecommand import SafeCommand


class MoveTurret(SafeCommand):
    convertion_rate = autoproperty(0.1)

    def __init__(
            self,
            turret: Turret,
            xbox_remote: commands2.button.CommandXboxController
    ):
        super().__init__()
        self.turret = turret
        self.xbox_remote = xbox_remote
        self.addRequirements(turret)

    def execute(self):
        speed = self.xbox_remote.getRightX() * self.convertion_rate
        self.turret.turn(speed)

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.turret.stop()



