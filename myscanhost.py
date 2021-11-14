import socket
import struct
from myping import ping, ping2


def scan_hosts(address, start, last):
    address_start = '.'.join(address.split('.')[:-1]) + '.' + start
    address_end = '.'.join(address.split('.')[:-1]) + '.' + str(int(last) + 1)
    address_start = struct.unpack('>I', socket.inet_aton(address_start))[0]
    # print(address_start)
    address_end = struct.unpack('>I', socket.inet_aton(address_end))[0]
    # print(address_end)
    lst_ips = [socket.inet_ntoa(struct.pack('>I', i)) for i in range(address_start, address_end)]
    lst = []
    with open('result_host.txt', 'w') as f:
        for ip in lst_ips:
            if ping2(ip) == 0:  # i should install python-nmap not just check ip
                item = ip + ' --> ' + 'Live'
                f.write(item + '\n')
                lst.append(item)
    for litem in lst:
        print(litem)
