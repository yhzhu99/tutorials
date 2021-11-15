# Tools

## 实用工具

- [在线正则表达式测试](https://tool.oschina.net/regex/)
- [LaTex 公式编辑器](https://www.latexlive.com/)
- [NextITellYou](https://next.itellyou.cn/)
- [Git 约定式提交](https://www.conventionalcommits.org/zh-hans/v1.0.0/)
- [LL LR SLR 分析法](http://jsmachines.sourceforge.net/machines/)
- [Paste Code Image](https://carbon.now.sh/)
- [Hiplot | Visualization of Scientific Data](https://hiplot.com.cn/)
- [PDF to PNG Converter](https://www.freepdfconvert.com/pdf-to-png)
- [PlantUML](https://plantuml.com/zh/)
- [Create LaTeX tables online](https://www.tablesgenerator.com/)
- [HTTP Status Code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
- [REST Resource Naming Guide](https://restfulapi.net/resource-naming/)
- [HTML 转义字符](http://114.xixik.com/character/)
- [diskpart 格式化 U 盘](https://jingyan.baidu.com/article/363872ec22e1336e4ba16f85.html)
- [Restart Shell Script](https://blog.csdn.net/u012081441/article/details/93877212)

## Pip 更换国内源

[Reference](https://blog.csdn.net/yuzaipiaofei/article/details/80891108)

临时使用：在使用 pip 的时候在后面加上 `-i` 参数，指定 pip 源

```sh
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Anaconda 的使用

[Reference](https://www.cnblogs.com/zhangxingcomeon/p/13801554.html)

- 创建 conda 环境

  ```sh
  conda create -n your_env_name python=X.X # (2.7、3.6等)
  ```

- 查看有哪些 conda 环境

  ```sh
  conda env list
  ```

- 进入 conda 环境

  ```sh
  conda activate your_env_name
  ```

- 查看当前环境下的包

  ```sh
  conda list
  ```

- 进入到环境后安装包

  ```sh
  conda install [package]
  ```

- 进入到环境后删除某包

  ```sh
  conda remove [package]
  ```

- 退出 conda 环境

  ```sh
  conda deactivate
  ```

- 删除 conda 环境

  ```sh
  conda remove -n your_env_name --all
  ```

## Ubuntu 中 apt 卸载

[Reference](https://blog.csdn.net/u012843189/article/details/81720854)

- `apt-get remove packagename`

  该命令将移除与 packagename 相关联的所有二进制文件，但是不会移除与之相关联的配置文件或数据文件(configuration or data files)，同样也不会移除 packagename 所依赖的包。

- `apt-get purge packagename` 或者 `apt-get remove --purge packagename`

  这两条命令是等价的。它们的作用是：移除与包 `packagename` 相关联的所有文件，这些文件包括二进制文件和全局配置文件。注意，该命令不会移除 `packagename` 所依赖的包，也不会移除位于用户家目录中的与 `packagename` 相关联的配置文件或数据文件。

  当我们想要完全卸载一个程序的时候，这条命令将特别有用。因为我们经常遇到安装一个应用程序过程中出现安装失败，导致我们需要重新安装它；或者由于某个应用程序的配置文件混乱，我们想完全卸载这个应用程序然后再重新安装，那么就可以使用这条命令先完全卸载应用程序所在的包。

- `apt-get autoremove`

  卸载当前系统中的所有孤立的包(`remove orphaned packages`)，具体指那些曾经被其他包所依赖，但是现在不被任何包依赖了的包。例如，我们用 `apt-get remove --purge packagename` 卸载了 `packagename`，但是 `packagename` 所依赖的包还保留在系统中，这时我们就可以用命令 `apt-get autoremove` 来卸载这些依赖包。注意，这条命令卸载的依赖包一定指的是孤立的包，即不再被任何包给依赖了的包。

- `aptitude remove packagename` 或者 `aptitude purge packagename`

  上面两条命令也会卸载被 `packagename` 依赖但是不被系统中其他包依赖的包。

- `apt-get -s remove packagename`

  这条命令将模拟卸载 `pacagename` 包，但是不会真的卸载。一般在卸载某个包之前，我们先用这条命令来查看一下卸载过程中会卸载哪些内容，防止因为拼错包名 `packagename` 而卸载了不是我们意图卸载的包。

## WSL

- [运行/停止/备份/恢复/删除教程](https://huyangjia.com/computer-technology/905.html)

## Tmux

- [使用教程](https://blog.csdn.net/kikajack/article/details/84188157)

## MySQL

- [Converting a MySQL database from latin1 to utf8](https://techleader.pro/a/420-Converting-a-MySQL-database-from-latin1-to-utf8)
- [阿里云数据库 RDS 申请或释放外网地址](https://help.aliyun.com/document_detail/97736.htm)
- [彻底删除 MySQL](https://www.ywnz.com/linuxysjk/3141.html)
- [How To Install MySQL 8.0 on Ubuntu 20.04](https://computingforgeeks.com/how-to-install-mysql-8-on-ubuntu/)

## Docker

- [停止、删除所有的 Docker 容器和镜像](https://colobu.com/2018/05/15/Stop-and-remove-all-docker-containers-and-images/)

## GitHub

- [GitHub actions runner worker process crashed with error: System.Net.Http.HttpRequestException: The SSL connection could not be established, see inner exception #547](https://github.com/actions/runner/issues/547)

## Node

- [Install Node.js](https://computingforgeeks.com/install-node-js-14-on-ubuntu-debian-linux/)
- [NPM 切换淘宝源](https://www.jianshu.com/p/fa233e05b010)
- [jS heap went out of memory](https://stackoverflow.com/questions/57605441/error-this-is-probably-not-a-problem-with-npm-there-is-likely-additional-loggi)

  ```sh
  node --max_old_space_size=4096 node_modules/@angular/cli/bin/ng build --prod
  ```

## scp

- 应用场景：两台服务器之间免密传输：比如 A 和 B
- 如果之前 A 没有生成过公钥，需要用 `ssh-keygen -t rsa -b 4096` 来生成公钥
- 然后，`cat ~/.ssh/id_rsa.pub`
- 把输出出来的内容粘贴到 B：`vim ~/.ssh/authorized_keys`
- 传输命令如：scp -r ./mmlab yhzhu@10.10.2.5:/home/yhzhu/anaconda3/envs/mmlab
