def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def isD(k, d, e, mod):
    if k == 0:
        return False
    if d%2 == 0:
        return False
    if (e*d-1)%k != 0:
        return False

    phi = (e*d-1)/k
    b = -(mod-phi+1)
    c = mod
    det = b*b - 4*c
    detr = isqrt(det)
    if detr*detr == det and (-b+detr)%2 == 0:
        return True
    return False


def find_pvtkey(pubkey, mod):
    '''
    Convergents mk/nk is defined by
    mk = qk*(mk-1) + (mk-2)
    nk = qk*(nk-1) + (nk-2)
    m-1 = n-2 = 1, m-2 = n-1 = 0
    qk = kth partial quotient
    '''
    up = pubkey
    down = mod
    m1 = 1
    m2 = 0
    n1 = 0
    n2 = 1

    while True:
        q = up // down
        r = up % down
        up = down
        down = r

        m = q*m1 + m2
        n = q*n1 + n2

        if isD(m, n, pubkey, mod):
            return n
        if r == 0:
            return -1

        m2 = m1
        m1 = m
        n2 = n1
        n1 = n

def bigmod(x, p, mod):
    if p == 0:
        return 1
    elif p%2 == 1:
        return (x*bigmod(x, p-1, mod)) % mod
    else:
        ret = bigmod(x, p/2, mod)
        return (ret*ret)%mod

def decrypt(ctext, pvtkey, mod):
    return bigmod(ctext, pvtkey, mod)

def main():
    ''' Open and read the files '''
    f = open("4.3_ciphertext.hex")
    ctext = f.readline().strip()
    f.close()

    f = open("4.4_public_key.hex")
    pubkey = f.readline().strip()
    f.close()

    f = open("4.5_modulo.hex")
    mod = f.readline().strip()
    f.close()

    ''' Convert the hex strings to int '''
    ctext = int(ctext, 16)
    pubkey = int(pubkey, 16)
    mod = int(mod, 16)

    pvtkey = find_pvtkey(pubkey, mod)
    print("Private key: " + str(pvtkey))

    ptext = decrypt(ctext, pvtkey, mod)
    print("Plain text: " + str(ptext))

if __name__ == "__main__":
    main()
