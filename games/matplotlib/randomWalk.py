from random import choice

from matplotlib import pyplot as plt


class RandomWalk:
    """一个生成随机漫步数据的类。"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性。"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)。
        self.x_values = [0]
        self.y_values = [0]

    def _get_step(self):
        # 正左移动 负右边移动
        # 或者
        # 正上边移动 负下边移动
        direction = choice([1, -1])
        # 移动步数
        distance = choice([0, 1, 2, 3, 4])
        return  direction * distance

    def fill_walk(self):
        """计算漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            # 得到左右移动步数
            x_step = self._get_step()

            # 得到上下移动步数
            y_step = self._get_step()

            # 拒绝原地踏步。
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值。
            # 得到最后一个字，累加当前步数
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 追加
            self.x_values.append(x)
            self.y_values.append(y)




def genImg():
    print("构建随机漫步图")
    # 创建一个RandomWalk实例。
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = range(rw.num_points)
    # 将所有的点都绘制出来。
    plt.style.use('classic')
    # 指定大小
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    # 渐变
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap="Blues", edgecolors='none',s=1)

    # 突出起点和终点。
    ax.scatter(0, 0, c='green', edgecolors='none', s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=10)

    # 隐藏坐标轴。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


if __name__ == '__main__':
    genImg()
    while True:
        is_co = input("按任意键继续，按q退出:")
        if is_co.lower() == 'q':
            break
        else:
            genImg()