
from subsystems.shooter import Shooter
from utils.safecommand import SafeCommand


class PrepShooter(SafeCommand):
    def __init__(self, shooter: Shooter):
        super().__init__()
        self.shooter = shooter
        self.addRequirements(shooter)

    def execute(self):
        self.shooter.shoot()

    def end(self):
        self.shooter.stop()
