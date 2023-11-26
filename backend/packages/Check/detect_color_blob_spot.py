from packages.Check import CheckBoundary, Check
from packages.Position import Position
from packages.Spot import ColorBlob

class DetectColorBlobSpot(Check):
  def check(self, map, position):
    x, y = position.get_x(), position.get_y()
    return [CheckBoundary().check(map, Position(x + dx, y + dy)) and isinstance(map.get_spot(Position(x + dx, y + dy)), ColorBlob) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
