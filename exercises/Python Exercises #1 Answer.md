# Python Exercises #1 Answer

## Q1

> 用for循环打印个九九乘法表

```
1x1=1    
1x2=2    2x2=4    
1x3=3    2x3=6    3x3=9    
1x4=4    2x4=8    3x4=12    4x4=16    
1x5=5    2x5=10    3x5=15    4x5=20    5x5=25    
1x6=6    2x6=12    3x6=18    4x6=24    5x6=30    6x6=36    
1x7=7    2x7=14    3x7=21    4x7=28    5x7=35    6x7=42    7x7=49    
1x8=8    2x8=16    3x8=24    4x8=32    5x8=40    6x8=48    7x8=56    8x8=64    
1x9=9    2x9=18    3x9=27    4x9=36    5x9=45    6x9=54    7x9=63    8x9=72    9x9=81
```

**Answer:**

```python
for i in range(1,10): # 从1开始，<10，默认步长为1
    for j in range(1,i+1):
        print(j,"x",i,"=",j*i, sep="",end=" ")
    print()
```

## Q2

>Calculate area of any triangle

**Example:**

```
Input: 3 4 5
Output: 6

Input: 3 4 8
Output: Illegal

Input: 1.5 2 2.5
Output: 1.5
```

**Answer:**

```python
import math
a,b,c=map(float,input().split())
if(a<=0 or b<=0 or c<=0):
    print("Illegal")
elif(not(a+b>c and b+c>a and c+a>b)):
    print("Illegal")
else:
    p=(a+b+c)/2
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
```
