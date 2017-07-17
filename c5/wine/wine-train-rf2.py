from sklearn import cross_validation, svm, metrics

# 와인 데이터(CSV)를 읽어들인다 --- (*1)
wine_csv= []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    no = 0
    for line in fp:
        line = line.strip() 
        cols = line.split(";")
        wine_csv.append(cols)

# 첫 행은 헤더를 포함하므로 삭제한다 --- (*2)
wine_csv = wine_csv[1:]

# CSV의 각 데이터를 수치로 변환한다 --- (*3)
labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols)) # --- (*3a)
    # 와인의 등급을 조정한다 --- (*4)
    grade = int(cols[11]) # 마지막 부분에 있느 데이터가 와인의 등급이다
    if grade == 9: grade = 8 # 샘플 개수가 너무 적으면 조정한다
    if grade < 4 : grade = 5
    labels.append(grade)
    data.append( cols[0:11] ) # 와인의 성분 데이터 --- (*5)

# 훈련용 데이터와 테스트용 데이터로 나눈다 --- (*6)
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(data, labels)

# 랜덤 포레스트 알고리즘을 이용해 학습시킨다 --- (*7)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 예측해본다 --- (*8)
predict = clf.predict(data_test)
total = ok = 0
for idx,pre in enumerate(predict):
	# pre = predict[idx]     # 예측한 등급
	answer = label_test[idx] # 정답 등급
	total += 1
	# 정답에 가까우면 정답으로 여긴다.
	if (pre-1) <= answer <= (pre+1):
		ok += 1
print("정답률=", ok, "/", total, "=", ok/total)


