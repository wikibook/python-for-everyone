# 정규표현 모듈을 import한다
import re

# 단어 목록
words = [
    "orange", "october", "octpus", 
    "order","banana", "baby", "busy"
]

# 정규표현 패턴에 매칭하는 것을 화면에 출력한다
pattern = r"oc.*"
print("oc로 시작되는 패턴=", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"b.*y"
print("b로 시작하고 y로 끝나는 패턴=", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)


