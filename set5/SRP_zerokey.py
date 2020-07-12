
from Crypto.Util.number import *
from gmpy2 import *
import random
from hashlib import *
import hmac
N=pow(2,521)-1
g=2
k=3
I="Th3_w34sly_br0th3r5@gmail.com"
P="Mischief_managed"

"Server side"
salt=random.randint(100,32134)
xH=str(salt)+P
xH=xH.encode('utf-8')
xH=sha256(xH).hexdigest()
x=int(xH,16)
v=pow(g,x,N)

"Client side"

a=random.randint(1,N-1)%N

A=random.choice([0,N,2*N])
"Evil Client GEnerate A%N==0"
"Client sends A and I to the server"

"Server sends salt"


b=random.randint(1,2*N)%N
B=k*v+pow(g,b,N)


uH=str(A)+str(B)
uH=uH.encode('utf-8')
uH=sha256(uH).hexdigest()
u=int(uH,16)
"This is done at both Client and server side"

S_Client=0
"Calculated using A =0"

K_Client=str(S_Client).encode('utf-8')
K_Client=sha256(K_Client).hexdigest()
K_Client=int(K_Client,16)

"Server side"
S_Server=pow(A*pow(v,u,N),b,N)
K_Server=str(S_Server).encode('utf-8')
K_Server=sha256(K_Server).hexdigest()
K_Server=int(K_Server,16)
salt=str(salt).encode('utf-8')
hmac_server=(hmac.new(long_to_bytes(K_Server), salt,sha256).hexdigest())
"Client sends to Server"


"Client validates"
hmac_Client=(hmac.new(long_to_bytes(K_Client), salt,sha256).hexdigest()) 
if(hmac_server==hmac_Client):
    print("OK")

