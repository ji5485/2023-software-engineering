from packages.Position import Position
from packages.Spot import Predefined
from packages.Movement import Forward, Turn
from packages.Check import (CheckBoundary, CheckIsEmptySpot,
                            CheckIsHazardSpot, DetectColorBlobSpot, DetectHazardSpot)

searchOrder = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상, 하, 우, 좌

class AddOn:
  def __init__(self, map, robot, path):
    self.map = map
    self.robot = robot
    self.path = path
  def create_spot(self, spot, position):
    temp = []
    # boundary, empty
    temp.append(CheckBoundary())
    temp.append(CheckIsEmptySpot())
    self.map.add_spot(spot, position, temp)

  def update_robot_position(self, position):
    if len(self.path.route) == 0:
      # 체크하기 - check_~

      if isinstance(self.map.get_spot(position), Predefined):
        self.map.arrive_spot(position)
        print("현재위치", self.robot.position, "탐색완료")

  def move_robot(self):
    nextPos = self.path.createMovement(self.robot)  # 인접 경로 받아오기

    x_diff = nextPos.get_x() - self.robot.position.get_x()
    y_diff = nextPos.get_y() - self.robot.position.get_y()
    x_corr = self.robot.get_sight_position().get_x() - self.robot.position.get_x()
    y_corr = self.robot.get_sight_position().get_y() - self.robot.position.get_y()

    if x_diff != 0:
      if x_diff * x_corr <= 0:
        Turn().execute(self.robot)
        # 체크하기
        DetectHazardSpot().check(self.map, self.robot.get_sight_position())
        DetectColorBlobSpot().check(self.map, self.robot.get_position())
      else:
        Forward().execute(self.robot)
        # 체크하기
        DetectHazardSpot().check(self.map, self.robot.get_sight_position())
        DetectColorBlobSpot().check(self.map, self.robot.get_position())
        print("현재위치", self.robot.position)
        self.path.removeCurrentPosition()   # 이동 완료한 경로 지우기
    else:
      if y_diff * y_corr <= 0:
        Turn().execute(self.robot)
        # 체크하기
        DetectHazardSpot().check(self.map, self.robot.get_sight_position())
        DetectColorBlobSpot().check(self.map, self.robot.get_position())
      else:
        Forward().execute(self.robot)
        # 체크하기
        DetectHazardSpot().check(self.map, self.robot.get_sight_position())
        DetectColorBlobSpot().check(self.map, self.robot.get_position())
        print("현재위치", self.robot.position)
        self.path.removeCurrentPosition()  # 이동 완료한 경로 지우기


  def create_path(self):
    stack = []
    tempPath = []
    visited = []
    branch = []
    startPoint = self.robot.position

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
      self.path.route = tempPath

      for i in range(len(self.path.route)):
        print(self.path.route[i], end=' ')
      print()
    else:
      print('dfs 경로 탐색 실패')
      return 0
