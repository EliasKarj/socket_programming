import socket as sc
import threading
import time
import sys

def checksum(packet):
    data = bytearray(packet)
    plen = len(data)
    if plen % 2 == 1:
        plen += 1
        data.append(0)

    sum = 0
    for i in range(0, plen // 2):
        sum += data[2*i] * 256 + data[2*i+1]

    sum = (sum >> 16) + (sum & 0xffff)
    return 0xffff - sum

def send(s):
    for seq in range(1, 4):
        time.sleep(1)
        
        packet = bytearray(b'\x08\x00\x00\x00\x17\x61\x00\x00e2301761')

        packet[6] = seq // 256
        packet[7] = seq % 256
        
        csum = checksum(packet)
        packet[2] = csum // 256
        packet[3] = csum % 256
        
        print("send %s" % (packet))
        s.sendto(packet, (target_ip, 0))

def recv(s):
    while True:
        try:
            d = s.recvfrom(65534)
            if d[1][0] == target_ip:
                packet = d[0][20:]
                print("Recv %s" % (packet))
        except:
            break

try:
    s = sc.socket(sc.AF_INET, sc.SOCK_RAW, sc.IPPROTO_ICMP)
    s.bind(("", 0))
    
    target_ip = input("Address to ping: ")
    
    t1 = threading.Thread(target=recv, args=[s])
    t1.daemon = True
    t1.start()
    
    send(s)
    
    time.sleep(2)
    s.close()
    
except Exception as e:
    print(e)