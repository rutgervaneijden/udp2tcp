import socket

UDP_host = '127.0.0.1'
UDP_port = 8003

TCP_host = '127.0.0.1'
TCP_port = 2000

sentences = ['RSA','THS','VDM','VTG']

def filter(data):
    if data[3:6].decode() in sentences:
        TCP.sendall(data)
        print(data)

UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP.bind((UDP_host,UDP_port))

TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP.settimeout(30)
TCP.connect((TCP_host,TCP_port))

while True:
    data,addr = UDP.recvfrom(1024)
    filter(data)