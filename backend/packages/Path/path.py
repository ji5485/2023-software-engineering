class Path:
  def __init__(self):
      self.route = None
  def createMovement(self, robot):
      self.robot = robot

      return self.route[0]


  def removeCurrentPosition(self):
      del self.route[0]