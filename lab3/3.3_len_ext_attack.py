import pymd5

''' Read query '''
fi = open("3.3_query.txt", "r")
query = fi.readline().strip()
fi.close()

''' Read the new command '''
fi = open("3.3_command3.txt")
comm3 = fi.readline().strip()
fi.close()

''' Extract token (hash) and message from the query '''
token = query[query.index("=")+1:query.index("&")]
msg = query[query.index("&")+1:]

''' Compute the padding of current message '''
keylen = 8
msglen = len(msg)
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

for i in range(0, len(padhex), 2):
    newquery += "%5Cx" + padhex[i:i+2]
newquery += comm3

''' Write the query '''
fo = open("solution33.txt", "w")
fo.write(newquery)
fo.close()
