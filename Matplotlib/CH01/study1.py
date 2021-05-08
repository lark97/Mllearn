from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 1, 16, 17, 20, 19, 24, 21, 16, 13, 13]

# 设置图片大小figsize(长，宽），设置图像清晰度dpi
# plt.figure(figsize=(20, 10), dpi=100)

# plot函数：成图
plt.plot(x, y)

# 设置x轴刻度
# x_labels = [i / 2 for i in range(4, 48)],当需要传小数的时候必须先做出一个列表出来
plt.xticks(range(2, 25))

plt.yticks(range(min(y), max(y) + 1, 2))

# 保存图片
# plt.savefig("./t1.png")

# show 展示
plt.show()
