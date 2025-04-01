from Crypto.Util.number import *
from math import gcd
with open('level1.txt') as f:
    data = f.read()

data = data.split('\n\n')
ns = []
es = []
cs = []

for i in data:
    i = i.split('\n')
    n = int(i[0].split(' = ')[1])
    e = int(i[1].split(' = ')[1])
    c = int(i[2].split(' = ')[1])
    ns.append(n)
    es.append(e)
    cs.append(c)


for i in range(len(ns)):
    for j in range(i+1, len(ns)):
        if gcd(ns[i], ns[j]) != 1 and ns[i] != ns[j]:
            p = gcd(ns[i], ns[j])
            q = ns[i] // p
            phi = (p-1)*(q-1)
            d = inverse(es[i], phi)
            m = pow(cs[i], d, ns[i])
            print(long_to_bytes(m))
            exit()