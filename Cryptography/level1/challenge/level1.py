from Crypto.Util.number import *
from secret import FLAG
import random


def gen_prime():
    p = getPrime(512)
    return p

def gen_key(primes):
    p = random.choice(primes)
    q = random.choice(primes)
    n = p * q
    e = 0x10001
    return (n, e)

def encrypt_flag(n , e, flag):
    m = bytes_to_long(flag)
    c = pow(m, e, n)
    return c

def main():
    primes = [gen_prime() for _ in range(10)]
    with open(f"level1.txt", "w") as f:
        for i in range(50):
            n, e = gen_key(primes)
            c = encrypt_flag(n, e, FLAG)
            f.write(f"n = {n}\n")
            f.write(f"e = {e}\n")
            f.write(f"c = {c}\n\n")

if __name__ == '__main__':
    main()