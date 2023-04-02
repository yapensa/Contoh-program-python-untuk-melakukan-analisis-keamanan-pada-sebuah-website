import requests
from bs4 import BeautifulSoup

# Meminta input dari pengguna berupa URL website yang akan dianalisa
url = input("Masukkan URL website yang akan dianalisa: ")

# Menggunakan requests untuk mengirimkan permintaan GET ke website
response = requests.get(url)

# Mengambil status code dari response
status_code = response.status_code

# Menampilkan status code dan pesan sesuai dengan kondisi status code
if status_code == 200:
    print("Status Code: 200 OK")
    print("Website berhasil diakses.")
else:
    print("Status Code:", status_code)
    print("Website tidak dapat diakses.")

# Mengambil headers dari response
headers = response.headers

# Menampilkan headers
print("\nHeaders:")
print(headers)

# Membuat objek BeautifulSoup dari response content
soup = BeautifulSoup(response.content, 'html.parser')

# Menampilkan judul website
print("\nJudul website:")
print(soup.title.string)

# Mencari tautan (links) yang ada pada website
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
print("\nTautan (links) yang ditemukan:")
print(links)

# Menampilkan isi (content) website
print("\nIsi (content) website:")
print(soup.get_text())
