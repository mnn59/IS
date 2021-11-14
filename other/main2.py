# ping ips of a list and then create a dictionary for ip and status
import os
import ctypes, sys


def ping(url):
    ping_status = os.system('ping -c 1 ' + url)
    if ping_status == 0:
        print("Active")
    else:
        print("Inactive")
    # return ping_status


# 89.43.0.1 -> 0 Active
# 89.43.0.1 -> 1 DisActive
# print(ping('89.43.0.3'))
print(ping('89.43.0.1'))