# import socket
#
#
# def func(host, port):
#     a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     location = (host, port)
#     result_of_check = a_socket.connect_ex(location)
#     if result_of_check == 0:
#         print("Port {} is open".format(port))
#
#
# ip = '89.43.3.170'
# [func(ip, i) for i in range(1, 501)]




# print("*" * 23)


# import logging
#
# from scapy.layers.inet import IP, TCP
#
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# from scapy.all import *
#
# dst_ip = "89.43.3.170"
# src_port = RandShort()
# dst_port = 21
#
# tcp_connect_scan_resp = sr1(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=10)
# if str(type(tcp_connect_scan_resp)) == "<type ‘NoneType’>":
#     print("Closed")
# elif tcp_connect_scan_resp.haslayer(TCP):
#     if tcp_connect_scan_resp.getlayer(TCP).flags == 0x12:
#         send_rst = sr(IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="AR"), timeout=10)
#         print("Open")
#     elif tcp_connect_scan_resp.getlayer(TCP).flags == 0x14:
#         print("Closed")


# for i in range(1,13)