from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from RobotMovement import RobotMovement
from MarkerController import MarkerController
from DrawingTasks import DrawingTasks

class Robot:
    def __init__(self):
        self.ev3 = EV3Brick()
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)
        self.marker_motor = Motor(Port.A)
        self.gyro_sensor = GyroSensor(Port.S4)
        self.movement = RobotMovement(self.left_motor, self.right_motor, 50, 126, self.gyro_sensor)
        self.marker = MarkerController(self.marker_motor)
        self.tasks = DrawingTasks(self.movement)