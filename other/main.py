import csv
import os
import socket
import struct
from itertools import product

import joblib


def ping(url):
    response = os.system("ping -c 1 " + url)
    if response == 0:
        ping_status = "Network Active"
    else:
        ping_status = "Network Error"
    return ping_status


def scan_ip_range(url):
    pass


def main():
    pass
    # print("Please Enter your IP/Domain: ")
    # url = str(input())
    # ping_status = ping(url)
    # print(ping_status)

    # import ipaddress
    # for ip in ipaddress.IPv4Network('192.168.1.0/24'):
    #     print(ip)

    # import socket, struct


start = '89.43.0.0'
# end = '89.43.7.255'
end = '89.43.0.255'
start = struct.unpack('>I', socket.inet_aton(start))[0]
end = struct.unpack('>I', socket.inet_aton(end))[0]
lst_ips = [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

print(len(lst_ips))


def func(url):
    with open('results.csv', mode='a') as url_file:
        employee_writer = csv.writer(url_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        response = ping(url)
        if response == 'Network Error':
            print("time out! there is no such site")
            employee_writer.writerow([url, 'fail'])
        else:
            print("success! there is a site with this url ({})".format(url))
            employee_writer.writerow([url, 'success'])


# if __name__ == '__main__':
#     main()


f = open("results.csv", "w")
f.truncate()
f.close()

# with joblib.Parallel(n_jobs=2) as parallel:
#     accumulator = 0.
#     n_iter = 0
#     while accumulator < 1000:
#         results = parallel(joblib.delayed(func)(url)
#                            for url in lst_ips)
#         if results is not None:
#             accumulator += sum(results)  # synchronization barrier
#             n_iter += 1

# joblib.Parallel(n_jobs=2)(joblib.delayed(func)(url) for url in lst_ips)

# [func(url) for url in lst_ips]


