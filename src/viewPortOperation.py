from structs import Point, Line, Wireframe, TransformOperation
import defaultConfig as dc
from typing import List, Union
import numpy as np

def viewPortTransform(point: Point, winSize: List[float]) -> Point:
    x = (point.x - winSize[0]) / (winSize[2] - winSize[0]) * (dc.XV_MAX - dc.XV_MIN)
    y = (1 - ((point.y - winSize[1]) / (winSize[3] - winSize[1]))) * (dc.YV_MAX - dc.YV_MIN)
    return Point(x, y)

def translationMatrix(translationVector: Point) -> np.matrix:
    return np.matrix(f"1 0 0; 0 1 0; {translationVector.x} {translationVector.y} 1")

def scalingMatrix(scalingFactor: Point) -> np.matrix:
    return np.matrix(f"{scalingFactor.x} 0 0; 0 {scalingFactor.y} 0; 0 0 1")

def rotationMatrix(rotationAngle: float) -> np.matrix:
    return np.matrix(f"{np.cos(np.radians(rotationAngle))} {- np.sin(np.radians(rotationAngle))} 0;" +
    f" {np.sin(np.radians(rotationAngle))} {np.cos(np.radians(rotationAngle))} 0;" +
    " 0 0 1")

def collapseMatrix(tranformOperations: List[TransformOperation], centre: Point) -> np.matrix:
    #operation 0 == translation
    #operation 1 == scaling
    #operation 2 == rotation - origin
    #operation 3 == rotation - object
    #operation 4 == rotation - point
    resultMatrix = np.matrix("1 0 0; 0 1 0; 0 0 1")
    for tranformOperation in tranformOperations:
        if tranformOperation.operation == 0:
            resultMatrix = np.matmul(resultMatrix, translationMatrix(tranformOperation.point))
        elif tranformOperation.operation == 1:
            resultMatrix = np.matmul(resultMatrix, translationMatrix(centre.inverse()))
            resultMatrix = np.matmul(resultMatrix, scalingMatrix(tranformOperation.point))
            resultMatrix = np.matmul(resultMatrix, translationMatrix(centre))
        elif tranformOperation.operation == 2:
            resultMatrix = np.matmul(resultMatrix, rotationMatrix(tranformOperation.degree))
        elif tranformOperation.operation == 3:
            resultMatrix = np.matmul(resultMatrix, translationMatrix(centre.inverse()))
            resultMatrix = np.matmul(resultMatrix, rotationMatrix(tranformOperation.degree))
            resultMatrix = np.matmul(resultMatrix, translationMatrix(centre))
        elif tranformOperation.operation == 4:
            resultMatrix = np.matmul(resultMatrix, translationMatrix(tranformOperation.point.inverse()))
            resultMatrix = np.matmul(resultMatrix, rotationMatrix(tranformOperation.degree))
            resultMatrix = np.matmul(resultMatrix, translationMatrix(tranformOperation.point))
        else:
            print("Deu ruim aqui")
    return resultMatrix