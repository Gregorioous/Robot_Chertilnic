from RobotMovement import RobotMovement

class DrawingTasks:
    def __init__(self, movement):
        self.movement = movement

    def draw_sq(self, size):
        for _ in range(4):
            self.movement.move_forward(size)
            self.movement.turn(90)  