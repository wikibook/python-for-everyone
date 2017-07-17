# 데코레이터를 정의한다
def wrap_html(func):
    def wrapper(*args, **kwargs):
        s = "<html>"
        s += func(*args, **kwargs)
        s += "</html>"
        return s
    return wrapper

def wrap_body(func):
    def wrapper(*args, **kwargs):
        s = "<body>"
        s += func(*args, *kwargs)
        s += "</body>"
        return s
    return wrapper

# 데코레이터를 사용해본다
@wrap_html
@wrap_body
def show_html(text):
    return text

print(show_html("데코레이터 테스트"))
