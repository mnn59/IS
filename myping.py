import os
import subprocess


# ping -c 1 "url" in linux
# ping -n 1 "url" in windows

# 0 : active
# 1 : inactive
def ping(url):
    response = os.system("ping -n 1 " + url)
    if response == 0:
        ping_status = "Network Active"
    else:
        ping_status = "Network Error"
    save_ping_result(url, ping_status)
    return ping_status


def ping2(url):
    process = subprocess.Popen(['ping', '-n', '1', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    return returncode


def save_ping_result(url, ping_status):
    with open('result_ping.txt', 'w') as f:
        f.write(url + ', ' + ping_status)
