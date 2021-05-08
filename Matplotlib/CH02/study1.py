from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ["FangSong"]
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 11, 12, 15, 14, 15, 17, 17, 18, 21, 20, 14, 15, 16, 19, 21, 20, 23,
       21, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 11, 5, 13, 17, 12, 10,
        11, 10, 12]
x1 = range(1, 32)
x2 = range(40, 71)

plt.figure(figsize=(20, 10), dpi=80)
_x = list(x1) + list(x2)
x_labels = ["3月{}日".format(i) for i in x1]
x_labels += ["10月{}日".format(i - 50) for i in x2]

plt.xticks(_x[::2], x_labels[::2], rotation=45)
plt.xlabel("时间")
plt.ylabel("温度")
# 使用scatter绘制散点图，只有这一点区别
plt.scatter(x1, y_3, label="3月")
plt.scatter(x2, y_10, label="10月")
plt.legend()
plt.show()

# 使用bar绘制条形图，width控制宽度，barh把条形图横着，记住加入height控制宽度
