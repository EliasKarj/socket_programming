import socket as soc
import struct

studentID = input("Input student id: ")
last_digit_str = studentID[-1]
last_digit = int(last_digit_str)
n = last_digit + 1

two_last_str = studentID[-2:]
two_last = int(two_last_str)
s = two_last + 1

print("\n" + "-"*30)
print(f"Analyysi tunnukselle: {studentID}")
print("-" * 30)
print(f"Viimeinen numero on {last_digit} -> Ping-määrä (-c) on: {n}")
print(f"Kaksi viimeistä ovat {two_last} -> Paketin koko (-s) on: {s}")
print("-" * 30)

print(f"Suorita tämä komento terminaalissa:")
print(f"ping -c {n} -s {s} 8.8.8.8")
print("-" * 30)
