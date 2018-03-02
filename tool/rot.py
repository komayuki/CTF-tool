import re

def rot(n, str):
    arr = []
    for s in str:
        x = ord(s)
        if 65 < x & x < 90:
            x = x + n
            if x > 90: x = x - 26

        elif 97 < x & x < 122:
            x = x + n
            if x > 122: x = x - 26

        arr.append(chr(x))

    return "".join(arr)
