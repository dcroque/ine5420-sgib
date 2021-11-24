from typing import List, Union
import numpy as np

class Point():
    def __init__(self, x: float, y: float, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def toMatrix(self) -> np.matrix:
        return np.matrix(f"{self.x} {self.y} 1")

    def matrixToPoint(self, matrix: np.matrix) -> None:
        self.x = matrix.item(0)
        self.y = matrix.item(1)
        self.z = matrix.item(2)

    def inverse(self):
        return Point(-self.x, -self.y, -self.z)

class Line():
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

class Wireframe():
    def __init__(self, coordinates: List[Point], name: str) -> None:
        self.coordinates = coordinates
        self.name = name

    def centre(self):
        coords = [0,0,0]
        for point in self.coordinates:
            print(f"pontos: {point.x} {point.y} {point.z}")
            coords = [coords[0] + point.x, coords[1] + point.y, coords[2] + point.z]
        n = len(self.coordinates)
        coords = [x/n for x in coords]
        print(f"centroide = {coords}")
        return Point(coords[0], coords[1], coords[2])


class DisplayFile():
    def __init__(self, object: List[Union[Point, Line, Wireframe]]) -> None:
        self.object = object

class TransformOperation():
    def __init__(self, point: Point, operation: int, degree: float = 0) -> None:
        self.point = point
        self.degree = degree
        self.operation = operation