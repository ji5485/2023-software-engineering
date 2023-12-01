from packages.Position import Position
from packages.Spot import Predefined, Hazard
from packages.Movement import Forward, Turn
from packages.Check import (CheckBoundary, CheckIsEmptySpot,
                            CheckIsHazardSpot, DetectColorBlobSpot, DetectHazardSpot)
from packages.Path import Path

searchOrder = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상, 하, 우, 좌

class AddOn:
  def __init__(self, map, robot):
    self.map = map
    self.robot = robot
  def create_spot(self, spot, position):
    temp = []
    # boundary, empty
    temp.append(CheckBoundary())
    temp.append(CheckIsEmptySpot())
    self.map.add_spot(spot, position, temp)

  def update_robot_position(self):
    if self.path.route[0] != self.robot.get_position():
      print('경로 재탐색')
      self.create_path()
      return 0
    else:
      return 1

  def move_robot(self):

    temp = self.path.createMovement(self.robot)

    # 체크하기
    DetectHazardSpot().check(self.map, self.robot.get_sight_position())
    DetectColorBlobSpot().check(self.map, self.robot.get_position())

    if isinstance(temp, Turn):
      temp.execute(self.robot)
    else:
      if isinstance(self.map.get_spot(self.robot.get_sight_position()), Hazard):
        print('경로 재탐색')
        self.create_path()

      temp.execute(self.robot)
      print("현재위치", self.robot.get_position())

      if CheckBoundary().check(self.map, self.robot.get_position()) == 0:
        print('경계를 넘어감')
        exit()

      self.map.arrive_spot(self.robot.get_position()) # Spot에 대하여 도착, 로봇이 움직였으니

      if self.update_robot_position() == 1:
        self.path.removeCurrentPosition()  # 이동 완료한 경로 지우기 / 정상 이동 case



  def create_path(self):
    stack = []
    tempPath = []
    visited = []
    branch = []
    startPoint = self.robot.get_position()

    stack.append(startPoint)
    while len(stack) != 0:
      here = stack.pop()

      tempPath.append(here)
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
              branch.append(here)
              stack.append(temp)
        if count >= 1:
          del branch[-1]
        if count == 0:
          while tempPath[-1] != branch[-1]:
            del tempPath[-1]
          del branch[-1]

    if isinstance(self.map.get_spot(tempPath[-1]), Predefined):
      del tempPath[0]
      self.path = Path(tempPath)
    else:
      print('dfs 경로 탐색 실패')
      return 0
