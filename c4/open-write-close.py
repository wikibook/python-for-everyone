# (1) 파일을 연다
a_file = open("test.txt", mode="w", encoding="utf-8")

# (2) 파일에 내용을 쓴다
a_file.write("나는 실패해본 적이 없다.\n")
a_file.write("1만 가지의 방법을 찾아냈을 뿐이다.\n")
a_file.write("- 토마스 에디슨\n")

# (3) 파일을 닫는다
a_file.close()


