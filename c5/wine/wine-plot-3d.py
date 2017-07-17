import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# 와인 데이터(CSV)를 읽어들인다 --- (*1)
wine = pd.read_csv("winequality-white.csv", delimiter=";")

# CVS에서 와인의 등급을 나타내는 열만 가져온다 --- (*2)
y = wine["quality"] # label

# 3D 그래프로 표현한다 --- (*3)
xname = "alcohol"
yname = "sulphates"
zname = "total sulfur dioxide"

plt.style.use('ggplot')
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel(xname)
ax.set_ylabel(yname)
ax.set_zlabel(zname)
ax.scatter3D(
    wine[xname], 
    wine[yname], 
    wine[zname], 
    c=y, s=y**2, cmap="cool")
plt.show()
