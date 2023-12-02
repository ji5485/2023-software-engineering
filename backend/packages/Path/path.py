from packages.Movement import Forward, Turn

class Path:
  def __init__(self, route):
      self.route = route
  def createMovement(self, robot):

    nextPos = self.route[0]

    x_diff = nextPos.get_x() - robot.position.get_x()
    y_diff = nextPos.get_y() - robot.position.get_y()
    x_corr = robot.get_sight_position().get_x() - robot.position.get_x()
    y_corr = robot.get_sight_position().get_y() - robot.position.get_y()

    if x_diff != 0:
      if x_diff * x_corr <= 0:
        return Turn()
      else:
        return Forward()
    else:
      if y_diff * y_corr <= 0:
        return Turn()
      else:
        return Forward()


  def removeCurrentPosition(self):
      del self.route[0]