import socket as sk

try:
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM, sk.IPPROTO_UDP)
except sk.error:
    print("Cannot open socket, quit")
    exit()

while True:
    try:
        m = input("msg:")
        s.sendto(bytearray(m, encoding="ascii"), ("192.168.73.235", 44444))
        try:
            m, addr = s.recvfrom(1000)
            print(m.decode("ascii\n"))
        except sk.error:
            print("something is wrong")
            break
    except KeyboardInterrupt: break

s.close()