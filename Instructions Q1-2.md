# Instructions Q1-2

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

- 双重循环的使用
- 格式化输出 (相邻的算式之间一个空格即可)

**Hint:**

```python
help(print) # 这条指令查看print的隐含用法
```

## Q2

> Calculate area of any triangle

**Example:**

```
Input: 3 4 5
Output: 6

Input: 3 4 8
Output: Illegal

Input: 1.5 2 2.5
Output: 1.5
```

**Hint:**

- 如何输入
```python
# 一行输入一个
x=input() # type(x)为str(字符串)
x=int(input()) # str向int转型，读入integer
```

如要一行输入多个数字，见该[blog](https://zhuanlan.zhihu.com/p/25536573)

- 如何使用一些数学Function
  - `import math`
  - [Python中的Math模块的用法](https://zhuanlan.zhihu.com/p/25536573)