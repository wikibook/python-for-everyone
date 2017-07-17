#!/usr/bin/env python3

import os, cgi, cgitb, html
import cksession # 자작 세션 모듈
import datetime

class SecBoard:
    """ 비밀 메시지 게시판을 구현한 클래스 """

    # 사용자 이름과 암호 --- (*1)
    USERS = { "taro":"aaa", "jiro":"bbb" }
    # 메시지 파일
    FILE_MSG = "sec-msg.bin"

    def __init__(self): # --- (*2)
        self.form = cgi.FieldStorage()
        self.session = cksession.CookieSession()
        self.check_mode()

    def check_mode(self): # --- (*3)
        mode = self.form.getvalue("mode", "login")
        if mode == "login"      : self.mode_login()
        elif mode == "trylogin" : self.mode_trylogin()
        elif mode == "logout"   : self.mode_logout()
        elif mode == "sec"      : self.mode_sec()
        elif mode == "secedit"  : self.mode_secedit()
        else: self.mode_login()

    def print_html(self, title, html, headers = []):
        """ 헤더와 HTML을 출력한다 """ # --- (*4)
        print("Content-Type: text/html; charset=utf-8")
        for hd in headers: print(hd)
        print("")
        print("""
        <html><head><meta charset="utf-8">
        <title>{0}</title></head><body>
        <h2>{0}</h2><div>{1}</div></body></html>
        """.format(title, html))

    def show_error(self, msg):
        """ 오류를 표시한다 """
        self.print_html("오류", """
        <div style="color:red">{0}</div>
        """.format(msg))

    def mode_login(self):
        """ 로그인 화면을 표시한다 """ # --- (*5)
        self.print_html("회원 전용 로그인", """
        <form method="POST">
        사용자 이름: <input type="text" name="user" size="8"><br>
        암호: <input type="password" name="pw" size="8">
        <input type="submit" value="로그인">
        <input type="hidden" name="mode" value="trylogin">
        </form>
        """)

    def mode_trylogin(self):
        """ 로그인할 수 있는지 검사한다 """ # --- (*6)
        # 폼 데이터에서 로그인 정보를 가져온다
        user = self.form.getvalue("user", "")
        pw   = self.form.getvalue("pw", "")
        # 로그인할 수 있는지 조사한다
        if not (user in self.USERS):
            self.show_error("사용자가 존재하지 않습니다.")
            return
        if self.USERS[user] != pw:
            self.show_error("암호가 다릅니다.")
            return
        # 로그인에 성공했다는 것을 알린다
        now = datetime.datetime.now()
        self.session["login"] = now.timestamp()
        headers = [self.session.output()]
        self.print_html("로그인 성공", """
        <a href="sec-board.py?mode=sec">회원 전용 게시판을 본다</a>
        """, headers)

    def mode_logout(self):
        """ 로그아웃한다 """ # --- (*7)
        self.session['login'] = 0
        self.print_html('로그아웃', """
        <a href="sec-board.py">로그아웃했습니다.</a>
        """, [self.session.output()])
    
    def is_login(self):
        """ 로그인한 상태인지 판정한다 """ # --- (*8)
        if "login" in self.session:
            if self.session['login'] > 0:
                return True
        return False

    def mode_sec(self):
        """ 비밀 메시지를 표시한다 """ # --- (*9)
        if not self.is_login():
            self.show_error('로그인해야 합니다')
            return
        # 비밀 메시지를 읽어들인다
        msg = "여기에 비밀 메시지를 써주세요."
        if os.path.exists(self.FILE_MSG):
            with open(self.FILE_MSG, "r", encoding="utf-8") as f:
                msg = f.read()
        msg = html.escape(msg)
        self.print_html("비밀 메시지", """
        <form method="POST" action="sec-board.py">
        <textarea name="msg" rows="5" cols="80">{0}</textarea>
        <br><input type="submit" value="변경">
        <input type="hidden" name="mode" value="secedit"></form>
        <hr><a href="sec-board.py?mode=logout">→로그 아웃</a>
        """.format(msg))

    def mode_secedit(self):
        """ 비밀 메시지를 편집한다 """ # --- (*10)
        if not self.is_login():
            self.show_error("로그인해야 이용할 수 있습니다.", "")
            return
        # 비밀 메시지를 저장한다
        msg = self.form.getvalue("msg", "")
        with open(self.FILE_MSG, "w", encoding="utf-8") as f:
            f.write(msg)
        # 변경했다는 사실을 알림
        self.print_html("변경했습니다.", """
        <a href="sec-board.py?mode=sec">내용을 확인한다</a>
        """)

if __name__ == "__main__":
    cgitb.enable()
    app = SecBoard()
