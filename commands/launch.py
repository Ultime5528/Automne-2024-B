from commands2 import SequentialCommandGroup, WaitCommand

from commands.extend import Extend
from commands.retract import Retract
from subsystems.cycler import Cycler
from utils.safecommand import SafeMixin


class Launch(SequentialCommandGroup, SafeMixin):
    def __init__(self, cycler: Cycler):
        super().__init__(
            Extend(cycler),
            WaitCommand(1),
            Retract(cycler)
        )
