import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

opiskelijanumero = b"e2301761"
kohde = ("8.8.8.8", 80)
s.sendto(opiskelijanumero, kohde)

print("UDP-paketti lähetetty onnistuneesti!")