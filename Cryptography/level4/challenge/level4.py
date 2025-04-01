from Crypto.Util.number import *
from secret import FLAG


def nextprime(p):
    while True:
        p += 1
        if isPrime(p):
            return p

def gen_key():
    p = getPrime(512)
    q = nextprime(p)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse(e, phi)
    return n, e, d

def encrypt(m, e, n):
    return pow(m, e, n)


def choices():
    print("1. Encrypt Flag")
    print("2. Enceypt Message")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    n, e, d = gen_key()
    while True:
        c = choices()
        if c == 1:
            m = bytes_to_long(FLAG)
            print("Encrypted message: ", encrypt(m, e , n))
        elif c == 2:
            m = bytes_to_long(str(input("Enter the message: ")).encode())
            print("Encrypted message: ", encrypt(m, e , n))
        elif c == 3:
            break
        else:
            print("Invalid choice")
        


if __name__ == '__main__':
    main()
