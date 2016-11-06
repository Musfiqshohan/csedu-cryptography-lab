def wha(txt):
    outhash = 0
    mask = 0x3FFFFFFF
    # 00111111 11111111 11111111 11111111

    # 11001100 00000000 00000000 00000000
    # 00000000 00110011 00000000 00000000
    # 00000000 00000000 10101010 00000000
    # 00000000 00000000 00000000 01010101

    # 11001100 00110011 10101010 01010101

    for c in txt:
        b = ord(c)
        val =  ((b ^ 0xCC) << 24)
        val |= ((b ^ 0x33) << 16)
        val |= ((b ^ 0xAA) << 8)
        val |= (b ^ 0x55)
        outhash = (outhash & mask) + (val & mask)
    return outhash

fi = open("3.2_input_string.txt", "r")
txt = fi.readline().strip()
fi.close()

print(hex(wha(txt)))
