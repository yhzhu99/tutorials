# Python Basics #3

**看这个视频**：[Python Tutorial - Python for Beginners [Full Course]](https://www.youtube.com/watch?v=_uQrJ0TkZlc)

关于以下这几个部分的讲解都讲得很浅，可以了解一下(讲深了就不是for Beginners了)

Python面向对象编程其实也算Advanced的特性，像FDU的Python课便没有教面向对象

面向过程、面向对象(还有个函数式编程)都是编程语言中很重要的几个思想，他视频里举的例子简单易懂，蛮好的

## Exceptions 异常

异常处理可以了解一下，有这个东西可以处理异常，它使程序更Robust

```python
try:
    age=int(input("Age: "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")
```

## Classes 类

面向对象编程

```python
class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point()
point2 = Point()

point1.draw()
```

## Constructors 构造函数

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point(2,3)
point2 = Point(5,4)

print(point1.y)
```

## Inheritance 继承

```python
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("wangwangwang")

class Cat(Mammal):
    pass
    # python不允许empty class
    # 至少要有一句pass

dog = Dog()
dog.bark()

cat = Cat()
cat.walk() # Cat和Dog继承了Mammal中的方法walk()
```

## Modules & Packages

主要看一下用法就行，这些功能我所理解的作用是为了让一个项目更易读、易管理、增加可复用性