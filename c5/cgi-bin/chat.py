#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

# 브라우저에서 디버깅할 수 있도록 디버그 기능을 유효화한다 --- (*1)
cgitb.enable()

# 전체 로그 설정 --- (*2)
FILE_LOG = "chat-log.txt"

# HTML을 화면에 출력한다 --- (*3)
def print_html(body):
    # 헤더를 출력한다
    print("Content-Type: text/html; charset=utf-8")
    print("")    
    # HTML을 출력한다
    print("""
<html><head><meta charset="utf-8">
<title>채팅</title></head><body>
<h1>채팅</h1>
<div><form>
이름: <input type="text" name="name" size="8">
본문: <input type="text" name="body" size="20">
<input type="submit" value="말하기">
<input type="hidden" name="mode" value="write">
</form></div><hr>
{0}
</body></html>
    """.format(body))

# 화면에 로그를 표시한다 --- (*4)
def mode_read(form):
    # 로그를 읽어들인다
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    print_html(log)

# 임의의 URL로 점프한다 --- (*5)
def jump(url):
    # 헤더를 출력한다
    print("Status: 301 Moved Permanently")
    print("Location: " + url)
    print("")
    # HTML을 출력한다(헤더가 처리를 못했을 때를 대비함)
    print('<html><head>')
    print('<meta http-equiv="refresh" content="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">jump</a></body></html>')

# 메시지를 쓴다 --- (*6)
def mode_write(form):
    # 매개변수를 얻는다
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    # HTML로 변환한다
    name = html.escape(name)
    body = html.escape(body)
    # 파일에 저장한다 --- (*6a)
    with open(FILE_LOG, "a+", encoding='utf-8') as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name,body))
    # 쓰기를 실행한 후에 '새로 고침'한다
    jump('chat.py')

# 메인 처리 --- (*7)
def main():
    # 폼 데이터 값을 얻는다
    form = cgi.FieldStorage()
    # mode 매개변수를 얻는다
    mode = form.getvalue("mode", "read")
    # mode의 값에 맞춰 처리를 변경한다
    if mode == "read": mode_read(form)
    elif mode == "write": mode_write(form)
    else: mode_read(form)

if __name__ == "__main__":  # --- (*8)
    main()


