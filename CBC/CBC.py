from Crypto.Cipher import AES
def encrypt(pt):
     key="0"*16
     iv="1"*16
     cipher = AES.new(key, AES.MODE_CBC,iv)
     ct= cipher.encrypt(pt)
     return(ct)
def dec(ct):
     key="0"*16
     iv="1"*16
     cipher = AES.new(key, AES.MODE_CBC,iv)
     print cipher.decrypt(ct)
inp="a"*16
ct=encrypt(inp)
print(ct)
dec(ct)
