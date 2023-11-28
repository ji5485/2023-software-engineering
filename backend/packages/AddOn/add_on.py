# from packages.Position import Position
# from packages.Spot import Predefined
# path for ji5485


import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Position import Position
from Spot import ColorBlob, Empty, Hazard, Predefined
from Check import (Check, CheckBoundary, CheckIsEmptySpot,
                   CheckIsHazardSpot, DetectColorBlobSpot, DetectHazardSpot)
from Movement import Movement, Forward, Turn

# from Position.position import Position
# from Spot.color_blob import ColorBlob
# from Spot.empty import Empty
# from Spot.hazard import Hazard
# from Spot.predefined import Predefined
# from Check.check import Check
# from Check.check_boundary import CheckBoundary
# from Check.check_is_empty_spot import CheckIsEmptySpot
# from Check.check_is_hazard_spot import CheckIsHazardSpot
# from Check.detect_color_blob_spot import DetectColorBlobSpot
# from Check.detect_hazard_spot import DetectHazardSpot
# from Movement.movement import Movement
# from Movement.forward import Forward
# from Movement.turn import Turn



searchOrder = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상, 하, 우, 좌

class AddOn:
  def __init__(self, map, robot):
    self.map = map
    self.robot = robot

  def create_spot(self, spot, position):
    pass

  def update_robot_position(self, position):
    pass

  def move_robot(self):
    if self.path == -1:
      print('탐색 불가')
      return 0
    while len(self.path) != 0:
      x_diff = self.path[0].get_x() - self.robot.position.get_x()
      y_diff = self.path[0].get_y() - self.robot.position.get_y()
      x_corr = self.robot.get_sight_position().get_x() - self.robot.position.get_x()
      y_corr = self.robot.get_sight_position().get_y() - self.robot.position.get_y()


      if x_diff != 0:
        if x_diff * x_corr <= 0:
          while True:
            Turn().execute(self.robot)
            # print("현재위치", self.robot.position)
            # print("시야", self.robot.get_sight_position())
            x_corr = self.robot.get_sight_position().get_x() - self.robot.position.get_x()
            if x_diff * x_corr > 0:
              break
        Forward().execute(self.robot)
        print("현재위치", self.robot.position)
        # print("시야", self.robot.get_sight_position())
      else:
        if y_diff * y_corr <= 0:
          while True:
            Turn().execute(self.robot)
            # print("현재위치", self.robot.position)
            # print("시야", self.robot.get_sight_position())
            y_corr = self.robot.get_sight_position().get_y() - self.robot.position.get_y()
            if y_diff * y_corr > 0:
              break
        Forward().execute(self.robot)
        print("현재위치", self.robot.position)
        # print("시야", self.robot.get_sight_position())

      del self.path[0]

    print("현재위치", self.robot.position, "탐색완료")
    self.map.get_spot(self.robot.position).detect = 1
    # 탐색 완료를 표시하기 위해 detected 값 바꾸기


  def create_path(self):    # dfs로 수정 예정
    # stack = []
    # self.path = []
    # visited = []
    # branch = []
    # startPoint = self.robot.position
    #
    # stack.append(startPoint)
    # while len(stack) != 0:
    #   here = stack.pop()
    #   self.path.append(here)
    #   if isinstance(self.map.get_spot(here), Predefined):
    #     break
    #   else:
    #     visited.append(here)
    #     count = 0
    #     for i in range(4):
    #       temp = Position(here.get_x() + searchOrder[i][0], here.get_y() + searchOrder[i][1])
    #       if CheckBoundary().check(self.map, temp):
    #         if not CheckIsHazardSpot().check(self.map, temp) and temp not in visited:
    #           count += 1
    #           branch.append(temp)
    #           stack.append(temp)
    #     if count == 1:
    #       del branch[-1]
    #     if count == 0:
    #       while self.path[-1] != branch[-1]:
    #         del self.path[-1]
    #       del self.path[-1]
    #
    # del self.path[0]
    # for i in range(len(self.path)):
    #   print(self.path[i], end=' ')
    # print()

    stack = []
    self.path = []
    visited = []
    branch = []
    startPoint = self.robot.position

    stack.append(startPoint)
    while len(stack) != 0:
      here = stack.pop()
      while here in visited:
        here = stack.pop()
      self.path.append(here)
      if isinstance(self.map.get_spot(here), Predefined) and self.map.get_spot(here).detect == 0:
        break
      else:
        visited.append(here)
        count = 0
        for i in range(4):
          temp = Position(here.get_x() + searchOrder[i][0], here.get_y() + searchOrder[i][1])
          if CheckBoundary().check(self.map, temp):
            if not CheckIsHazardSpot().check(self.map, temp) and temp not in visited:
              count += 1
              branch.append(temp)
              stack.append(temp)
        if count == 1:
          del branch[-1]
        if count == 0:
          while self.path[-1] != branch[-1]:
            del self.path[-1]
          del self.path[-1]

    if isinstance(self.map.get_spot(self.path[-1]), Predefined):
      del self.path[0]
      for i in range(len(self.path)):
        print(self.path[i], end=' ')
      print()
    else:
      print('dfs 경로 탐색 실패')
