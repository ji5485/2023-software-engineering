import numpy as np

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Spot.color_blob import ColorBlob
from Spot.empty import Empty
from Spot.hazard import Hazard
from Spot.predefined import Predefined
from Position.position import Position

from Check.check import Check
from Check.check_boundary import CheckBoundary
from Check.check_is_empty_spot import CheckIsEmptySpot
from Check.check_is_hazard_spot import CheckIsHazardSpot
from Check.detect_color_blob_spot import DetectColorBlobSpot
from Check.detect_hazard_spot import DetectHazardSpot


class Map:

  def __init__(self, width, height):
    self.spots = []
    self.width = width
    self.height = height
    emptySpot = Empty()

    for i in range(height+1):
      temp = []
      for j in range(width+1):
        temp.append(emptySpot)
      self.spots.append(temp)

  def print_map(self):
    show_map = np.zeros((self.height + 1, self.width + 1), dtype=np.int64)
    for i in range(self.width + 1):
      for j in range(self.height + 1):
        if isinstance(self.spots[j][i], ColorBlob):  # ColorBlob = 5
          show_map[j][i] = 5
        if isinstance(self.spots[j][i], Empty):  # Empty = 0
          show_map[j][i] = 0
        if isinstance(self.spots[j][i], Hazard):  # Hazard = 4
          show_map[j][i] = 4
        if isinstance(self.spots[j][i], Predefined):  # Predefined = 7
          show_map[j][i] = 7
    print(show_map)

  def add_spot(self, spot, position, checks):
    num = len(checks)

    for i in range(num):
      if isinstance(checks[i], CheckBoundary):
        if position.x <= self.width and position.y <= self.height:
          pass
        else:
          print('경계 오류')
          return 0
      elif isinstance(checks[i], CheckIsEmptySpot):
        if isinstance(self.spots[-(position.y + 1)][position.x], Empty):
          self.spots[-(position.y + 1)][position.x] = spot
        else:
          print('비어있지 않음')
          return 0
      elif isinstance(checks[i], CheckIsHazardSpot):
        if isinstance(self.spots[-(position.y+1)][position.x], Hazard):
          pass  # hazard 표현
        else:
          pass  # hazard가 아니니 괜찮다~
      elif isinstance(checks[i], DetectColorBlobSpot):
        pass
      elif isinstance(checks[i], DetectHazardSpot):
        pass
      else:
        pass

  def detect_spot(robot):
    pass

  def arrive_spot(robot):
    pass