from .check import Check

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Spot.color_blob import ColorBlob
from Spot.empty import Empty
from Spot.hazard import Hazard
from Spot.predefined import Predefined

class CheckIsEmptySpot(Check):
  def __init__(self):
    pass

  def check(self, map, position):
    if isinstance(self.spots[-(position.get_y() + 1)][position.get_x()], Empty):
      return 1
    else:
      print('비어있지 않음')
      return 0