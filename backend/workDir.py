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



num1 = int(input("탐색 위치 개수는? "))
for _ in range(num1):
    print("탐색 위치는?", end=" ")
    x, y = map(int, input().split(','))
    pos = Position(x, y)
    pred = Predefined()
    temp = []
    # boundary, empty
    temp.append(CheckBoundary())
    temp.append(CheckIsEmptySpot())

    total_map.add_spot(pred, pos, temp)

total_map.print_map()


num2 = int(input("위험 지점 개수는? "))
for _ in range(num2):
    print("위험 지점은?", end=" ")
    x, y = map(int, input().split(','))
    pos = Position(x, y)
    haz = Hazard()
    temp = []
    # boundary, empty
    temp.append(CheckBoundary())
    temp.append(CheckIsEmptySpot())

    total_map.add_spot(haz, pos, temp)

total_map.print_map()


addon = AddOn(total_map, robot)

for _ in range(num1):
    addon.create_path()  # 경로 생성하기
    addon.move_robot()  # 로봇 움직이기