import sys
import dpkt

f = open(sys.argv[1])
pcap = dpkt.pcap.Reader(f)

ips = list()
snd = dict()
rcv = dict()

cnt = 0
for ts, buf in pcap:
    eth = None
    try:
        eth = dpkt.ethernet.Ethernet(buf)
    except Exception:
        continue
    if eth.type != dpkt.ethernet.ETH_TYPE_IP:
        continue
    ip = eth.data
    if ip.p != dpkt.ip.IP_PROTO_TCP:
        continue
    tcp = ip.data

    # Process the tcp packet
    if (tcp.flags & dpkt.tcp.TH_SYN) != 0:
        # Count for sending a syn packet
        host = ip.src
        if host not in snd:
            snd[host] = 1
            if host not in ips:
                ips.append(host)
                print(host.encode('hex'))
        else:
            snd[host] += 1
    if (tcp.flags & (dpkt.tcp.TH_SYN | dpkt.tcp.TH_ACK)) != 0:
        # Count for receiving a syn+ack packet
        host = ip.dst
        if host not in rcv:
            rcv[host] = 1
            if host not in ips:
                ips.append(host)
                print(host.encode('hex'))
        else:
            rcv[host] += 1

fh = open('8.2.txt', 'w')

for ip in ips:
    if ip in snd and ip in rcv:
        #if snd[ip] > 3*rcv[ip]:
        ipstr = ip.encode('hex')
        fh.write(str(int(ipstr[0:2], 16)))
        fh.write('.')
        fh.write(str(int(ipstr[2:4], 16)))
        fh.write('.')
        fh.write(str(int(ipstr[4:6], 16)))
        fh.write('.')
        fh.write(str(int(ipstr[6:8], 16)))
        fh.write(' ' + str(snd[ip]) + ' ' + str(rcv[ip]) + '\n')
