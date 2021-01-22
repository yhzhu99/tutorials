# Intructions Q5

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

一个关于File I/O和`split()`的小练习

**Hint:**

- 使用`with expr as var`
- `with open("file.txt", "r") as f` 读
- `with open("file.txt", "w") as f` 写
- 将字符串`"xxx"`输出至文件`file`中的方法：`file.write("xxx")`
- `r`、`w`均为`open()`方法中的mode参数，更多关于File的方法可参考这个[Tutorial](https://www.runoob.com/python/file-methods.html)