from .spot import Spot

class Predefined(Spot):
  def __init__(self):
    self.detect = 0
    # predefined는 지도에 무조건 표시하고, robot이 경유하면 값이 1로 바뀜