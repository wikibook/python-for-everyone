# 여러 개의 텍스트 파일 중에서 텍스트 파일을 검색하는 스크립트
import sys
import os

# 인수의 개수를 확인한다 ---( 1)
# 키워드가 아무것도 없으면 사용법을 표시한다
if len(sys.argv) <= 1:
    print("[USAGE] findtext (keyword)")
    sys.exit(0) # 프로그램을 끝낸다 ---( 2)

# 명령 프롬프트 인수에서 키워드를 얻는다 --- (*3)
keyword = sys.argv[1]

# 현재 디렉토리 아래에 있는 모든 파일을 처리한다 --- (*4)
for root, dirs, files in os.walk("."):
    for fi in files:
        result = []
        # 텍스트 파일을 읽는다 ---( 5)
        try:
            path = os.path.join(root, fi) 
            with open(path, encoding='utf-8') as f:
                for no, line in enumerate(f):
                    if line.find(keyword) >= 0:
                        line = line.strip()
                        s = "| {0:4}: {1}".format(no+1, line)
                        result.append(s)
        except:
            continue
        # result에 검색 결과가 있으면 결과를 표시한다 --- (*6)
        if len(result) > 0:
            print("+ file: " + fi)
            for li in result:
                print(li)

