from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

class RobotMovement:
    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track, gyro_sensor, simulator=None):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.gyro_sensor = gyro_sensor
        self.simulator = simulator

    def move_forward(self, dist, speed=200):
        degrees = (dist / (self.wheel_diameter * 3.14159)) * 360
        self.left_motor.run_angle(speed, degrees, then=Stop.HOLD, wait=False)
        self.right_motor.run_angle(speed, degrees, then=Stop.HOLD, wait=True)

    def turn(self, angle, speed=50):
        self.gyro_sensor.reset_angle(0)
        turn_rate = (self.axle_track / self.wheel_diameter) * angle
        initial_left_angle = self.left_motor.angle()
        initial_right_angle = self.right_motor.angle()
        target_left_angle = initial_left_angle - turn_rate
        target_right_angle = initial_right_angle + turn_rate
        self.left_motor.run_target(speed, target_left_angle)
        self.right_motor.run_target(speed, target_right_angle)
        wait(500)  # Уменьшили до 500 мс
        self.left_motor.stop()
        self.right_motor.stop()
        wait(500)
        final_angle = self.gyro_sensor.angle()

    def res_gyr(self):
        self.gyro_sensor.reset_angle(0)
        wait(100)