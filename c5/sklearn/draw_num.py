# Scikit learn에 포함된 샘플 데이터를 임포트한다
from sklearn import datasets

# 렌더링하기 위해 matplotlib 모듈을 임포트한다
from matplotlib import pyplot as plt, cm

# 손글씨 데이터를 읽어들인다
digits = datasets.load_digits()
data = digits.images[0]

# 렌더링한다
plt.imshow(data.reshape(8, 8), cmap=cm.gray_r, interpolation='nearest')
plt.show()
