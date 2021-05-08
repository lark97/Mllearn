import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))
b = np.array(range(10))
print(b)
print(type(b))
c = np.arange(0, 12, dtype='i1')
# 数据类型：dtype,数组类型：type,不要搞混

print(c)
print(c.dtype)


# 数组的形状，表示数组是几行几列shape
# reshape ，改变数组形状
# 数组的维度就等于数字形状shape的个数
print(c.ndim) #表明数组是一个一维数组

#轴的概念 axis