import random
from matplotlib import pyplot as plt
from matplotlib import font_manager as ft

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['FangSong']  # 用来正常显示中文标签 第二种方式
my_front = ft.FontProperties(fname="C:/Windows/Fonts/simfang.ttf", size=11)  # 第一种方式，使用路径
a = [random.randint(20, 35) for i in range(120)]
x = range(0, 120)
plt.figure(figsize=(20, 10), dpi=80)

_x = list(x)
x_labels = ["10点{}分".format(i) for i in range(60)]
x_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长数据，使x与y一一对应
plt.xticks(_x[::3], x_labels[::3], rotation=45, fontproperties=my_front)
plt.plot(x, a)
plt.show()
