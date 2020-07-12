import random
from hashlib import *
from Crypto.Cipher import AES 
p='ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327fffffffffffff'

p=int(p,16)

g=2

a=random.randint(1,2*p)%p

A=pow(g,a,p)

b=random.randint(1,2*p)%p

B=pow(g,b,p)

s=pow(B,a,p)

assert(s==pow(A,b,p))

s=str(s)

s=s.encode('utf-8')

s=md5((s)).hexdigest()

cipher=AES.new(s,AES.MODE_ECB)

enc=cipher.encrypt("Here_we_go_again_blocks_are_all_")

print(cipher.decrypt(enc))

'''We get p,g,A and p,g,B pair by interception'''


