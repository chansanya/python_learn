from random import randint
from plotly import offline
from plotly.graph_objs import Bar, Layout


class Die:
    """这是一个骰子"""

    def __init__(self, num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def rol(self):
        """返回一个骰子的值，大小1~6"""
        return randint(1, self.num_sides)


def draw(dies, results):
    """
    对结果进行可视化

    num_sides:骰子最大数

    frequencies: 数据出现频率
    """
    # 骰子最大值为对个骰子的和
    max_sides = sum(die.num_sides for die in dies)
    max_sides_index = max_sides+1

    # 骰子的最小值为骰子数目：len(dies)
    min_sides = len(dies)
    frequencies = [results.count(num) for num in range(min_sides, int(max_sides_index))]

    # 表格X轴数据为出现的点数
    x_values = list(range(min_sides, max_sides_index))

    print(f"奇数值：{x_values}")
    print(f"对应数据值：{frequencies}")

    #  'dtick': 1 => 刻度
    x_axis_config = {'title': '结果', 'dtick': 1}
    y_axis_config = {'title': '结果的频率'}
    my_layout = Layout(title=f'掷{min_sides}个骰子 {len(results)}次的结果', xaxis=x_axis_config, yaxis=y_axis_config)

    # 表格Y轴数据为出现点数的频率
    data = [Bar(x=x_values, y=frequencies)]
    offline.plot({'data': data, 'layout': my_layout}, filename='./html/d6.html')


if __name__ == '__main__':

    dies = [Die(), Die()]



    results = []

    for roll_num in range(0, 100):
        total_sum = 0
        for die in dies:
            total_sum += die.rol()

        results.append(total_sum)

    draw(dies, results)
