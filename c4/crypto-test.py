from Crypto.Cipher import AES # ---- (*1)
import base64

# 암호화하려는 데이터와 암호를 지정한다 ---(*2)
message = "내가 받고 싶은 것을 남에게도 해준다"
password = "xxxxxxxxxx" # 암호를 아무거나 지정한다
iv = "L3f4mlTJtCIPV9af" # 초기화 벡터(16문자로 아무거나 값을 지정)
mode = AES.MODE_CBC # 암호화 모드를 지정한다

# 특정 길이의 배수로 만들기 위해 공백으로 데이터를 채우는 함수 --- (*3)
def mkpad(s, size):
    s = s.encode("utf-8") # UTF-8 문자열을 바이트 배열로 변환한다
    pad = b' ' * (size - len(s) % size)
    return s + pad

# 암호화한다 --- (*4)
def encrypt(password, data):
    # 특정 길이로 조절한다
    password = mkpad(password, 16) # 16의 배수로 맞춘다
    data = mkpad(data, 16)         # 바이트 배열로 변환하고 16의 배수로 맞춘다
    password = password[:16]       # 정확히 16문자로 맞춘다
    # 암호화한다
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")

# 복호화한다 --- (*5)
def decrypt(password, encdata):
    # 암호의 문자 개수를 조절
    password = mkpad(password, 16) # 16의 배수로 맞춘다
    password = password[:16]       # 정확히 16문자로 맞춘다
    # 복호화
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")


# 암호화한다
enc = encrypt(password, message)
# 복호화한다
dec = decrypt(password, enc)

# 결과를 표시한다
print("암호화:", enc)
print("복호화:", dec)



