from Crypto.Cipher import AES

fi = open("aes_weak_ciphertext.hex", "r")
ciphertext = fi.readline().strip()
ciphertext = ciphertext.decode("hex")
fi.close()

iv = "00000000000000000000000000000000".decode("hex")
keybase = "00000000000000000000000000000000000000000000000000000000000000"

for it in range(0, 10):
    key = keybase + "0" + str(it)
    print(key)
    key = key.decode("hex")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(cipher.decrypt(ciphertext))
for it in range(ord("A"), ord("G")):
    key = keybase + "0" + chr(it)
    print(key)
    key = key.decode("hex")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(cipher.decrypt(ciphertext))

for it in range(0, 10):
    key = keybase + "1" + str(it)
    print(key)
    key = key.decode("hex")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(cipher.decrypt(ciphertext))
for it in range(ord("A"), ord("G")):
    key = keybase + "1" + chr(it)
    print(key)
    key = key.decode("hex")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(cipher.decrypt(ciphertext))


print(iv)
print(ciphertext)
