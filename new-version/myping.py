import os
import subprocess
import platform

# ping -c 1 "url" in linux
# ping -n 1 "url" in windows

# 0 : active
# 1 : inactive

oper = platform.system()


def ping(url):
    response = 1
    if oper == 'Windows':
        response = os.system("ping -n 1 " + url)
    elif oper == 'Linux':
        response = os.system("ping -c 1 " + url)
    if response == 0:
        ping_status = "Network Active"
    else:
        ping_status = "Network Error"
    save_ping_result(url, ping_status)
    return ping_status


def ping2(url):
    option = '-c'
    if oper == 'Windows':
        option = '-n'
    elif oper == 'Linux':
        option = '-c'
    process = subprocess.Popen(['ping', option, '1', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    return returncode


def save_ping_result(url, ping_status):
    with open('result_ping.txt', 'w') as f:
        f.write(url + ', ' + ping_status)
