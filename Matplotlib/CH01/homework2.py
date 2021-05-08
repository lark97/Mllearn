from matplotlib import pyplot as plt

y = [1, 2, 3, 1, 3, 2, 2, 1, 1, 2, 2]
x = range(15, 26)

plt.figure(figsize=(20, 10), dpi=80)

plt.plot(x, y)
x_tricks = ["{}岁".format(i) for i in x]
plt.xticks(x, x_tricks, fontproperties="FangSong")
plt.yticks(range(0, 5))

# 绘制网格
plt.grid(alpha=0.4)  # 设置透明度 默认alpha = 1
plt.show()
