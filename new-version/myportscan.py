import nmap


def generate_port(start, last):
    return start + '-' + last


def scan_ports(host, start, last):
    nm = nmap.PortScanner()
    nm.scan(host, generate_port(start, last))
    # print(nm.command_line())
    with open('result_port.txt', 'w') as f:
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            list(lport).sort()
            for port in lport:
                port_status = nm[host][proto][port]['state']
                if port_status == 'open':
                    item = "Port Open:-->\t{}".format(str(port))
                    f.write(item + '\n')
                    print(item)
