from packages.Position import Position
from packages.Spot import ColorBlob
from .check import Check
from .check_boundary import CheckBoundary

class DetectColorBlobSpot(Check):
  def check(self, map, position):
    self.map = map
    x, y = position.get_x(), position.get_y()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      pos = Position(x + dx, y + dy)
      if CheckBoundary().check(map, pos):
        self.map.detect_spot(pos)
