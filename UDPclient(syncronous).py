import socket as sc
import threading

def recv(s):
    while True:
        try:
            msg, addr = s.recvfrom(1024)
            print("\xlb7\xlb[%d;%dH\xlb[31m%s\xlb[0m\xlb8" % (10,40,msg))
        except OSError:
            break
try:
    s = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
except:
    print("Cannot create socket")
    exit()
t = threading.Thread(tarket=recv, args=[s]).start()
while True:
    try:
        msg = input("To server: ")
        s.sendto(bytearray(msg, encoding="ascii"), ("192.168.73.235", 44444))
    except KeyboardInterrupt: break
s.close()