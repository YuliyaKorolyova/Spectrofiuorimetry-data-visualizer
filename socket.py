import socket

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)

while True:
    client, addr = sock.accept()
    
