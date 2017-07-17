import sys
import os
import fnmatch
import datetime
import math

# 인수를 확인하고 사용법을 표시한다 --- (*1)
if len(sys.argv) <= 1:
    print("[USAGE] findfile [--name][--wild][--desc] name")
    sys.exit(0)

# 옵션의 초깃값 --- (*2)
search_mode = "name"
search_func = lambda target, name : (target == name)
name = ""
desc_mode = False

# 옵션을 해석한다 --- (*3)
for v in sys.argv:
    if v == "--name":
        search_mode = "name"
        search_func = lambda target, name : (target == name)
    elif v == "--wild":
        search_mode = "wild"
        search_func = lambda target, pat : fnmatch.fnmatch(target, pat)
    elif v == "--desc": desc_mode = True
    else:
        name = v

# 옵션을 해석한 결과를 표시한다
print("+ option")
print("| search_mode=", search_mode, name)
print("| desc_mode=", desc_mode)

# 파일을 검색한다 --- (*4)
for root, dirs, files in os.walk("."):
    for fname in files:
        path = os.path.join(root, fname)
        b = search_func(fname, name)
        if b == False: continue
        if desc_mode:
            info = os.stat(path)
            kb = math.ceil(info.st_size / 1024)
            mt = datetime.datetime.fromtimestamp(info.st_mtime)
            s = "{0},{1}KB,{2}".format(path, kb, mt.strftime("%Y-%m-%d"))
            print(s)
        else:
            print(path)


