from Crypto.Util.number import *
from secret import FLAG

def gen_key():
    p = getPrime(512)
    q = p
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse(e, phi)
    return n, e, d

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d , n):
    return pow(c, d, n)

def main():
    n, e, d = gen_key()
    with open(f"level3.txt", "w") as f:
        f.write(f"{n=}\n{e=}\n")
        f.write(f"{encrypt(bytes_to_long(FLAG), e, n)}\n")


if __name__ == '__main__':
    main()