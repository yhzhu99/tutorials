# 人工智能导论补充案例

## 2.6 知识图谱

知识图谱（Knowledge Graph）的构建和表示工具有很多，其中使用图数据库来表示知识图谱的方法较为常用。在本例中我们将会使用一款主流的图数据库： Neo4j 来学习构建一个知识图谱。

Neo4j 的官网是 https://neo4j.com/ 。可从官网注册账号并免费试用。。

不同于 SQL 语言，在 Neo4j 中用于操作数据库的语言是 Cypher。Cypher 是特地为操作图数据库所设计的，能较高效地操作各节点。

```sql
// 创建Sally这个Person类型的结点，该结点的name属性为Sally，age属性为32
CREATE (sally:Person { name: 'Sally', age: 32 })

// 创建John结点
CREATE (john:Person { name: 'John', age: 27 })

// 创建Graph Databases一书所对应的结点
CREATE (gdb:Book { title: 'Graph Databases',
                   authors: ['Ian Robinson', 'Jim Webber'] })

// 在Sally和John之间建立朋友关系，这里的since值应该是timestamp。
CREATE (sally)-[:FRIEND_OF { since: 1357718400 }]->(john)

// 在Sally和Graph Databases一书之间建立已读关系
CREATE (sally)-[:HAS_READ { rating: 4, on: 1360396800 }]->(gdb)

// 在John和Graph Databases一书之间建立已读关系
CREATE (john)-[:HAS_READ { rating: 5, on: 1359878400 }]->(gdb)
```

这一段语句创建了三个节点，Person节点Sally和John，以及Book节点gdb，同时还指定了它们之间的关系。

![create_nodes](https://dist.neo4j.com/wp-content/uploads/modeling_johnsally_properties.jpg)

有了数据后，即可对数据进行操作，实现查询等功能。

```sql
MATCH (sally:Person { name: 'Sally' })
MATCH (john:Person { name: 'John' })
MATCH (sally)-[r:FRIEND_OF]-(john)
RETURN r.since as friends_since
```

如上段语句便可用来在图数据库中查询 Sally 和 John 是什么时候成为朋友的。

## 3.5 家庭财务分配管理系统

见 `03.invest.py` Python 文件。

## 4.7 基于朴素贝叶斯方法的垃圾邮件过滤

主程序见 `04.email.py` Python 文件，数据集在 email_dataset 文件夹下。

借助了 sklearn 机器学习工具包来实现了数据集拆分、朴素贝叶斯预测分类，其所使用到的理论与书中是基本一致的。

最终的预测准确率可在约90%。

## 5.6 无人驾驶中的搜索策略

一个支持A*、Dijkstra、BFS、DFS等各种搜索算法的，且能够可视化搜索过程的网站，见 https://qiao.github.io/PathFinding.js/visual/ 。

Python 中的 networkx 包支持了 A* 算法，可自定义距离估计函数。用法如下：

```python
>>> import networkx as nx
# 一维路径
>>> G=nx.path_graph(5)
>>> print(nx.astar_path(G,0,4))
[0, 1, 2, 3, 4]

# 二维图
>>> G=nx.grid_graph(dim=[3,3]) # nodes are two-tuples (x,y)
>>> def dist(a, b): # 定义距离估计函数
...    (x1, y1) = a
...    (x2, y2) = b
...    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>>> print(nx.astar_path(G,(0,0),(2,2),dist))
[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
```

另外，参考代码见 05.astar 文件夹下，主入口是 main.py 。

## 6.8 账号过滤

见 `06.account.py` Python 文件。