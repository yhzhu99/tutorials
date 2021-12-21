# main.py

from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

import astar
import random_map


plt.figure(figsize=(5, 5))

# 创建一个随机地图
map = random_map.RandomMap()

# 设置图像的内容与地图大小一致
ax = plt.gca()
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])

# 绘制地图:
# 对于障碍物绘制一个灰色的方块，其他区域绘制一个白色的的方块
for i in range(map.size):
    for j in range(map.size):
        if map.is_obstacle(i, j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1,
                            edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

# 绘制起点为蓝色方块
rec = Rectangle((0, 0), width=1, height=1, facecolor='b')
ax.add_patch(rec)

# 绘制终点为红色方块
rec = Rectangle((map.size - 1, map.size - 1), width=1, height=1, facecolor='r')
ax.add_patch(rec)

# 设置图像的坐标轴比例相等并且隐藏坐标轴
plt.axis('equal')
plt.axis('off')
plt.tight_layout()
# plt.show()

# 调用算法来查找路径
a_star = astar.AStar(map)
a_star.run_and_save_image(ax, plt)
