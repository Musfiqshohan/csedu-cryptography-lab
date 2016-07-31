from Crypto.Cipher import AES

fi = open("aes_key.hex", "r")
key = fi.readline().rstrip()
key = key.decode("hex")
fi.close()

fi = open("aes_iv.hex", "r")
iv = fi.readline().rstrip()
iv = iv.decode("hex")
fi.close()

fi = open("aes_ciphertext.hex", "r")
ciphertext = fi.readline().rstrip()
ciphertext = ciphertext.decode("hex")
fi.close()

cipher = AES.new(key, AES.MODE_CBC, iv)

fo = open("solution02.txt", "w")
fo.write(cipher.decrypt(ciphertext))
fo.close()
