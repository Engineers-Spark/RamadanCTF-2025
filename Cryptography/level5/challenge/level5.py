from Crypto.Util.number import *
from secret import FLAG
import random

k = 128
B = 2 ** (8 * (k - 1))


def oracle(c , d , n , B):
        return (pow(c, d, n) < B) | random.choice([True, False])

def gen_key():
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse(e, phi)
    return n, e, d

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d , n):
    return pow(c, d, n)

def choices():
    print("1. Encrypt Flag")
    print("2. Check Padding")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    n, e, d = gen_key()
    while True:
        c = choices()
        if c == 1:
            m = bytes_to_long(FLAG)
            c = encrypt(m, e , n)
            print("Encrypted message: ", c)
            print(f'{n=}\n{e=}')
        elif c == 2:
            c = int(input("Enter the encrypted message: "))
            print("oracle: ", oracle(c, d, n, B))
        elif c == 3:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

