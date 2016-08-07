fi = open("3.1_sha_diff.txt", "r")
h1 = fi.readline().strip()
h2 = fi.readline().strip()
fi.close()

hlen = 256
h1 = bin(int(h1, 16))[2:].zfill(hlen)
h2 = bin(int(h2, 16))[2:].zfill(hlen)

cnt = 0
for it in range(0, hlen):
    if h1[it] != h2[it]:
        cnt += 1

fo = open("solution31.hex", "w")
fo.write(hex(cnt)[2:])
fo.close()
