#!/usr/bin/env python3
# 방문 회수를 쿠키로 카운트한다

import os
import cgi
from http import cookies
import datetime

# Cookie를 얻는다
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
cnt = 1
if 'counter' in cookie:
    cnt = int(cookie['counter'].value) + 1

# Cookie를 설정한다
cookie['counter'] = cnt
#  유효기간을 지정한다
expires = datetime.datetime.now() + datetime.timedelta(days=90)
cookie['counter']['expires'] = expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

# 헤더를 출력한다
print("Content-Type: text/html; charset=utf-8")
print(cookie.output())
print("")
print("방문 회수=", cnt)
