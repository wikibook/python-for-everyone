#!/usr/bin/env python3

import random

# 헤더를 출력한다
print("Content-Type: text/html")
print("") # 헤더와 몸체를 구별하는 빈 행

# 무작위 수를 얻는다
no = random.randint(1, 6)
# 화면에 출력한다
print("""
<html>
<head><title>Dice</title></head>
<body>
  <h1>{num}</h1>
</body>
</html>
""".format(num=no))
