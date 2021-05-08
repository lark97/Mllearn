from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
y1 = [1, 2, 3, 1, 3, 2, 2, 1, 1, 2, 2]
y2 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 5, 2]
x = range(15, 26)

plt.figure(figsize=(20, 10), dpi=80)

# 可传参数，color(r,b,m,b,w,c,y,k)，linestyle(-,--,:,-.,'')，linewidth(线条粗细)
plt.plot(x, y1, label="自己", color="r",linestyle=':')
plt.plot(x, y2, label="同桌", color="c",linestyle='-.')
x_tricks = ["{}岁".format(i) for i in x]
plt.xticks(x, x_tricks, fontproperties="FangSong")
# plt.yticks(range(0, 5))

# 把设置号的label图例添加进去
plt.legend(loc=0)
# 绘制网格
plt.grid(alpha=0.4)  # 设置透明度 默认alpha = 1
plt.show()
