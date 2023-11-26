from .check import Check

class CheckBoundary(Check):
  def check(self, map, position):
    x, y = position.get_x(), position.get_y()

    return 0 <= x and x <= map.get_width() and 0 <= y and y <= map.get_height()
