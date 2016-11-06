from Crypto.PublicKey import RSA

def main():
    key = open("key", "r").read()
    keypub = open("key.pub", "r").read()
    rsapri = RSA.importKey(key)
    rsapub = RSA.importKey(keypub)

    m = "hello world"
    c = rsapub.encrypt(m, "")[0]
    print(c.encode("hex"))
    p = rsapri.decrypt(c)
    print(p)

if __name__ == "__main__":
    main()