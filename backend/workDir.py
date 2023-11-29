from packages.AddOn import AddOn
from packages.Check import (Check, CheckBoundary, CheckIsEmptySpot,
                   CheckIsHazardSpot, DetectColorBlobSpot, DetectHazardSpot)
from packages.Map import Map
from packages.Movement import Movement, Forward, Turn
from packages.Path import Path
from packages.Position import Position
from packages.Spot import ColorBlob, Empty, Hazard, Predefined
from api import Robot, SIM



print("맵 크기는?", end= " ")
x, y = map(int, input().split(','))
total_map = Map(x, y)

total_map.print_map()


print("로봇의 시작 위치는?", end=" ")
x, y = map(int, input().split(','))
robot = Robot(Position(x, y))

path = Path()   # 추가함

addon = AddOn(total_map, robot, path)


num1 = int(input("탐색 위치 개수는? "))
for _ in range(num1):
    print("탐색 위치는?", end=" ")
    x, y = map(int, input().split(','))
    addon.create_spot(Predefined(), Position(x, y))
total_map.print_map()


num2 = int(input("중요 지점 개수는? "))
for _ in range(num2):
    print("중요 지점은?", end=" ")
    x, y = map(int, input().split(','))
    addon.create_spot(ColorBlob(), Position(x, y))
total_map.print_map()


num3 = int(input("위험 지점 개수는? "))
for _ in range(num3):
    print("위험 지점은?", end=" ")
    x, y = map(int, input().split(','))
    addon.create_spot(Hazard(), Position(x, y))
total_map.print_map()


for _ in range(num1):
    addon.create_path()  # 경로 생성하기
    while len(addon.path.route) != 0:
        addon.move_robot()  # 로봇 움직이기
    addon.update_robot_position(addon.robot.get_position())
total_map.print_map()
