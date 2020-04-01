import string
import random
def randomkey():
    letters=string.ascii_letters
    key=''
    for i in range(16):
        key=key+(random.choice(letters))
    return(key)
def randiv():
    letters=string.ascii_letters
    iv=''
    for i in range(16):
        iv=iv+(random.choice(letters))
    return(iv)
def encryption_oracle(plain):
    s=''
    letters=string.ascii_letters
    x=random.randint(5,10)
    for i in range(x):
        s=s+(random.choice(letters))
    plain=s+plain
    for i in range(x):
        plain=plain+(random.choice(letters))
    y=random.randint(1,2)
    if y==1:
        r=cbc(plain)
    else:
        r=ecb(plain)
    return(r)
def cbc(plain):
    from Crypto.Cipher import AES
    import binascii
    def encryption(s):
            x=s
            w=16-(len(x)%16)
            n=chr(w)
            for j in range(w):
                    x=str(x)+n
            ct=cypher.encrypt(x)
            return(ct)
    key=randomkey()
    pt=plain
    cypher=AES.new(key,AES.MODE_ECB)
    a=[]
    p=''
    for i in range (0,len(pt)):
        if i%16==0 and i!=0:
                a.append(p)
                p=''
        p=p+pt[i]
        if i==len(pt)-1:
                a.append(p)
    enc=''
    iv=randiv()
    for i in a:
        b=''
        key=iv
        s=[]
        l=len(key)
        for k in range(len(i)):
                j=k
                if(j>=l):
                        j=j%l
                else:
                        s.append(hex(ord(i[k])^ord(key[j])))
        s="".join(s)
        s=s.replace("0x","")
        c=encryption(s)
        c=(binascii.hexlify(c))
        iv=str(c)
        enc=enc+str(c)
    return(enc)
def ecb(plain):
    from Crypto.Cipher import AES
    import binascii
    def encryption(key,pt):
            w=16-(len(pt)%16)
            n=chr(w)
            for j in range(w):
                    pt=str(pt)+n
            ct=cypher.encrypt(pt)
            return(ct)
    key=randomkey()
    pt=plain
    cypher=AES.new(key,AES.MODE_ECB)
    c=encryption(key,pt)
    c=binascii.hexlify(c)
    return(c)

plain="a"*50
r=encryption_oracle(plain)
print(r)
r=str(r)
r=r[34:]
n=''
for i in range(32):
    n=n+r[i]
p=''
for i in range(32,64):
    p=p+r[i]
if n==p:
    print("ecb")
else:
    print("cbc")
