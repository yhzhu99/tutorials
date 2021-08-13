# Python Extra Exercises #1 Answer

## Q1

> $1+3/4+5/9+7/16+...+199/10000$

**Answer:**

```python
sum=0
for i in range(1,101):
    sum+=(2*i-1)/(i*i)
print(sum)
```

## Q2

> 编写函数`maximum(a,b,c)`，return a,b,c中最大值

**Answer:**

```python
def maximum(a,b,c):
    return max(max(a,b),c)
```

## Q3

> 编写函数，对给出的一个只含数字的字符串，求其各数位之和

**Example:**

```
Input: 345
Output: 12
```

**Answer:**

```python
def calc_dig_string_sum(s):
    sum=0
    for i in range(0,len(s)):
        sum+=int(s[i])
    return sum
# Test
print(calc_dig_string_sum("345"))
```

## Q4

> 编写函数，判断一个数是否是完全平方数

**Answer:**

```python
from math import sqrt,floor
def is_square(x):
    if(x<0): return False
    if(floor(sqrt(x))*floor(sqrt(x))==x): return True
    return False
# Test
for i in range(-2,26):
    print(i,is_square(i))
```

## Q5

> 在terminal中循环输入整数：
> 
> 如果输入-1，跳出循环；
> 
> 如果输入0~59，`print F`
>
> 60~69：D
> 
> 70~79: C
> 
> 80~89: B
> 
> 90~99: A
> 
> 100: A+
> 
> 输入非以上所提到的值，`print Error`

**Answer:**

```python
while(x:=int(input("print a digit:")))!=-1:
    # New feature in Python 3.8!
    # Use := to assign variables from an expression!
    if(x>=0 and x<60):print("F")
    elif(x<70):print("D")
    elif(x<80):print("C")
    elif(x<90):print("B")
    elif(x<100):print("A")
    elif(x==100):print("A+")
    else:print("Error")
```

## Q6

> 输出 1 1 2 3 5 8 13 21... 小于10000的Fibonacci sequence

**Answer:**

```python
import numpy as np
a=np.zeros(1005,dtype=int)
a[0]=1
a[1]=1
i=1
while(a[i]+a[i-1]<10000):
    a[i+1]=a[i]+a[i-1]
    i+=1
for i in range(0,i+1):
    print(a[i],end=" ")
```

## Q7

> 编写函数，判断一个字符串是否是回文字符串

**Example:**

```
Input: abcba
Output: True

Input: c#d
Output: False
```

**Answer:**

```python
def is_palindrome(s):
    tmp=s[::-1]
    if(s==tmp): return True
    return False
# Test
print(is_palindrome("c#d"))
```
