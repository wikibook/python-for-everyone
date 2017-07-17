#!/usr/bin/env python3
import cgi

# ヘッダの表示
print("Content-Type: text/html; charset=utf-8")
print("") # 空行

print("<pre>")
# URLパラメータを取得する ---- (*1)
form = cgi.FieldStorage()

# 特定のパラメータを取得して表示 --- (*2)
if "mode" in form:
    print("mode=", form["mode"].value)
else:
    print("mode=空")

# 全てのパラメータを取得して表示 --- (*3)
print("--- all params ---")
for k in form.keys():
    print(k,"=",form.getvalue(k))

