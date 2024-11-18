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

        self.is_forward=False


    def goForward(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)
        self.is_forward = True

    def goBackward(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)
        self.is_forward = False

    def stop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)

