from .spot import Spot

class Hazard(Spot):
  def __init__(self):
    self.detect = 1
    # 음성으로 들어왔을 땐 detected: 0 _ 음성 part와 병합하면서 수정