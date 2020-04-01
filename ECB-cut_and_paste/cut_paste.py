import string
import random
import binascii
from Crypto.Cipher import AES
def encryption(key,pt):
        w=16-(len(pt)%16)
        n=chr(w)
        for j in range(w):
                pt=str(pt)+n
        ct=cypher.encrypt(pt)
        return(ct)
def decrypt(key,ct):
    p=cypher.decrypt(ct)
    l=p[len(p)-1]
    p=p[:-l]
    return(p)
def add(info,key,value):
    info[key]=value
def profile_for(x):
    info={}
    a=''
    for i in range(3):
        if i==0:
            key="Email"
            value=x.replace('&','')
            value=value.replace("=","")
            add(info,key,value)
        if i==1:
            key="Uid"
            value="10"
            add(info,key,value)
        if i==2:
            key="role"
            value="user"
            add(info,key,value)
    return(info)
    newinfo={}
def encoded(info):
    n=''
    for i in info:
        n=n+i+"="+info[i]+"&"
    n=n[:-1]
    return(n)
key="YELLOW SUBMARINE"
cypher=AES.new(key,AES.MODE_ECB)
x="sarangdileep@"
r=profile_for(x)
r=encoded(r)
enc=encryption(key,r)
print(enc)
enc=enc[:-16]
admin=encryption(key,"admin")
enc=enc+admin
dec=decrypt(key,enc)
print(dec)
