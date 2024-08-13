import requests

url = "http://litctf.org:31779/"

r = requests.get(url)

print(r.text)
