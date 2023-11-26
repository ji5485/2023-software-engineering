from .spot import Spot

class Empty(Spot):
  def __init__(self):
    self.detected = 1