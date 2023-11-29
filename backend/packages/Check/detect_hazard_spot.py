from packages.Check import CheckBoundary, Check
from packages.Spot import Hazard
from .check import Check
from .check_boundary import CheckBoundary

class DetectHazardSpot(Check):
  def check(self, map, position):
    self.map = map
    # 이 부분에서 오류가 생길수도 detect attribute 추가
    if CheckBoundary().check(map, position) and isinstance(map.get_spot(position), Hazard) and map.get_spot(position).detect == 0:
      self.map.detect_spot(position)
