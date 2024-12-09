import rev
from wpiutil import SendableBuilder

from utils.property import autoproperty
from utils.switch import Switch

import ports
from utils.safesubsystem import SafeSubsystem
from utils.sparkmaxutils import configureLeader


class Turret(SafeSubsystem):
    joystick_threshold = autoproperty(0.015)

    def __init__(self):
        super().__init__()

        self.motor = rev.CANSparkMax(
            ports.turret_motor, rev.CANSparkMax.MotorType.kBrushless
        )
        configureLeader(self.motor, mode="brake")

        self.encoder = self.motor.getEncoder()

        self.switch = Switch(Switch.Type.NormallyOpen, ports.turret_switch)

        self.encoder.setPosition(0)

    def isDanger(self):
        return self.motor.get() * self.encoder.getPosition() > 0

    def turn(self, speed):
        if abs(speed) > self.joystick_threshold:
            if not self.isDanger() or not self.switch.isPressed():
                self.motor.set(speed)
            else:
                self.motor.set(0.0)
        else:
            self.motor.set(0.0)

    def simulationPeriodic(self) -> None:
        encoder_next_pos = self.encoder.getPosition() + self.motor.get()
        self.encoder.setPosition(encoder_next_pos)

    def isSwitchPressed(self) -> bool:
        return self.switch.isPressed()

    def stop(self):
        self.motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addBooleanProperty("isSwitchPressed", lambda: self.isSwitchPressed(), noop)
        builder.addFloatProperty("encoderPosition", lambda: self.encoder.getPosition(), noop)
        builder.addFloatProperty("isDanger", lambda: self.isDanger(), noop)
        builder.addFloatProperty("motor.get()", lambda: self.motor.get(), noop)
