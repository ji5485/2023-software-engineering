from api import Robot, SIM
from packages.Position import Position
from packages.Map import Map

robot = Robot(Position(1, 2))
map = Map(4, 5)
sim = SIM()

detect = sim.detect_sensor(map, robot)

print(detect.get("hazard"))
print(detect.get("color_blob"))
print(detect.get("positioning"))