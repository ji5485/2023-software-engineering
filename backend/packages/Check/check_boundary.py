from .check import Check

class CheckBoundary(Check):
  def __init__(self):
    pass

  def check(self, map, position):
    if position.x <= self.width and position.y <= self.height:
      return 1
    else:
      print('경계 오류')
      return 0