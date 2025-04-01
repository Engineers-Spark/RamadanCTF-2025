from Crypto.Util.number import *
from secret import FLAG

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
    print("2. Decrypt")
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
            print(f'{n=}\n{e=}')
        elif c == 2:
            c = int(input("Enter the encrypted message: "))
            if decrypt(c, d, n) == bytes_to_long(FLAG):
                print("Not allowed")
            else:
                print("Decrypted message: ", decrypt(c, d, n))
        elif c == 3:
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
