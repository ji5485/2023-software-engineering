from .check import Check
from .check_boundary import CheckBoundary
from packages.Spot import Hazard

class CheckIsHazardSpot(Check):

  def __init__(self):
    pass
  def check(self, map, position):
    return CheckBoundary().check(map, position) and isinstance(map.get_spot(position), Hazard)

