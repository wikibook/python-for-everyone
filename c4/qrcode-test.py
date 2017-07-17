# 패키지를 import한다
import qrcode
# QR 코드 생성
img = qrcode.make("http://www.wikibook.co.kr/")
# 파일에 저장한다
img.save("qrcode-test.png")

