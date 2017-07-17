#!/usr/bin/env python3

### わざとエラーを出すプログラム ###

import cgi
import cgitb
cgitb.enable()

# ヘッダの表示
print("Content-Type: text/html; charset=utf-8")
print("") # 空行

form = cgi.FieldStorage()

print("--- all params ---")
for k in form.items():
    print(k,"=",form.getvalue(k))

