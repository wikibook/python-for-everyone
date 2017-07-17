from sklearn import cross_validation, svm, metrics
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

# 와인 데이터(CSV)를 읽어들인다 --- (*1)
wine = pd.read_csv("winequality-white.csv", delimiter=";")

names = ["fixed acidity","volatile acidity","citric acid", 
    "residual sugar","chlorides", "free sulfur dioxide", 
    "total sulfur dioxide", "density", "pH", "sulphates",
    "alcohol"]
y = wine["quality"] # label

fig, axn = plt.subplots(11, sharey=True)

for i, name in enumerate(names):
    axn[i].set_title(name)
    axn[i].scatter(wine[name], y)

plt.show()
