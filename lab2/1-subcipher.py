fi = open("sub_key.txt", "r")

key = fi.readline().rstrip()

dic = dict()

it = ord('A')
for k in key:
	dic[k] = chr(it)
	it += 1

fi = open("sub_ciphertext.txt", "r")
fo = open("solution01.txt", "w")

ciphertext = fi.readline().rstrip()
for c in ciphertext:
	if c == ' ':
		fo.write(c)
	else:
		fo.write(dic[c])
