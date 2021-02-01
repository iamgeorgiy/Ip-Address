import socket
hostname=input("Enter hostname man:->")
IP=socket.gethostbyname(hostname)
print("Ip Address is:->"+IP)