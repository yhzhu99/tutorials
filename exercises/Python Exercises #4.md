# Python Exercises #4

## Q6

> 还记得在File I/O一节中遇到的ZeroDivisionError吗？使用Exception处理一下(`print("Error!")`，让程序执行结束，不报错)

```python
with open("knights.txt","r") as f:
    for line in f:
        data = line.split()

        name = data[0]
        wins = int(data[1])
        losses = int(data[2])

        win_percent = 100 * wins / (wins + losses)
        print(f"{name}: Wins {win_percent:.2f}%")
```

## Q7

> 编写一个Point类，一个Line类(含Attribute起点、终点)；再编写一个函数`distance()`，计算线段的长度
