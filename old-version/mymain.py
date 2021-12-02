import datetime
import time

import pyfiglet

from myping import ping
from myscanhost import scan_hosts
from myscanport import scan_ports


def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' * row] + ['+'])
    result = h + '\n'"|" + msg + "|"'\n' + h
    print(result)


# TODO: try-except
def main():
    ascii_banner = pyfiglet.figlet_format("MY SCANNER")
    print(ascii_banner)
    try:
        while 1:
            print('Select option: ')
            print('0) ping\n1) scan host\n2) scan port\n3) exit\n#################')
            sel = input()
            menu_dic = {'0': handle_ping, '1': handle_scan_host, '2': handle_scan_port, '3': exit}
            menu_dic[sel]()
    except Exception as e:
        print(e)


def handle_ping():
    url = str(input("Please Enter your IP/Domain: "))
    ping_status = ping(url)
    border_msg(ping_status)


def handle_scan_host():
    address = str(input("Enter the Network Address: "))
    start = str(input("Enter the Starting Number: "))
    last = str(input("Enter the Last Number: "))
    print("Scanning in Progress...")
    start_time = time.time()
    scan_hosts(address, start, last)
    end_time = time.time()
    dt = end_time - start_time
    print("Scanning complete in {}".format(str(datetime.timedelta(seconds=dt))))


def handle_scan_port():
    host = str(input("Enter the remote host IP to scan: "))
    start = str(input("Enter the start port number: "))
    last = str(input("Enter the last port number: "))
    print("*" * 40)
    print("Mohit\'s Scanner is working on {}".format(host))
    print("*" * 40)
    scan_ports(host, start, last)
    # scan_ports(host)


if __name__ == '__main__':
    main()
