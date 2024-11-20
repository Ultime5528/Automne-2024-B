import wpilib
import ports
from utils.safesubsystem import SafeSubsystem


class Cycler(SafeSubsystem):
    def __init__(self):
        super().__init__()

        self.piston = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM,
            ports.shooter_piston_forward,
            ports.shooter_piston_backward
        )



    def goForward(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def goBackward(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def stop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)

