#!/usr/bin/env python3
from typing import Optional

import commands2.button
import wpilib
from commands.prepshooter import PrepFlywheels
from subsystems.shooter import Shooter

class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        wpilib.LiveWindow.enableAllTelemetry()
        wpilib.LiveWindow.setEnabled(True)
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)

        """
        Autonomous
        """
        self.auto_command: Optional[commands2.Command] = None
        self.auto_chooser = wpilib.SendableChooser()

        """
        Joysticks
        """
        self.xbox_controller = commands2.button.CommandXboxController(0)

        """
        Subsystems
        """

        """
        Default subsystem commands
        """

        """
        Setups
        """
        self.setupAuto()
        self.setupButtons()
        self.setupDashboard()

    def setupAuto(self):
        self.auto_chooser.setDefaultOption("Nothing", None)
        wpilib.SmartDashboard.putData("Autonomous mode", self.auto_chooser)

    def setupButtons(self):
        """
        Bind commands to buttons on controllers and joysticks
        """

    def setupDashboard(self):
        """
        Send commands to dashboard to
        """
        pass
          
    def autonomousInit(self):
        self.auto_command: commands2.Command = self.auto_chooser.getSelected()
        if self.auto_command:
            self.auto_command.schedule()

    def teleopInit(self):
        if self.auto_command:
            self.auto_command.cancel()



if __name__ == "__main__":
    wpilib.run(Robot)

