import json

# 딕셔너리형 데이터
data = {
  "no": 5,  # 수치
  "code": ("jas", 1, 19), # 튜플
  "scr": "be quick to listen, slow to speak, slow to anger", # 문자열
}

# 파일에 쓴다
filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)

# 파일에서 읽어들인다
with open(filename, "r") as fp:
    r = json.load(fp)
    print("no=", r["no"])
    print("code=", r["code"])
    print("scr=", r["scr"])

