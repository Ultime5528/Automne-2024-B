import rev

from utils.switch import Switch

import ports
from utils.safesubsystem import SafeSubsystem
from utils.sparkmaxutils import configureLeader


class Turret(SafeSubsystem):

    def __init__(self):
        super().__init__()

        self.motor=rev.CANSparkMax(
            ports.turret_motor, rev.CANSparkMax.MotorType.kBrushless
        )
        configureLeader(self.motor, mode="brake")


        self.encoder = self.motor.getEncoder()

        self.switch = Switch(Switch.Type.NormallyOpen, ports.turret_switch)


    def turn(self, speed):
        self.motor.set(speed)

    def isSwitchPressed(self):
        self.switch.isPressed()

    def stop(self):
        self.motor.stopMotor()

    def getAngle(self):
       return self.encoder.getPosition()



#END
#*roll credits*