import random
from Crypto.Util.number import *
from gmpy2 import *

P="4ft3r_411_th15_t1m3?"
e=65537
P=bytes_to_long(P.encode('ascii'))
p=getPrime(1024)
q=getPrime(1024)        

n=p*q

phi=(p-1)*(q-1)

C=pow(P,e,n)


d=invert(e,phi)

S=23534653453

C_2=(pow(S,e,n)*C)%n

P_2=pow(C_2,d,n)

P_2=(P_2//S)%n

print(long_to_bytes(P_2))
print(P==P_2)
