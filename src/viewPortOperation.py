from structs import Point
import defaultConfig as dc

def viewPortTransform(point: Point) -> Point:
    x = (point.x - dc.XW_MIN) / (dc.XW_MAX - dc.XW_MIN) * (dc.XV_MAX - dc.XV_MIN)
    y = 1 - ((point.y - dc.YW_MIN) / (dc.YW_MAX - dc.YW_MIN)) * (dc.YV_MAX - dc.YV_MIN)
    return Point(x, y)