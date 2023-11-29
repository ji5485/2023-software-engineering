from .check import Check
from packages.Spot import Empty

class CheckIsEmptySpot(Check):
  def __init__(self):
    pass

  def check(self, map, position):
    if isinstance(self.spots[-(position.get_y() + 1)][position.get_x()], Empty):
      return 1
    else:
      print('비어있지 않음')
      return 0