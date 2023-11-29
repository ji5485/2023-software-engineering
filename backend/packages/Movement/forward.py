from .movement import Movement

class Forward(Movement):
  def execute(self, robot):
    robot.forward()