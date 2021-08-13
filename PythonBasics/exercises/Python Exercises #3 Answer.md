# Python Exercises #3 Answer

## Q5

> 读文件`in.txt`(多行)，对其中的data(name birthday)按以下Example中所示的处理方法，输出至`out.txt`

**Example:**

`in.txt` => `out.txt`

- `in.txt`

```
wangchengxuan 2000-11-09
caixukun 1998-08-02
qiaobenhuannai 1999-02-03
```

- `out.txt`

```
wangchengxuan 2000.11.9
caixukun 1998.8.2
qiaobenhuannai 1999.2.3
```

**Answer:**

```python
with open("in.txt", "r") as source:
    with open("out.txt", "w") as target:
        for line in source:
            data = line.split()

            name = data[0]
            ymd = data[1].split("-")

            year = int(ymd[0])
            month = int(ymd[1])
            day = int(ymd[2])

            s = str(name)+" "+str(year)+"."+str(month)+"."+str(day)+"\n"
            target.write(s)
```