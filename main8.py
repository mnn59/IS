# import nmap
#
# nmScan = nmap.PortScanner()
# res = nmScan.scan('89.43.3.0', '21-40')
# # print(res)
# print(nmScan.command_line())

# import platform
#
# print(platform.system())


###########################################################33

# import nmap
# import json
#
# nmScan = nmap.PortScanner()
# # res = nmScan.scan('89.43.3.0', '21-40')
# # print(res)
# # print(nmScan.command_line())
# res2 = nmScan.scan('89.43.3.0', '21-40', arguments='-n -sP -PE -PA21,23,80,3389')
# print(res2)
#
#
# with open('./cred.json', 'a') as cred:
#     json.dump(res2, cred)


#########################################################
import nmap


# 198.116.0.23
# 198.116.0.60-70
def generate_hosts(address, start, last):
    half_address = '.'.join(address.split('.')[:-1])
    return half_address + '.' + start + '-' + last


address = str(input("Enter the Network Address: "))
start = str(input("Enter the Starting Number: "))
last = str(input("Enter the Last Number: "))

# print(generate_hosts(address, start, last))

nm = nmap.PortScanner()
# 198.116.0-255.1-127
nm.scan(hosts=generate_hosts(address, start, last), arguments='-v -sn')
# print(nm.command_line())
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    if status == 'up':
        print('{} --> Live'.format(host))
