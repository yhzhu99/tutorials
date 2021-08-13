from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Line:
    def __init__(self,s,e):
        self.s=s
        self.e=e

def distance(line):
    return sqrt((line.s.x-line.e.x)**2+(line.s.y-line.e.y)**2)

point1=Point(2,3)
point2=Point(5,4)
line=Line(point1,point2)

print(distance(line))
