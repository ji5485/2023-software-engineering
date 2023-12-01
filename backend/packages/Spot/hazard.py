from .spot import Spot

class Hazard(Spot):
  def __init__(self):
    self.detect = 0

  def detected(self):
    self.detect = 1

  def arrived(self):
    print('해저드 도착')
    exit()