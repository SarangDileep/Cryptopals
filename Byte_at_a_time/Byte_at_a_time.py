from Crypto.Cipher import AES 

def encryption(y):
	key="YELLOW SUBMARINE"
	x='Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
	x=y+x
	w=16-(len(x)%16)
	n=chr(w)
	for j in range(w):
		x=x+n
	ct=cypher.encrypt(x)
	return(ct)

key="YELLOW SUBMARINE"
cypher=AES.new(key,AES.MODE_ECB)
x='SECRET'
c=''
count=0
l=0
s=''
for k in range(1,16):
	y=k*"a"
	l=len(y)
	c=encryption(y)
	r=encryption('')
	if(len(c)>len(r) and len(c)%16==0):
		lenc=len(c)
		break;
		
slen=len(r)-l
q=''
a=""
for m in range(len(r)-1,len(r)-slen-1,-1):
	q="a"*m
	enc=encryption(q)
	for j in range(128):
		new=m*"a"+a+chr(j)
		comp=encryption(new)
		if(comp[0:slen]==enc[0:slen]):
			a+=chr(j)
			break;
			
print(a)
