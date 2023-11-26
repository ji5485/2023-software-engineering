from packages.Spot import Empty

class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.spots = [[Empty() for _ in range(width)] for _ in range(height)]

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  def get_spot(self, position):
    x, y = position.get_x(), position.get_y()
    return self.spots[y][x]

  def add_spot(self, spot, position, checks):
    pass

  def detect_spot(robot):
    pass

  def arrive_spot(robot):
    pass