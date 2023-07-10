import matplotlib.pyplot as plt
# import seaborn as sns
print(plt.style.available)
# 设置样式
plt.style.use('Solarize_Light2')

# 函数subplots()
# 这个函数可在一张图片中绘制一个或多个图表。
# 变量fig 表示整张图片。变量ax 表示图片中的各个图表，大多数情况下要使用它。
fig, ax = plt.subplots()

x_vals = range(1, 100)
y_vals = [x ** 2 for x in x_vals]

# ax.plot(squares)
# 折线图
# ax.plot(x_vals, y_vals, linewidth=3, c='red')
# 散点图
# ax.scatter(x_vals, y_vals, s=10,  c=x_vals, cmap=plt.cm.Blues)
ax.scatter(x_vals, y_vals, s=10,  c=x_vals, cmap='Blues')


# 设置图表标题并给坐标轴加上标签。
ax.set_title("title", fontsize=24)
ax.set_xlabel("x label", fontsize=14)
ax.set_ylabel("y label", fontsize=14)
# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=15)

# 设置刻度
ax.axis([0, 110, 0, 10000])

# 保存
plt.savefig('./images/matplotlib.png', bbox_inches='tight')

# 展示
plt.show()