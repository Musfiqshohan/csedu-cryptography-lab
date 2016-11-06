def encrypt(s, key):
    key -= 1
    ret = str()
    for c in s:
        i = ord(c)
        i -= ord('A')
        i += key
        i %= 26
        i += ord('A')
        c = chr(i)
        ret += c

    return ret

print encrypt("HELLOZ", 3)
