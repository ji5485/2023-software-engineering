from .spot import Spot
class ColorBlob(Spot):
  def __init__(self):
    self.detect = 0

  def detected(self):
    self.detect = 1
    # 로봇이 상하좌우에서 탐지하는 경우 detect = 1 and 지도에 표시

  def arrived(self):
    pass