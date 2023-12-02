from packages.Spot import Empty
from .check import Check

class CheckIsEmptySpot(Check):
  def __init__(self):
    pass

  def check(self, mapInfo, position):
    if isinstance(mapInfo.spots[-(position.get_y() + 1)][position.get_x()], Empty):
      return 1
    else:
      print('비어있지 않음')
      return 0