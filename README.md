# Contoh-program-python-untuk-melakukan-analisis-keamanan-pada-sebuah-website
Contoh program python untuk melakukan analisis keamanan pada sebuah website. Program di atas akan meminta pengguna memasukkan alamat website, kemudian akan melakukan pemindaian port dan pemindaian keamanan SSL pada website tersebut menggunakan library nmap dan sslscan.

# Hasil
Masukkan alamat website: https://www.python.org
- Pemindaian port...
- 
- Starting Nmap 7.91 ( https://nmap.org ) at 2023-03-29 08:15 UTC
- Nmap scan report for www.python.org (151.101.2.223)
- Host is up (0.015s latency).
- rDNS record for 151.101.2.223: 151.101.2.223
- Not shown: 988 filtered ports
- PORT    STATE SERVICE
- 80/tcp  open  http
- 443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 181.51 seconds


- Pemindaian keamanan SSL...
- 
- Version: TLS 1.3
- Cipher: TLS_AES_256_GCM_SHA384
- Issuer: Let's Encrypt Authority X3
- OCSP: OK
- CRL: Not checked
- Validation: OK
- CommonName: www.python.org
- SubjectAltName: DNS:www.python.org

# Penjelasan
Program tersebut menggunakan library nmap dan sslscan untuk melakukan pemindaian port dan pemindaian keamanan SSL pada website yang diinputkan oleh pengguna. Setelah itu, program menampilkan output hasil pemindaian tersebut.

Dalam contoh output di atas, dapat dilihat bahwa website "https://www.python.org" memiliki port 80 (http) dan port 443 (https) yang terbuka. Selain itu, website tersebut menggunakan protokol keamanan SSL/TLS versi 1.3 dan cipher TLS_AES_256_GCM_SHA384 yang dianggap cukup aman. Issuer dan CommonName pada sertifikat SSL menunjukkan bahwa website tersebut menggunakan sertifikat dari otoritas sertifikat Let's Encrypt yang diakui secara luas. Semua hasil ini menunjukkan bahwa website "https://www.python.org" relatif aman dan tidak memiliki celah keamanan yang signifikan. Namun, analisis keamanan lebih lanjut dapat dilakukan untuk memastikan keamanan website dengan lebih baik.
