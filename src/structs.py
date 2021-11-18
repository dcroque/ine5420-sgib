from typing import List

class Point():
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

class Wireframe():
    def __init__(self, coordinates: List[Point], name: str) -> None:
        self.coordinates = coordinates
        self.transform_coordinates = []
        self.name = name