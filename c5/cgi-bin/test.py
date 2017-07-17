#!/usr/bin/env python3

import sys
import cgitb

# ブラウザでのデバッグを有効にする
cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print("")
print(sys.stdout)

