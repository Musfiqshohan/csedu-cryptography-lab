class RSA(object):

    def __init__(self):
        p = 11
        q = 13
        self.N = p*q
        r = (p-1)*(q-1)
        self.e = 7
        self.d = self.mulinv(self.e, r)

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def mulinv(self, b, n):
        g, x, _ = self.egcd(b, n)
        if g == 1:
            return x % n

    def encrypt(self, msg):
        c = msg ** self.e
        return c % self.N

    def decrypt(self, msg):
        m = msg ** self.d
        return m % self.N

def main():
    rsa = RSA()

    m = 45
    c = rsa.encrypt(m)
    m = rsa.decrypt(c)
    print(c)
    print(m)

if __name__ == "__main__":
    main()