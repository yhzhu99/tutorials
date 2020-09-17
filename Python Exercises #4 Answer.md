# Python Exercises #4 Answer

## Q6

> 还记得在File I/O一节中遇到的ZeroDivisionError吗？使用Exception处理一下(`print("Error!")`，让程序执行结束，不报错)

**Answer:**

```python
with open("knights.txt","r") as f:
    for line in f:
        try:
            data = line.split()

            name = data[0]
            wins = int(data[1])
            losses = int(data[2])

            win_percent = 100 * wins / (wins + losses)
            print(f"{name}: Wins {win_percent:.2f}%")
        except ZeroDivisionError:
            print("Error!")
```

## Q7

> 编写一个Point类，一个Line类(含Attribute起点、终点)；再编写一个函数`distance()`，计算线段的长度

**Answer:**

```python
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, s, e): # starting & ending point
        self.s = s
        self.e = e

def distance(line):
        return math.sqrt((line.s.x-line.e.x)**2+(line.s.y-line.e.y)**2)

point1 = Point(2,3)
point2 = Point(5,4)
line = Line(point1,point2)

print(distance(line))
```