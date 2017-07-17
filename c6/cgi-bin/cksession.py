#!/usr/bin/env python3
# 쿠키를 사용한 세션

from http import cookies
import os, json
import datetime, random, hashlib

class CookieSession:
    """ 쿠키를 사용한 세션 클래스 """
    
    SESSION_ID = "CookieSessionId"
    # 세션 데이터를 저장할 곳을 지정한다 --- (*1) 
    SESSION_DIR = os.path.dirname(
        os.path.abspath(__file__)) + "/SESSION"

    def __init__(self):
        # 세션 데이터를 저장한 곳의 경로를 확인한다 --- (*2)
        if not os.path.exists(self.SESSION_DIR):
            os.mkdir(self.SESSION_DIR)

        # 쿠키에서 세션ID를 가져온다 --- (*3)
        rc = os.environ.get('HTTP_COOKIE', '')
        self.cookie = cookies.SimpleCookie(rc)
        if self.SESSION_ID in self.cookie:
            self.sid = self.cookie[self.SESSION_ID].value
        else:
            # 처음 방문하는 것이라면 세션ID를 생성한다
            self.sid = self.gen_sid()

        # 저장돼 있는 데이터를 읽어들인다 --- (*4)
        self.modified = False
        self.values = {}
        path = self.SESSION_DIR + "/" + self.sid
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                a_json = f.read()
                # JSON 형식의 데이터를 복원한다
                self.values = json.loads(a_json)

    def gen_sid(self):
        """ 세션ID를 생성한다 """ # --- (*5)
        token = ":#sa$2jAiN"
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        rnd = random.randint(0, 100000)
        key = (token + now + str(rnd)).encode('utf-8')
        sid = hashlib.sha256(key).hexdigest()
        return sid

    def output(self):
        """ 쿠키 헤더 """ # --- (*6)
        self.cookie[self.SESSION_ID] = self.sid
        self.save_data()
        return self.cookie.output()

    def save_data(self):
        """ 세션 데이터를 파일에 출력한다 """
        if not self.modified: return
        path = self.SESSION_DIR + "/" + self.sid
        # JSON 형식으로 변환해서 저장한다
        a_json = json.dumps(self.values)
        with open(path, "w", encoding="utf-8") as f:
            f.write(a_json)

    # 첨자 접속을 위한 특수 메서드를 정의한다 --- (*7)
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.modified = True
        self.values[key] = value

    def __contains__(self, key):
        return key in self.values

    def clear(self):
        self.values = {}

if __name__ == "__main__":
    # 실행 테스트(방문 카운터)
    ck = CookieSession()
    counter = 1
    if "counter" in ck:
        counter = int(ck["counter"]) + 1
    ck["counter"] = counter
    print("Content-Type: text/html")
    print(ck.output())
    print("")
    print("counter=", counter)
