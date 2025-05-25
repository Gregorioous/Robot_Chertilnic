from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

class MarkerController:
    def __init__(self, marker_motor):
        self.marker_motor = marker_motor

    def lower_marker(self):
        self.marker_motor.run_time(-350, 500, then=Stop.HOLD, wait=True)

    def raise_marker(self):
        self.marker_motor.run_time(350, 500, then=Stop.HOLD, wait=True)