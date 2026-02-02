import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

studentID = input("Opiskelija numero: ")
target = ("8.8.8.8", 80)

s.sendto(studentID.encode('utf-8'), target)
print("Paketti lähetetty.")
s.close()