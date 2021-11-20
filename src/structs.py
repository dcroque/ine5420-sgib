from typing import List, Union

class Point():
    def __init__(self, x: float, y: float, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

class Line():
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

class Wireframe():
    def __init__(self, coordinates: List[Point], name: str) -> None:
        self.coordinates = coordinates
        self.coordinates.append(coordinates[0])
        self.transform_coordinates = []
        self.name = name

class DisplayFile():
    def __init__(self, object: List[Union[Point, Line, Wireframe]]) -> None:
        self.object = object