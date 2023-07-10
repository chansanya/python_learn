import csv
import matplotlib.pyplot as plt
from datetime import datetime


def dram(data, data2, pay_times):
    plt.style.use("seaborn")

    fig, ax = plt.subplots()

    ax.plot(pay_times, data, c="red", alpha=0.5)
    ax.plot(pay_times, data2, c="blue", alpha=0.5)
    ax.fill_between(pay_times, data, data2, pay_times)

    # 设置图形的格式。
    ax.set_title("Amount Statistics", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    # 倾斜日期标签
    fig.autofmt_xdate()
    ax.set_ylabel("Amount", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


file_path = "./source/wx.csv"

with open(file_path) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for item in enumerate(header_row):
        print(item, end="")

    print()
    vals = []
    vals2 = []
    pay_times = []
    for row in reader:
        try:
            val = row[7].replace("`", "")
            val2 = row[6].replace("`", "")
            pay_time = row[0].replace("`", "")
        except ValueError:
            print("解析数据异常")
        else:
            if val:
                print(f"交易时间：{pay_time}，值：{val} 值2：{val2} ")
                vals.append(val)
                vals2.append(val2)
                pay_times.append(datetime.strptime(pay_time, '%Y-%m-%d %H:%M:%S'))

    dram(vals, vals2, pay_times)
