# astar.py

import sys
import time

from matplotlib.patches import Rectangle
import numpy as np

import point


class AStar:
    """A* (A-Star) 算法主类
    """

    def __init__(self, map):
        """类的构造函数
        """
        self.map = map
        self.open_set = []
        self.close_set = []

    def base_cost(self, p):
        """节点到起点的移动代价，对应了g(n)
        """
        x_dis = p.x
        y_dis = p.y
        # 到起点的距离
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def heuristic_cost(self, p):
        """节点到终点的启发函数，对应h(n)
        由于是基于网格的图形，所以本函数和base_cost函数均使用的是对角距离
        """
        x_dis = self.map.size - 1 - p.x
        y_dis = self.map.size - 1 - p.y
        # 到终点的距离
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def total_cost(self, p):
        """代价总和，即对应了f(n)
        """
        return self.base_cost(p) + self.heuristic_cost(p)

    def is_valid_point(self, x, y):
        """ 判断点是否有效，不在地图内部或者障碍物所在点都是无效的
        """
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.is_obstacle(x, y)

    def is_in_point_list(self, p, point_list):
        """判断点是否在某个集合中
        """
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def is_in_open_list(self, p):
        """判断点是否在open_set中
        """
        return self.is_in_point_list(p, self.open_set)

    def is_in_close_list(self, p):
        """判断点是否在close_set中
        """
        return self.is_in_point_list(p, self.close_set)

    def is_start_point(self, p):
        """判断点是否是起点
        """
        return p.x == 0 and p.y == 0

    def is_end_point(self, p):
        """判断点是否是终点
        """
        return p.x == self.map.size - 1 and p.y == self.map.size - 1

    def save_image(self, plt):
        """将当前状态保存到图片中，图片以当前时间命名
        """
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)

    def process_point(self, x, y, parent):
        """针对每一个节点进行处理: 
        如果是没有处理过的节点，则计算优先级设置父节点，并且添加到open_set中
        """
        if not self.is_valid_point(x, y):
            return  # 无效的点直接返回
        p = point.Point(x, y)
        if self.is_in_close_list(p):
            return  # 在close_set中的点直接返回
        print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.is_in_open_list(p):
            p.parent = parent
            p.cost = self.total_cost(p)
            self.open_set.append(p)

    def select_point_in_open_list(self):
        """从open_set中找到优先级最高的节点，返回其索引
        """
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.total_cost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def build_path(self, p, ax, plt, start_time):
        """从终点往回沿着parent构造结果路径
        然后从起点开始绘制结果，结果使用绿色方块，每次绘制一步便保存一张图片
        """
        path = []
        while True:
            path.insert(0, p)  # 先插入
            if self.is_start_point(p):
                break
            else:
                p = p.parent
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()
            self.save_image(plt)
        end_time = time.time()
        print('算法运行时间为', int(
            end_time - start_time), '(秒)')

    def run_and_save_image(self, ax, plt):
        """A*算法的主逻辑
        """
        start_time = time.time()

        start_point = point.Point(0, 0)
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.select_point_in_open_list()
            if index < 0:
                print('没有找到任何一条可行的路径')
                return
            p = self.open_set[index]
            rec = Rectangle((p.x, p.y), 1, 1, color='c')
            ax.add_patch(rec)
            self.save_image(plt)

            if self.is_end_point(p):
                return self.build_path(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # 处理所有的邻居节点
            x = p.x
            y = p.y
            self.process_point(x - 1, y + 1, p)
            self.process_point(x - 1, y, p)
            self.process_point(x - 1, y - 1, p)
            self.process_point(x, y - 1, p)
            self.process_point(x + 1, y - 1, p)
            self.process_point(x + 1, y, p)
            self.process_point(x + 1, y + 1, p)
            self.process_point(x, y + 1, p)
