import nmap


# 198.116.0.60-70
def generate_hosts(address, start, last):
    half_address = '.'.join(address.split('.')[:-1])
    return half_address + '.' + start + '-' + last


def scan_hosts(address, start, last):
    nm = nmap.PortScanner()
    nm.scan(hosts=generate_hosts(address, start, last), arguments='-v -sn')
    # print(nm.command_line())
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    with open('result_host.txt', 'w') as f:
        for host, status in hosts_list:
            if status == 'up':
                item = '{} --> Live'.format(host)
                f.write(item + '\n')
                print(item)