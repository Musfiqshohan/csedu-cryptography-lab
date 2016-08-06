from operator import itemgetter
from ngram_score import ngram_score

def decrypt(ctxt, key):
    ret = str()
    for c in ctxt:
        i = ord(c)
        i -= ord('A')
        i -= key
        i = (i+26)%26
        i += ord('A')
        c = chr(i)
        ret += c
    return ret

fi = open("caesar_ciphertext.txt", "r")
ciphertext = fi.readline().strip()
fi.close()

ns = ngram_score("english_quadgrams.txt")

texts = dict()
for k in range(0, 26):
    plaintext = decrypt(ciphertext, k)
    scr = ns.score(plaintext)
    texts[plaintext] = scr
    print(plaintext + " " + str(ns.score(plaintext)))

result = max(texts, key=texts.get)
print("Result: " + result)
