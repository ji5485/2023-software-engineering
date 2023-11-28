from .check import Check
from .check_boundary import CheckBoundary

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Spot.color_blob import ColorBlob
from Spot.empty import Empty
from Spot.hazard import Hazard
from Spot.predefined import Predefined



class CheckIsHazardSpot(Check):

  def __init__(self):
    pass
  def check(self, map, position):
    return CheckBoundary().check(map, position) and isinstance(map.get_spot(position), Hazard)

