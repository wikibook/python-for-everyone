#!/usr/bin/env python3
import cgi

# 헤더를 표시한다
print("Content-Type: text/html; charset=utf-8")
print("") # 빈 행

print("<pre>")
# URL 매개변수를 받는다 ---- (*1)
form = cgi.FieldStorage()

# 특정 매개변수를 받아서 표시한다 --- (*2)
mode = form.getvalue("mode", default="")
print("mode=", mode)

# 모든 매개변수를 받아서 표시한다 --- (*3)
print("--- all params ---")
for k in form.keys():
    print(k,"=",form.getvalue(k))
