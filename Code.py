import requests
import os

# meminta input dari pengguna
url = input("Masukkan alamat website: ")

# melakukan pemindaian port menggunakan nmap
print("Pemindaian port...")
os.system("nmap " + url)

# melakukan pemindaian keamanan SSL menggunakan sslscan
print("\n")
print("Pemindaian keamanan SSL...")
os.system("sslscan " + url)