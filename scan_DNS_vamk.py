import socket as soc
import struct

s = input("Enter the subnet (x.y.z.t/n): ").split("/")
subnetID = soc.inet_aton(s[0])
mask_len = 32 -int(s[1])
subnetSize = 2**mask_len
first = int.from_bytes(subnetID)
for i in range(1, subnetSize):
        try:
                addr = struct.pack("!I", first + i)
                print(soc.gethostbyaddr(soc.inet_ntoa(addr)))
        except soc.error:
                print("Adress is not active")