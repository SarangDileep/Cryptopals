from Crypto.Cipher import AES

def add(s):
    def encrypt(pt):
        key="0"*16
        iv="1"*16
        cipher = AES.new(key, AES.MODE_CBC,iv)
        ct= cipher.encrypt(pt)
        return(ct)
    s="comment1=cooking%20MCs;userdata="+s
    s=s+";comment2=%20like%20a%20pound%20of%20bacon"
    s=s.replace(";","")
    s=s.replace("=","")
    w=16-(len(s)%16)
    n=chr(w)
    for j in range(w):
        s=s+n
    s=encrypt(s)
    return(s)

def decrypt(string):
    def dec(ct):
        key="0"*16
        iv="1"*16
        cipher = AES.new(key, AES.MODE_CBC,iv)
        return cipher.decrypt(ct)
    pt=(dec(string))
    if(";admin=true;" in pt):
        return(True)
    else:
        return(False)

def xor(iv,inp):
    x=inp
    key=iv
    s=[]
    l=len(key)
    for i in range(len(x)):
        j=i
        if(j>=l):
            j=j%l
        s.append(chr(ord(x[i])^ord(key[j])))
    s="".join(s)
    return(s)


inp="aaa;admin=true;"
string=add(inp)
print(string)
#print(enc_dec)
iv= string[:16]
pt1=";admin=true;aaaa"
#print iv
pt="20MCsuserdataaaa"
print(pt)
#print(pt)
#print(iv)
iv1=xor(iv,pt)
new_iv= xor(iv1,pt1)
#print(new_iv)
#print xor(new_iv,iv1)
ct=string
print(ct)
ct=ct.replace(ct[:16],new_iv)
#print(ct)
print(decrypt(ct))
