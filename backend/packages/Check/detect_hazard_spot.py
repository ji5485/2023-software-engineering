from packages.Check import CheckBoundary, Check
from packages.Spot import Hazard

class DetectHazardSpot(Check):
  def check(self, map, position):
    return CheckBoundary().check(map, position) and isinstance(map.get_spot(position), Hazard)
