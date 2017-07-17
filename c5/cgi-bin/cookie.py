#!/usr/bin/env python3
# クッキーで訪問回数のカウントアップ

import os
import cgi
from http import cookies
import datetime

# Cookieの取得
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
cnt = 1
if 'counter' in cookie:
    cnt = int(cookie['counter'].value) + 1

# Cookieの設定
cookie['counter'] = cnt
#  有効期限の指定
expires = datetime.datetime.now() + datetime.timedelta(days=90)
cookie['counter']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

# ヘッダを出力する
print("Content-Type: text/html; charset=utf-8")
print(cookie.output())
print("")
print("訪問回数=", cnt)


