from Crypto.Hash import MD5

m = MD5.new()
m.update('abc')
m.digest()

print m
