import socket, threading


def TCP_connect(ip, port_number, output):
    delay = 2
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'open'
    except:
        output[port_number] = ''


def scan_ports(host_ip, start, last):
    threads = []  # To run TCP_connect concurrently
    output = {}  # For printing purposes

    # Spawning threads to scan ports
    for i in range(65000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, output))
        threads.append(t)

    # Starting threads
    for i in range(65000):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(65000):
        threads[i].join()

    # Printing listening ports from small to large
    lst = []
    with open('result_port.txt', 'w') as f:
        for i in range(65000):
            if output[i] == 'open' and int(start) <= i <= int(last):
                item = "Port Open:-->\t{}".format(str(i))
                f.write(item + '\n')
                lst.append(item)
    for litem in lst:
        print(litem)
