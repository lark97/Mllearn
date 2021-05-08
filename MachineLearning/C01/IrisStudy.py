# 注意导入包的版本，在这里训练数据集不要用gpu版本，用anoconda自带的版本就好
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas.plotting
import numpy as np

# 观察数据
iris_dataset = load_iris()
x_train, x_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

iris_dataFrame = pd.DataFrame(x_train, columns=iris_dataset.feature_names)
grr = pd.plotting.scatter_matrix(iris_dataFrame, c=y_train, figsize=(15, 15),
                                 marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# matplotlib.pyplot.show()


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)  # 邻居数目设为1
# 传入训练集，构建模型
knn.fit(x_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None,
                     n_jobs=1, n_neighbors=1, p=2, weights='uniform')
x_new = np.array([[5, 2.9, 1, 0.2]])

# 用predict接口判别出类别，完成分类
prediction = knn.predict(x_new)
print("prediction:{}".format(prediction))
print("Predicted target name:{}".format(iris_dataset['target_names'][prediction]))

# 评估模型，score
print("Test set score:{:.2f}".format(knn.score(x_test,y_test)))