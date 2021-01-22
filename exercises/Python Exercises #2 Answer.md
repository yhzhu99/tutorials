# Python Exercises #2 Answer

## Q3

> 编写一个函数`maxOfList()`，求一个numeric列表的最大元素(不使用Python内置函数`max()`等；若列表内没有元素，`return "No element"`)

**Answer:**

```python
def maxOfList(list):
    n=len(list)
    if(n==0):
        return "No element"
    res=list[0]
    for i in range(0,n):
        if(res<list[i]):
            res=list[i]
    return res
# Test
arr=[3,5,1,2,4]
mmax=maxOfList(arr)
print(mmax)
```

## Q4

> 编写一个函数`isPrime()`，判断一个**整数**是否是素数(是素数返回`True`，否则返回`False`)

**Answer:**

```python
def isPrime(x):
    if(x<2): return False
    if(x==2): return True
    for i in range(2,x):
        if(x%i==0): return False
    return True
# Test
for i in range(-2,20):
    print(i,isPrime(i))
```

**An optimization algorithm**

```python
import math
def isPrime(x):
    if(x<2): return False
    if(x==2): return True
    for i in range(2,math.floor(math.sqrt(x))+1):
        if(x%i==0): return False
    return True
# Test
for i in range(-2,20):
    print(i,isPrime(i))
```