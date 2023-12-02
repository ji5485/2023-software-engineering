from .spot import Spot

class Predefined(Spot):
  def __init__(self):
    self.detect = 0

  def detected(self):
    pass

  def arrived(self):
    self.detect = 1