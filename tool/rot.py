import re

def rot(n, str):
    arr = []
    pattern = r"[a-zA-Z]"
    for s in str:
        if re.match(pattern , s):
            s = chr(ord(s) - n)
        arr.append(s)
    return "".join(arr)
