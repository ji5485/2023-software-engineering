import numpy as np
from packages.Spot import Empty, ColorBlob, Hazard, Predefined
from packages.Check import CheckBoundary, CheckIsEmptySpot, CheckIsHazardSpot, DetectColorBlobSpot, DetectHazardSpot

class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.spots = [[Empty() for _ in range(width+1)] for _ in range(height+1)]
    self.numPred= 0
    self.cnt = 0

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  def get_spot(self, position):
    x, y = position.get_x(), position.get_y()
    return self.spots[-(y+1)][x]

  def print_map(self):
    show_map = np.zeros((self.height + 1, self.width + 1), dtype=np.int64)
    for i in range(self.width + 1):
      for j in range(self.height + 1):
        if isinstance(self.spots[j][i], ColorBlob):  # ColorBlob = 5
          if self.spots[j][i].detect == 1:
            show_map[j][i] = 5
          else:
            show_map[j][i] = 0
        if isinstance(self.spots[j][i], Empty):  # Empty = 0
          show_map[j][i] = 0
        if isinstance(self.spots[j][i], Hazard):  # Hazard = 4
          if self.spots[j][i].detect == 1:
            show_map[j][i] = 4
          else:
            show_map[j][i] = 0
        if isinstance(self.spots[j][i], Predefined):  # Predefined = 7
          show_map[j][i] = 7
    print(show_map)

  def add_spot(self, spot, position, checks):
    num = len(checks)
    if isinstance(spot, Predefined):
      self.numPred += 1

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
      elif isinstance(checks[i], CheckIsHazardSpot):    # 굳이 안해도 될거같음
        if isinstance(self.spots[-(position.y+1)][position.x], Hazard):
          pass  # hazard 표현
        else:
          pass  # hazard가 아니니 괜찮다~
      else:
        pass

  def detect_spot(self, position):  # 인자 수정
    self.get_spot(position).detected()
    self.print_map()

  def arrive_spot(self, position):   # 인자 수정
    if isinstance(self.get_spot(position), Predefined) and self.get_spot(position).detect == 0:
      self.cnt += 1
      print('탐색!')
      self.get_spot(position).arrived()
      if self.cnt == self.numPred:
        self.print_map()
        print('탐색 종료')
        exit()
    self.get_spot(position).arrived()


