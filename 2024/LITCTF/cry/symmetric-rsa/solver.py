from pwn import *
from math import gcd
from Crypto.Util.number import long_to_bytes as ltb

io = remote("litctf.org", 31783)


def get_ct():
    io.recvuntil(b"CT = ")
    ct = int(io.recvline().strip().decode())

    return ct


def get_result(number):
    io.sendlineafter(b"Plaintext: ", number)
    return get_ct()


ct = get_ct()
n = get_result(b"-1") + 1
c1 = get_result(b"2")
c2 = get_result(b"3")
c3 = get_result(b"5")

io.close()

e = gcd(2 - c1, 3 - c2, 5 - c3)
p = e
q = n // e

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

flag = ltb(pow(ct, d, n)).decode()

print(flag)
