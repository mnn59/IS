import nmap

nmScan = nmap.PortScanner()
res = nmScan.scan('89.43.3.0', '21-40')
# print(res)
print(nmScan.command_line())