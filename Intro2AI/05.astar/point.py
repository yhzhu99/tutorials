# point.py

import sys


class Point:
    """点类

    Args:
        x (int): 横坐标
        y (int): 纵坐标
        cost (int): 代价，初始一个极大值 sys.maxsize
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = sys.maxsize
