import pymd5

key = "SECRET"
query = "user=admin&command1=ListFiles&command2=NoOp"
h = pymd5.md5()
h.update(key+query)
token = h.hexdigest()
tokenbak = token
query = "token=" + token + "&" + query

''' Read the new command '''
fi = open("3.3_command3.txt")
comm3 = fi.readline().strip()
fi.close()

''' Extract token (hash) and message from the query '''
token = query[query.index("=")+1:query.index("&")]
msg = query[query.index("&")+1:]

''' Compute the padding of current message '''
msglen = len(msg)
for keylen in range(0, 10):
    pad = pymd5.padding((keylen+msglen)*8)
    padhex = pad.encode("hex")

    ''' Setup the md5 hash function '''
    padlen = len(pad)
    cnt = (keylen + msglen + padlen) * 8
    h = pymd5.md5(state=token.decode("hex"), count=cnt)
    h.update(comm3)

    ''' Get the new token and create new query '''
    newtoken = h.hexdigest()
    newquery = query.replace(token, newtoken)
    newquery += pad
    newquery += comm3

    ''' Verify '''
    h = pymd5.md5()
    msg = newquery[newquery.index("&")+1:]
    h.update(key + msg)
    if h.hexdigest() == newtoken:
        print("Verified by key length: " + str(keylen))
