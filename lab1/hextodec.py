f = open("in.txt", "r")

def conv(dig):
    if(dig.upper() == 'A'):
        return 10
    if(dig.upper() == 'B'):
        return 11
    if(dig.upper() == 'C'):
        return 12
    if(dig.upper() == 'D'):
        return 13
    if(dig.upper() == 'E'):
        return 14
    if(dig.upper() == 'F'):
        return 15
    return ord(dig) - 48

for line in f:
    dec = 0
    for dig in line:
        if dig == '\n':
            break
        dec = dec * 16
        dec = dec + conv(dig)
    print dec
