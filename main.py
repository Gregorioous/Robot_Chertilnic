#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile
from Robot import Robot

robot = Robot()
robot.ev3.speaker.beep()
robot.movement.res_gyr()
wait(1000)
robot.marker.lower_marker()
robot.tasks.draw_sq(500)
robot.marker.raise_marker()
robot.ev3.speaker.beep()