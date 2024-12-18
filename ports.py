"""from typing import Final"""


"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    drivetrain_motor_fl: Final = 0
    drivetrain_motor_fr: Final = 1
    drivetrain_motor_rr: Final = 2
"""

# CAN
turret_motor = 1


# PWM

shooter_motor_left = 0
shooter_motor_right = 1
pivot_motor = 2


# DIO
turret_switch = 0
pivot_switch = 1
# PCM
shooter_piston_forward=0
shooter_piston_backward=1
