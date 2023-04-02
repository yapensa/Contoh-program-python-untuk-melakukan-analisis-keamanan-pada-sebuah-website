import requests

# Meminta input dari pengguna berupa URL website yang akan dianalisa
url = input("Masukkan URL website yang akan dianalisa: ")

# Mengirimkan permintaan GET ke website dan mengambil response
response = requests.get(url)

# Mengecek apakah website menggunakan HTTPS
if not response.url.startswith('https'):
    print("Website tidak menggunakan HTTPS!")
else:
    print("Website menggunakan HTTPS.")

# Mengecek apakah website memiliki proteksi terhadap serangan XSS
xss_payload = '<script>alert("XSS Vulnerability Found!")</script>'
xss_response = requests.get(url + xss_payload)
if xss_payload in xss_response.text:
    print("Website rentan terhadap serangan XSS!")
else:
    print("Website tidak rentan terhadap serangan XSS.")

# Mengecek apakah website memiliki proteksi terhadap serangan SQL Injection
sql_payload = "'; DROP TABLE users; --"
sql_query = f"SELECT * FROM users WHERE username = '{sql_payload}'"
sql_response = requests.get(url + "/search?query=" + sql_query)
if "Error executing SQL query" in sql_response.text:
    print("Website rentan terhadap serangan SQL Injection!")
else:
    print("Website tidak rentan terhadap serangan SQL Injection.")

# Mengecek apakah website memiliki proteksi terhadap serangan CSRF
csrf_payload = {
    "username": "hacker",
    "password": "123456",
    "submit": "Login"
}
csrf_response = requests.post(url + "/login", data=csrf_payload)
if "Welcome, hacker!" in csrf_response.text:
    print("Website rentan terhadap serangan CSRF!")
else:
    print("Website tidak rentan terhadap serangan CSRF.")
