from structs import Point
import defaultConfig as dc
from typing import List

def viewPortTransform(point: Point, winSize: List[float]) -> Point:
    x = (point.x - winSize[0]) / (winSize[2] - winSize[0]) * (dc.XV_MAX - dc.XV_MIN)
    y = (1 - ((point.y - winSize[1]) / (winSize[3] - winSize[1]))) * (dc.YV_MAX - dc.YV_MIN)
    return Point(x, y)