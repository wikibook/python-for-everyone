import os, sys, math
from sklearn import datasets, svm 
from sklearn.externals import joblib

# 모델 데이터 파일 이름
DIGITS_PKL = "digit-clf.pkl"

# 예측 모델을 생성한다 --- (*1)
def train_digits():
    # 손글씨 숫자 데이터를 읽어들인다
    digits = datasets.load_digits()
    # 훈련한다
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma=0.001)
    clf.fit(data_train, label_train)
    # 예측 모델을 저장한다
    joblib.dump(clf, DIGITS_PKL)
    print("예측 모들을 저장했습니다.=", DIGITS_PKL)
    return clf

# 데이터를 가지고 숫자를 예측한다 --- (*2)
def predict_digits(data):
    # 모델 파일을 읽어들인다
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits() # 모델이 없으면 생성한다
    clf = joblib.load(DIGITS_PKL)
    # 예측
    n = clf.predict([data])
    print("판정 결과=", n)

# 손글씨 숫자 이미지를 8x8 그레이 스케일 데이터 배열로 변환한다 --- (*3)
def image_to_data(imagefile):
    import numpy as np
    from PIL import Image
    image = Image.open(imagefile).convert('L')
    image = image.resize((8, 8), Image.ANTIALIAS)
    img = np.asarray(image, dtype=float)
    img = np.floor(16 - 16 * (img / 256)) # 행렬 연산 --- (*3a)
    # 변환한 이미지를 표시한다(이 부분에 있는 주석 표시를 지우면 이미지를 볼 수 있습니다.) --- (*3b)
    # import matplotlib.pyplot as plt
    # plt.imshow(img)
    # plt.gray()
    # plt.show()
    img = img.flatten()
    print(img)
    return img 

def main():
    # 사용자가 명령 프롬프트에 입력한 인수를 받는다 --- (*4)
    if len(sys.argv) <= 1:
        print("USAGE:")
        print("python3 predict_digit.py imagefile")
        return
    imagefile = sys.argv[1]
    data = image_to_data(imagefile)
    predict_digits(data)

if __name__ == '__main__':
    main()
