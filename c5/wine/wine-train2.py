from sklearn import cross_validation, svm, metrics

# 와인 데이터(CSV)를 읽어들인다
wine_csv= []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    no = 0
    for line in fp:
        line = line.strip() 
        cols = line.split(";")
        wine_csv.append(cols)

# 첫 행은 헤더를 포함하므로 삭제한다
wine_csv = wine_csv[1:]

# CSV의 각 데이터를 수치로 변환한다
labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))
    grade = int(cols[11]) # 마지막 부분에 있느 데이터가 와인의 등급이다
    labels.append(grade)
    data.append( cols[0:11] ) # 와인의 성분 데이터

# 훈련용 데이터와 테스트용 데이터로 나눈다
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(data, labels)

# 랜덤 포레스트 알고리즘을 이용한다 
clf = svm.SVC(probability=True)
clf.fit(data_train, label_train)

# 예측해본다
total = ok = 0
for idx, td in enumerate(data_test):
    predict = clf.predict(td)
    prob = clf.predict_proba(td)
    print(prob)
    answer = label_test[idx]
    total += 1
    if predict == answer:
        ok += 1
    else:
        if (predict-1) <= answer <= (predict+1):
            ok += 1
print(ok, "/", total, "=", ok/total)

#
predict = clf.predict(data_test)
n = clf.score(data_test, label_test)
print(n)

# 결과를 표시한다
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률=", ac_score)
print("보고서=\n", cl_report)

