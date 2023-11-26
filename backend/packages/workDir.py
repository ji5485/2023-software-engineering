from AddOn.add_on import AddOn

from Check.check import Check
from Check.check_boundary import CheckBoundary
from Check.check_is_empty_spot import CheckIsEmptySpot
from Check.check_is_hazard_spot import CheckIsHazardSpot
from Check.detect_color_blob_spot import DetectColorBlobSpot
from Check.detect_hazard_spot import DetectHazardSpot

from Map.map import Map
from Movement import forward, movement, turn
from Path import path
from Position.position import Position
from Spot.color_blob import ColorBlob
from Spot.empty import Empty
from Spot.hazard import Hazard
from Spot.predefined import Predefined


import numpy as np

print("맵 크기는?", end= " ")
x, y = map(int, input().split(','))
total_map = Map(x, y)

total_map.print_map()



# print("시작 좌표는?", end= " ")
# x, y = map(int, input().split(','))
# pos = Position(x, y)
# start =
#
# Map = setMap.startPoint(Map, [x, y])
# print(Map)



num = int(input("탐색 위치 개수는? "))
for _ in range(num):
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


num = int(input("위험 지점 개수는? "))
for _ in range(num):
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



print("로봇의 시작 위치는?", end=" ")
x, y = map(int, input().split(','))
point = Position(x, y)              # 형식상 만들기만 함
sightPoint = Position(x+1, y)       # 형식상 만들기만 함

robot = AddOn(total_map, point)            # 로봇 class 만들기 전

robot.create_path()                 # 경로 생성하기




# path = setMap.routeSearch(Map)
# # print(path)
# # setMap.moveSimulation(path, Map)