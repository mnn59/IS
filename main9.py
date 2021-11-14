import nmap

nm = nmap.PortScanner()
nm.scan('89.43.3.170', '1-500')

for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        list(lport).sort()
        for port in lport:
            port_status = nm[host][proto][port]['state']
            if port_status == 'open':
                print('port : {}\tstate : {}'.format(port, port_status))

