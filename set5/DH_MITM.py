
import random
from Crypto.Util import number
alpha=50
p=number.getPrime(2048)
a=random.getrandbits(16)
b=random.getrandbits(16)
o1=random.getrandbits(16)
o2=random.getrandbits(16)
A=pow(alpha,a,p)
B=pow(alpha,b,p)
O1=pow(alpha,o1,p)
O2=pow(alpha,o2,p)
KAO=KAB=pow(O2,a,p)   #key sent to A by O which A thinks is frm B
KBO=KBA=pow(O1,b,p)   #key sent to B by O which B thinks is frm A
KOA=pow(A,o2,p)       #A and O computes the same key which is diff from B
KOB=pow(B,o1,p)       #B and O computes the same key which is diff from A 
print("KAO and KOA:")
print(KAO)
print(KOA)
print(KAO==KOA)
print("KBO and KOB")
print(KBO)
print(KOB)
print(KBO==KOB)
print("KBA and KAB")  #A and B computes different Keys
print(KBA)
print(KAB)
print(KBA==KAB)

