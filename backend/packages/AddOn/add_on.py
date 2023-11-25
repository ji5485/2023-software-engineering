import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Spot.color_blob import ColorBlob
from Spot.empty import Empty
from Spot.hazard import Hazard
from Spot.predefined import Predefined
from Position.position import Position

class AddOn:
  def __init__(self, map, point):   # robot 잠시 제거, def __init__(self, map, robot):
    self.map = map
    self.point = point      # 임시, 로봇의 현재 위치
    # self.robot = robot

  def create_spot(self, spot, position):
    pass

  def update_robot_position(self, position):
    pass

  def move_robot(self):
    pass

  def create_path(self):
    predSet = []
    # 로봇의 위치 좌표와 시야 좌표를 가지고 경로를 생성하는 부분
    for i in range(self.map.width + 1):
      for j in range(self.map.height + 1):
        if isinstance(self.map.spots[j][i], Predefined):
          pos = Position(i, len(self.map.spots) - j - 1)
          predSet.append(pos)

    robotPosition = self.point

    path = [robotPosition]

    while len(predSet) != 0:
      x_diff = predSet[0].x - robotPosition.x
      y_diff = predSet[0].y - robotPosition.y

      path = [robotPosition]

      if x_diff > 0:
        for i in range(x_diff):
          path.append(Position(path[-1].x + 1, path[-1].y))
      else:
        for i in range(abs(x_diff)):
          path.append(Position(path[-1].x - 1, path[-1].y))

      if y_diff > 0:
        for i in range(y_diff):
          path.append(Position(path[-1].x, path[-1].y + 1))
      else:
        for i in range(abs(y_diff)):
          path.append(Position(path[-1].x, path[-1].y - 1))
      del path[0]

      for i in range(len(path)):
        if i == len(path) - 1:
          print(f"({path[i].x}, {path[i].y})", end='')
        else:
          print(f"({path[i].x}, {path[i].y})", end='->')

      print('\n', end='')

      del predSet[0]

