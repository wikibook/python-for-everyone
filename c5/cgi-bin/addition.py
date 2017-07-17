#!/usr/bin/env python3
# 덧셈 프로그램

import cgi

# 헤더를 출력한다
print("Content-Type: text/html")
print("")

# 송신되어져 온 폼 데이터를 받는다
form = cgi.FieldStorage()

# 폼에 v1과 v2라는 데이터가 포함돼 있는지 확인한다 --- (*1)
if (not 'v1' in form) or (not 'v2' in form):
    # 포함돼 있지 않으면 폼을 표시한다
    print("""
        <form>
        <input type="text" name="v1"> +
        <input type="text" name="v2">
        <input type="submit" value="계산">
        </form>
    """)
else:
    # 폼의 값을 가져와서 계산하고 결과를 표시한다 --- (*2)
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print("<h1>", ans, "</h1>")
