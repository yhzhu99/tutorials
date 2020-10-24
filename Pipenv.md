# pipenv的使用

## 安装

```
pip install pipenv
```

## 在新项目使用pipenv管理环境

创建虚拟环境：在项目根目录下执行：

```
pipenv install
```

如要安装django

```
pipenv install django==2.2.13
```

## 启动pipenv

```
pipenv run ...
```

如：

```
pipenv run python manage.py runserver
```

或先进入到虚拟环境：

```
pipenv shell
python manage.py runserver # 省去每次执行命令都要先pipenv run
```



## 删除环境

在以下目录中，将对应的文件夹删除即可

```
C:\Users\xxxxx\.virtualenvs
```

## 其他常见命令

```shell
pipenv install requests # 安装
pipenv install requests==2.13.0 # 指定版本安装
pipenv uninstall requests # 卸载
pipenv update --outdated # 查看所有需要更新的包
pipenv update # 更新所有包
pipenv update <包名> # 更新指定包
pipenv --python 3.6 # 指定python版本
```

### 从requirements.txt中导入

若项目中有requirements.txt文件，则将自动导入

```shell
pipenv install -r path/requirements.txt # requirements.txt在指定位置
```

### 导出requirements.txt

用下面的命令就可以将`Pipfile`和`Pipfile.lock`文件里面的包导出为`requirements.txt`文件。

```
pipenv lock -r
```

