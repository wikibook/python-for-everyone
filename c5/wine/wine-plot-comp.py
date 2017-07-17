from sklearn import cross_validation, svm, metrics
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA

# 와인 데이터(CSV)를 읽어들인다 --- (*1)
wine = pd.read_csv("winequality-white.csv", delimiter=";")

X = wine[["fixed acidity","volatile acidity","citric acid", 
    "residual sugar","chlorides", "free sulfur dioxide", 
    "total sulfur dioxide", "density", "pH", "sulphates",
    "alcohol"]] # data
y = wine["quality"] # label


# 차원 압축
comp = TruncatedSVD(n_components=2)
X_reduced = comp.fit_transform(X)

# 그래프를 그린다
plt.style.use('ggplot')
plt.scatter(
    X_reduced[:,0], 
    X_reduced[:,1], 
    c=y, 
    s=y*3, cmap="Reds")
plt.show()

