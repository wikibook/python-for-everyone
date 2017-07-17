from sklearn import datasets, cross_validation, svm, metrics

# 손글씨 숫자 데이터를 읽어들인다
digits = datasets.load_digits()

# 훈련용 데이터와 테스트용 데이터로 분류한다 --- (*1)
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(digits.data, digits.target)

# SVM 알고리즘을 이용한다 --- (*2)
clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

# 예측해본다 --- (*3)
predict = clf.predict(data_test)

# 결과를 표시한다 --- (*4)
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("분류기 정보=", clf)
print("정답률=", ac_score)
print("보고서=\n", cl_report)
