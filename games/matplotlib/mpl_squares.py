import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
# 函数subplots()
# 这个函数可在一张图片中绘制一个或多个图表。
# 变量fig 表示整张图片。变量ax 表示图片中的各个图表，大多数情况下要使用它。
fig, ax = plt.subplots()
# ax.plot(squares)
ax.plot(squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)

plt.show()